from django.contrib import admin

from .models import QuestionDrink, ChoiceDrink, Order

admin.site.register(QuestionDrink)
admin.site.register(ChoiceDrink)
admin.site.register(Order)
