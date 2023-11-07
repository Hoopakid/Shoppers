from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('cart', ShoppingCartTemplateView.as_view(), name='cart'),
    path('about', about, name='about'),
    path('shop', shop, name='shop'),
    path('contact', contact, name='contact'),
    path('shop-single', shop_single, name='shop-single'),
    path('checkout', OrderView.as_view(), name='checkout'),
    path('thankyou', thanks, name='thanks'),
    path('add-product', AddProductView.as_view(), name='add-product'),
    path('comment', CommentView.as_view(), name='comment'),

    # API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
]


# ORM -> Object Relational Mapping
