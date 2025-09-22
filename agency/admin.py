from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile, HomePage, AboutPage, ContactPage, FindUsPage, ToursPage, CartPage, Category, Tour, CartItem, Offer
from .forms import TourAdminForm

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email')
    search_fields = ('user__username', 'email')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'cta_text', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(FindUsPage)
class FindUsPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(ToursPage)
class ToursPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category_cta_text', 'all_tours_cta_text', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(CartPage)
class CartPageAdmin(admin.ModelAdmin):
    list_display = ('headline', 'banner_image')
    search_fields = ('headline', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    form = TourAdminForm
    list_display = ('name', 'price', 'category', 'image_preview', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category', 'created_at')
    list_per_page = 20
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'price', 'category')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('image_preview', 'created_at')
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; border-radius: 5px;" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = "Превью изображения"
    
    def created_at(self, obj):
        return obj.id  # Используем ID как пример, можно добавить поле created_at в модель
    created_at.short_description = "ID"

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'quantity')
    search_fields = ('user__username', 'tour__name')
    list_filter = ('user',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'discounted_price')
    search_fields = ('name', 'description')