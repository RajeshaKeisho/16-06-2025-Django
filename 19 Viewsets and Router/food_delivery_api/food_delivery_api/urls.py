from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from delivery.views import CustomerViewSet, ResturantViewSet, MenuItemViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'restaurants', ResturantViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
