import Menu

menu = Menu.Menu()

while True:
    work = input('진행할 작업을 선택해주세요. [M:메뉴관리][O:주문관리][S:매출관리][enter:종료]')
    # 메뉴 관리
    if work == 'M' or work == 'm':
        while True:
            ment = input('메뉴 관리 모드입니다. [C:메뉴추가][R:메뉴판출력][U:메뉴수정][D:메뉴삭제][enter:종료]\n')
            if ment == "C" or ment == "c":
                menu.add()
                continue
            elif ment == "R" or ment == 'r':
                menu.display()
                continue
            elif ment == "U" or ment == 'u':
                menu.update()
                continue
            elif ment == "D" or ment == 'd':
                menu.delete()
                continue
            elif ment == "":
                print('메뉴관리를 종료합니다.')
                menu.save()
                break
            else:
                print('잘못된 키를 입력하셨습니다.')
                continue
    # 주문 관리
    elif work == 'O' or work == 'o':
        while True:
            ment = input('주문 관리 모드입니다. [C:주문하기][R:주문내역출력][U:주문내역수정][D:주문내역삭제][enter:종료]\n')
            if ment == "C" or ment == "c":
                # order.add()
                continue
            elif ment == "R" or ment == 'r':
                # order.display()
                continue
            elif ment == "U" or ment == 'u':
                # order.update()
                continue
            elif ment == "D" or ment == 'd':
                # order.delete()
                continue
            elif ment == "":
                print('주문관리를 종료합니다.')
                menu.save()
                break
            else:
                print('잘못된 키를 입력하셨습니다.')
                continue
    # 매출 관리
    elif work == 'S' or work == 's':
        # 매출내역 출력
        continue
    # 종료
    elif work == "":
        print('카페관리 프로그램을 종료합니다.')
        break
    # 잘못된 키 입력
    else:
        print('잘못된 키를 입력하셨습니다.')
        continue