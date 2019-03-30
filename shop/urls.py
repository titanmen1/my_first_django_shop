from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('product/<product_slug>', views.product_view, name='product_view'),
    path('category/<category_slug>', views.category_view, name='category_view'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/', views.add_to_cart_view, name='add_to_cart_view'),
    path('remove_from_cart/', views.remove_from_cart_view, name='remove_from_cart_view'),
    path('change_item_qty/', views.change_item_qty, name='change_item_qty'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('order/', views.order_create_view, name='order_create_view'),
    path('thank_you/', views.make_order_view, name='thank_you'),
    path('account/', views.account_view, name='account_view'),
    path('registration/', views.registration_view, name='registration_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', LogoutView.as_view(next_page='base_view'), name='logout')
]