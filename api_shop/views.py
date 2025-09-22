from django.shortcuts import render

from .serializers import *
from rest_framework import viewsets
from agency.models import *
from .permission import *

UserProfile, HomePage, AboutPage, ContactPage, FindUsPage, ToursPage, CartPage, Category, Tour, CartItem, Offer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [CustomPermissions]

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [CustomPermissions]


class AboutPageViewSet(viewsets.ModelViewSet):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
    permission_classes = [CustomPermissions]


class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer
    permission_classes = [CustomPermissions]

class FindUsViewSet(viewsets.ModelViewSet):
    queryset = FindUsPage.objects.all()
    serializer_class = FindUsPageSerializer
    permission_classes = [CustomPermissions]

class ToursPageViewSet(viewsets.ModelViewSet):
    queryset = ToursPage.objects.all()
    serializer_class = ToursPageSerializer
    permission_classes = [CustomPermissions]

class CartPageViewSet(viewsets.ModelViewSet):
    queryset = CartPage.objects.all()
    serializer_class = CartPageSerializer
    permission_classes = [CustomPermissions]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [CustomPermissions]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [CustomPermissions]

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [CustomPermissions]

