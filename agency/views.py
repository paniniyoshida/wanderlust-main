from django.views.generic import TemplateView, ListView, CreateView, FormView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django import forms
from .models import HomePage, AboutPage, ContactPage, FindUsPage, ToursPage, CartPage, Category, Tour, CartItem, Offer, UserProfile
from django.contrib.auth.models import User

# Кастомная форма регистрации
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

# Миксин для требования авторизации
class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# Статические страницы
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = HomePage.objects.first()
        return context

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = AboutPage.objects.first()
        return context

class ContactsView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = ContactPage.objects.first()
        return context

class FindUsView(LoginRequiredMixin, TemplateView):
    template_name = 'find_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = FindUsPage.objects.first()
        return context

class ToursView(LoginRequiredMixin, TemplateView):
    template_name = 'tours.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = ToursPage.objects.first()
        return context

# Списки
class CategoriesView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = ToursPage.objects.first()
        return context

class AllToursView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = 'all_tours.html'
    context_object_name = 'tours'

    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        if category_id:
            return Tour.objects.filter(category_id=category_id)
        return Tour.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = ToursPage.objects.first()
        return context

class OffersView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offers.html'
    context_object_name = 'offers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = ToursPage.objects.first()
        return context

class CartView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = CartPage.objects.first()
        for item in context['cart_items']:
            item.total_cost = item.tour.price * item.quantity
        return context

class ProfileView(LoginRequiredMixin, ListView):
    model = CartItem
    template_name = 'profile.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

# Авторизация
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('agency:home')

    def form_valid(self, form):
        user = form.save()
        # Создаем профиль пользователя с email
        UserProfile.objects.create(user=user, email=user.email)
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('agency:home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

# Выход (FBV, так как дженерик избыточен)
def logout_view(request):
    logout(request)
    return redirect('agency:login')

# Корзина (AJAX)
class AddToCartView(LoginRequiredMixin, CreateView):
    model = CartItem
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            tour_id = request.POST.get('tour_id')
            quantity = request.POST.get('quantity', '1')
            post_data = request.POST.dict()  # Для отладки

            if not tour_id:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Тур не указан',
                    'post_data': post_data
                }, status=400)
            
            try:
                quantity = int(quantity)
                if quantity < 1:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Количество должно быть положительным',
                        'post_data': post_data
                    }, status=400)
            except ValueError:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Неверное количество',
                    'post_data': post_data
                }, status=400)

            tour = get_object_or_404(Tour, id=tour_id)
            cart_item, created = CartItem.objects.get_or_create(
                user=self.request.user,
                tour=tour,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Тур добавлен в корзину',
                'post_data': post_data
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
                'post_data': request.POST.dict()
            }, status=500)

class UpdateCartItemView(LoginRequiredMixin, CreateView):
    model = CartItem
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            cart_item_id = request.POST.get('cart_item_id')
            quantity = request.POST.get('quantity')
            post_data = request.POST.dict()  # Для отладки

            if not cart_item_id:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Элемент корзины не указан',
                    'post_data': post_data
                }, status=400)

            try:
                quantity = int(quantity)
                if quantity < 1:
                    return JsonResponse({
                        'status': 'error',
                        'message': 'Количество должно быть положительным',
                        'post_data': post_data
                    }, status=400)
            except ValueError:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Неверное количество',
                    'post_data': post_data
                }, status=400)

            cart_item = get_object_or_404(CartItem, id=cart_item_id, user=self.request.user)
            cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Количество обновлено',
                'post_data': post_data,
                'total_cost': cart_item.tour.price * cart_item.quantity
            })
        except CartItem.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Элемент корзины не найден',
                'post_data': request.POST.dict()
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
                'post_data': request.POST.dict()
            }, status=500)

class DeleteFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        try:
            cart_item_id = request.POST.get('cart_item_id')
            if not cart_item_id:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Элемент корзины не указан',
                    'post_data': request.POST.dict()
                }, status=400)
            
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Тур удален из корзины',
                'post_data': request.POST.dict()
            })
        except CartItem.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Элемент корзины не найден',
                'post_data': request.POST.dict()
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e),
                'post_data': request.POST.dict()
            }, status=500)

    def get_object(self):
        cart_item_id = self.request.POST.get('cart_item_id')
        return get_object_or_404(CartItem, id=cart_item_id, user=self.request.user)

    def get_success_url(self):
        # Не используется, так как возвращаем JSON
        pass