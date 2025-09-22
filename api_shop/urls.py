from .views import *
from .views import UserProfileViewSet
from rest_framework import routers

urlpatterns = [

]

router = routers.SimpleRouter()
router.register('userProfile', UserProfileViewSet, basename='userProfile')
router.register('homePage', HomePageViewSet, basename='homePage')
router.register('aboutPage', AboutPageViewSet, basename='aboutPage')
router.register('contactPage', ContactPageViewSet, basename='contactPage')
router.register('findUsPage', FindUsViewSet, basename='findUsPage')
router.register('toursPage', ToursPageViewSet, basename='toursPage')
router.register('cartPage', CartPageViewSet, basename='cartPage')
router.register('category', CategoryViewSet, basename='category')
router.register('tour', TourViewSet, basename='tour')
router.register('cartItem', CartItemViewSet, basename='CartItem')
router.register('offer', OfferViewSet, basename='offer')
urlpatterns += router.urls