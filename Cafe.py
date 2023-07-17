import Order

cafe = Order.Order()

while True:
    work = input('진행할 작업을 선택해주세요. [M:메뉴관리][O:주문관리][S:매출출력][enter:종료]')

    # 메뉴 관리
    if work == 'M' or work == 'm':
        cafe.control()

    # 주문 관리
    elif work == 'O' or work == 'o':
        cafe.controlOrder()

    # 매출 출력
    elif work == 'S' or work == 's':
        cafe.sales.display()

    # 종료
    elif work == "":
        print('카페관리 프로그램을 종료합니다.')
        break

    # 잘못된 키 입력
    else:
        print('잘못된 키를 입력하셨습니다.')