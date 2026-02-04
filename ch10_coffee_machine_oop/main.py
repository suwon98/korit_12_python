from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
# 현재 상황에서 menu.menu를 활용하여 espresso라는 str을 추출하려면 어떡해야 하나요?

while is_on:
    choice = input(f'어떤 음료를 드시겠습니까? {menu.get_items()} >>> ')
    # todo  - 1 : off일 때는 동일 report일 때 메서드의 호출로 현재 재료와 수익을 조회하시오.
    if choice in '정지':
        print('커피머신을 종료합니다.')
        is_on = False
    elif choice in '정산':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)     # 결과값이 MenuItem 객체거나 None
        # if drink == None:
        #     continue
        if drink and coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)