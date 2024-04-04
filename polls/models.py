from django.db import models




# 음료 종류 (음료 고유 ID (PK), 음료종류명)
# -> 커피, 에이드, 스무디, 차, 라떼
class QuestionDrink(models.Model):        
  category_of_drink = models.CharField(max_length=50)      # 음료 종류명

  def __str__(self) :
    return self.category_of_drink
  



# 선택한 음료 종류의 여러 음료들 제시
# (세부 음료 고유 ID (PK), 음료 세부명, 가격, ice & hot 여부, 음료 종류 고유 ID (FK), )
#  커피 -> 아메리카노 / 카페라떼 / 아인슈페너 / 바닐라라떼 / 카라멜 마끼아또
#  에이드 -> 레몬에이드 / 자몽에이드 / 사과에이드
#  스무디 -> 딸기 스무디 / 요거트 스무디 / 블루베리 스무디
#  차 -> 유자차 / 녹차 / 캐모마일차 / 호박차
#  라떼 -> 녹차라떼 / 고구마 라떼 / 초코라떼 
class ChoiceDrink(models.Model):          
  chosen_drink_category = models.ForeignKey(QuestionDrink, on_delete=models.CASCADE)    # 외래키 - 선택된 음료 카테고리
  name_of_drink = models.CharField(max_length=50)     # 선택한 카테고리에서의 음료 종류명
  price = models.DecimalField(max_digits=8, decimal_places=2)       # 해당 음료의 가격
 
  # 해당음료 온도 선택 여부 (에이드, 스무디는 아이스만 가능)
  HOT_ONLY = 'H'        # 해당 음료가 핫만 가능 
  ICE_ONLY = 'I'        # 해당 음료가 아이스만 가능
  BOTH_OK = 'B'         # 해당 음료 둘 다 가능
  HOT_OR_ICE_CHOICES = [
      (HOT_ONLY, 'Hot Only'),
      (ICE_ONLY, 'Ice Only'),
      (BOTH_OK, 'Both hot and ice')  
      ]
  temperature = models.CharField(max_length=1, choices=HOT_OR_ICE_CHOICES, default=BOTH_OK)
  

