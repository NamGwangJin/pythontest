arMenu = []
sum = 0
while True: # 메뉴 추가
    menu = input("메뉴명을 입력하세요.\n")
    if menu == "":
        print("메뉴 추가 종료. 메뉴판을 출력합니다.")
        break
    price = int(input("가격을 입력하세요.\n"))
    arMenu.append( {'메뉴명': menu, '가격': price} )

print('-'*10,'메뉴판','-'*10)
for x in arMenu: # 메뉴판 출력
    sum += x['가격']
    print(f"{x['메뉴명']:15s} {x['가격']:5d}원")

print(f"\n메뉴 금액 합계 : {sum}원")