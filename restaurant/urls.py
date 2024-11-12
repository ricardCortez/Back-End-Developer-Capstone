from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Create a router and register the BookingViewSet
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

# Add the router URLs to the urlpatterns list
urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu/', views.MenuItemsView.as_view(), name='menu_items'),  # For listing and creating menu items
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),  # For retrieving, updating, or deleting a single menu item
    path('api/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]