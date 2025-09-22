from django.urls import path
from . import views

app_name = 'agency'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('find-us/', views.FindUsView.as_view(), name='find_us'),
    path('tours/', views.ToursView.as_view(), name='tours'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('tours/all/', views.AllToursView.as_view(), name='all_tours'),
    path('offers/', views.OffersView.as_view(), name='offers'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-to-cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('update-cart-item/', views.UpdateCartItemView.as_view(), name='update_cart_item'),
    path('delete-from-cart/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
]