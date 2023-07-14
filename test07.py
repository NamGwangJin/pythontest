import Menu

menu = Menu.Menu()

while True:
    ment = input('진행할 작업을 선택해주세요. [C:메뉴추가][R:메뉴판출력][U:메뉴수정][D:메뉴삭제][enter:종료]\n')
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
        print('프로그램을 종료합니다.')
        menu.save()
        break
    else:
        print('잘못된 키를 입력하셨습니다.')
        continue