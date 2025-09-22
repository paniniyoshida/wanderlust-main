from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username

class HomePage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')
    cta_text = models.CharField(max_length=100, blank=True, verbose_name='Текст кнопки CTA')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return self.headline

class AboutPage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страница "О нас"'

    def __str__(self):
        return self.headline

class ContactPage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')

    class Meta:
        verbose_name = 'Страница контактов'
        verbose_name_plural = 'Страница контактов'

    def __str__(self):
        return self.headline

class FindUsPage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')

    class Meta:
        verbose_name = 'Страница "Как нас найти"'
        verbose_name_plural = 'Страница "Как нас найти"'

    def __str__(self):
        return self.headline

class ToursPage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')
    category_cta_text = models.CharField(max_length=100, blank=True, verbose_name='Текст кнопки категорий')
    all_tours_cta_text = models.CharField(max_length=100, blank=True, verbose_name='Текст кнопки всех туров')

    class Meta:
        verbose_name = 'Страница туров'
        verbose_name_plural = 'Страница туров'

    def __str__(self):
        return self.headline

class CartPage(models.Model):
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    banner_image = models.CharField(max_length=100, blank=True, verbose_name='Баннер (имя файла)')

    class Meta:
        verbose_name = 'Страница корзины'
        verbose_name_plural = 'Страница корзины'

    def __str__(self):
        return self.headline

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='tours/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        return f"{self.tour.name} ({self.quantity})"

class Offer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Исходная цена')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидочная цена')

    class Meta:
        verbose_name = 'Специальное предложение'
        verbose_name_plural = 'Специальные предложения'

    def __str__(self):
        return self.name