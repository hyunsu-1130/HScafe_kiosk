# HScafe_kiosk
# 카페 키오스크 만들기
# QuestionDrink : 음료종류 ( 커피, 에이드, 스무디, 차, 라떼)
# ChoiceDrink : 커피 -> 아메리카노 / 카페라떼 / 아인슈페너 / 바닐라라떼 / 카라멜 마끼아또
#          에이드 -> 레몬에이드 / 자몽에이드 / 사과에이드
#          라떼 -> 녹차라떼 / 고구마 라떼 / 초코라떼 
#          스무디 -> 딸기 스무디 / 요거트 스무디 / 블루베리 스무디
#          차 -> 유자차 / 녹차 / 캐모마일차 / 호박차

# ㄱ. 음료종류 선택 (음료 고유 ID (PK), 음료종류명)
# ㄴ. 해당 음료 종류의 세부 종류 선택 (세부 음료 고유 ID (PK), 음료 세부명, 가격, ice & hot 여부, 음료 종류 고유 ID (FK), )
# ㄷ. 해당 음료 ice or hot 선택 - 에이드와 스무디는 only ice
# ㄹ. 포인트 적립 - 번호 입력
# ㅁ. 결제하기 - 카드 or 모바일 페이(카카오페이) / 현금은 불가
# ㅂ. 영수증 출력하기 - 선택사항