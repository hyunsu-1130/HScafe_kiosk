from django.urls import path
from .views import OrderCreateView
from . import views

urlpatterns = [
    #path("", views.rich_cafe),
    path("", views.drink_category_list, name="category"),
    path('category/<int:category_id>/', views.drink_list, name='drink_list'),

    # 주문 생성 뷰에 대한 URL 패턴 추가
    path('order/create/', OrderCreateView.as_view(), name='order_create'),  
]