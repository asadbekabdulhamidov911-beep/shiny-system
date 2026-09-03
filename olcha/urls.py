from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('swiper1', views.Swiper1ViewSet)
router.register('swiper2', views.Swiper2ViewSet)
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
]