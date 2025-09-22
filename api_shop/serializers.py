from rest_framework import serializers
from agency.models import UserProfile, HomePage, AboutPage, ContactPage, FindUsPage, ToursPage, CartPage, Category, Tour, CartItem, Offer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'user',
            'email'
        ]

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = [
            'headline',
            'description',
            'banner_image',
            'cta_text'
        ]

class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = [
            'headline',
            'description',
            'banner_image'
        ]

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = [
            'headline',
            'description',
            'banner_image'
        ]

class FindUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindUsPage
        fields = [
            'headline',
            'description',
            'banner_image'
        ]

class ToursPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursPage
        fields = [
            'headline',
            'description',
            'banner_image',
            'category_cta_text',
            'all_text_cta_text'
        ]

class CartPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartPage
        fields = [
            'headline',
            'description',
            'banner_image'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            'name',
            'description',
            'price',
            'category',
            'image',
            'created_at',
            'updated_at'
        ]

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'user',
            'tour',
            'quantity'
        ]

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            'name',
            'description',
            'original_price',
            'discounted_price'
        ]