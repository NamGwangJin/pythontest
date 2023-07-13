# import pkg1.Circle as won # 외부모듈
# from pkg1.Circle import *

# ar = around(4)
# sq = square(4)
# vo = volume(4)

# if __name__ == '__main__':
#     print (f"둘레 : {ar:5.2f}\n면적 : {sq:5.2f}\n체적 : {vo:5.2f}")

# def greeting(message='Hello',times=4):
#     str1 = message * times
#     print(str1)
# greeting('hi',9)
#
# def between(x):
#     if 10<=x<=20:
#         return 'between 10 and 20'
#     else:
#         return 'not between 10 and 20'
#
# print(between(13))
# print(between(23))

# # 예외 처리
# while True:
#     try :
#         i = int(input('첫번째 값 입력'))
#         j = int(input('두번째 값 입력'))
#         print(i/j)
#         break
#     except ZeroDivisionError:
#         print('불능')
#     except ValueError:
#         print('적절하지 않은 값이 입력되었습니다.')

# # 파이썬 문자열 인덱싱, 슬라이싱
# str1 = "beautiful jeju island"
# str2 = ""
# for x in str1:
#     str2 = x + str2
# str1 = str2
# print(str1)

# str1 = input('문자열을 입력하시오.')
#
# for x in range(len(str1)-1,-1,-1):
#     str1 += str1[x]
# else:
#     str1 = str1[len(str1)//2:]
#     print(str1)

# str1 = "Mountain Fountain Maintain Captain"
# print(str1.lower())
# print(str1.upper())
# print(str1.swapcase())
# print(str1.find('tain'),len(str1))
# print(str1.rfind('tain'))
# print(str1.find('tain',10))
# print(str1.replace('tain','tion'))
# print(str1.replace('tain','tion',1))
# print("avion"+"navigation")
# print("avion"*5)
# print(len('avion'))
# str1 = "Good Morning Vietnam Saigon"
# ar = str1.split(' ')
# print(ar)