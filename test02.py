# # Create(add)
# arName = [1, 'Hello', 3.14, True, None, "world"]
# arName.append(25)
# arName.insert(3,'남광진')
# arName.extend(arName) # 리스트와 리스르를 연결
#
# # Read
# for x in arName:
#   print(x)
# print('-'*30)
# for i in range(len(arName)):
#   print(i,"=",arName[i])
# x = arName.pop(3) # 인덱스 위치의 값을 반환하고 삭제
#
# # Update
# arName[3] = '하이미디어'
# print('-'*30)
# for x in arName:
#   print(x)
#
# # Delete
# arName.remove('하이미디어') # 값으로 치우기
# print('-'*30)
# for x in arName:
#   print(x)
#
# del(arName[3]) # 인덱스로 지우기
# print('-'*30)
# for x in arName:
#   print(x)
#
# arName.clear() # 리스트 전체 지우기
#
# # 기타 함수
# arName.sort() # 정렬
# arName.reverse() # 리스트를 역순으로 만든다.

# # reverse 구현
# for x in range(len(arList)):
#     change = arList.pop()
#     arList.insert(x,change)
# print(arList)

# arResult = []
# for x in range(len(arList)-1,-1,-1):
#     arResult.append(arList[x])
# print(arResult)

# i = 0
# j = len(arList)-1
# while i<j:
#     arList[i],arList[j] = arList[j],arList[i]
#     i += 1
#     j -= 1
# print(arList)

# # 메뉴 리스트
# arMenu = []
# arPrice = []
# sum = 0
# while True:
#     menu = input("메뉴명을 입력하세요.\n")
#     if menu == "":
#         print("메뉴 추가 종료. 메뉴판을 출력합니다.")
#         break
#     price = int(input("가격을 입력하세요.\n"))
#     arMenu.append(menu)
#     arPrice.append(price)
# print('-'*10,'메뉴판','-'*10)
# for x in range(len(arMenu)):
#     sum += arPrice[x]
#     print(f"{arMenu[x]:15s} {arPrice[x]:5d}원")
# print(f"\n메뉴 금액 합계 : {sum}원")

# # 메뉴 리스트 딕셔너리로 변형
arMenu = []
sum = 0
while True: # 메뉴 추가
    menu = input("메뉴명을 입력하세요.\n")
    if menu == "":
        print("메뉴 추가 종료. 메뉴판을 출력합니다.")
        break
    price = int(input("가격을 입력하세요.\n"))
    arMenu.append( {'menu':menu, 'price':price} )

print('-'*10,'메뉴판','-'*10)
for x in arMenu: # 메뉴판 출력
    sum += x['price']
    print(f"{x['menu']:15s} {x['price']:5d}원")

print(f"\n메뉴 금액 합계 : {sum}원")

# # 배열 안의 for문, 함수
# def prime():
#     arPrime = []
#     for i in range(1000):
#         for j in range(2, i):
#             if i%j == 0 : break
#         else:
#             arPrime.append(i)
#     return arPrime
#
# arList = prime()
# print(arList)
#
# arNumber = [ i for i in range(0,100,3) ]
# print(arNumber)