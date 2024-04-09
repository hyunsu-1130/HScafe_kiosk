from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView
from polls.models import QuestionDrink, ChoiceDrink, Order
from django.views.generic.edit import FormView
from .forms import OrderForm
from django.utils import timezone



# 음료 카테고리 리스트 제시
def drink_category_list(request):
    categories = QuestionDrink.objects.all()
    return render(request, 'polls/drink_category_list.html', {'categories': categories})


# 선택된 카테고리의 음료 리스트 제시
def drink_list(request, category_id):
    category = QuestionDrink.objects.get(pk=category_id)
    drinks = ChoiceDrink.objects.filter(chosen_drink_category_id = category_id)
    return render(request, 'polls/drink_list.html', {'category' : category , 'drinks' : drinks})


class OrderCreateView(FormView):
    template_name = 'order_form.html'
    form_class = OrderForm
    success_url = '/order/success/'

    def form_valid(self, form):
        # 폼이 유효한 경우, 주문을 생성합니다.
        order = form.save(commit=False)  # 데이터베이스에 저장하지 않고 주문 객체 생성
        order.order_date = timezone.now()  # 주문 날짜 설정
        order.order_price = order.order_item.price * order.order_item_count  # 주문 가격 계산
        order.save()  # 주문 객체를 데이터베이스에 저장
        return super().form_valid(form)