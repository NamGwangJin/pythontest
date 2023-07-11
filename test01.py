import math

 ## format , print 연습
# i, j, k, str1 = 0, 1, 3.14, 'hello world'
# print("i ["+str(i)+"] j ["+str(j)+"] str1 ["+str1+"]")
# print(str(i)+str1)
# print(f"i [{i}] j [{j}] k [{k}] str1 [{str1}]")
# print(f"i={i:2d} j={j:3d} k={k:4.2f} str1={str1:5s}")
# print('i={0}, j={1}, k={2}, str1={3}'.format(i,j,k,str1))
# print('i=%2d, j=%3d, k=%.2f, str1=%12s'%(i,j,k,str1))


 ## file 오픈, 읽기
# f = open('c:/temp/menu.txt','r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line,end='')
# f.close()

 ## for문
# for i in range(10): # == for(int i=0; i<10; 1++)
#   print(i)

 ## 구구단
# for i in range(2,10):
#   print('-'*10,f'{i}단','-'*10)
#   for j in range(1,10):
#     print(f"{i} x {j} = {i*j:2d}")

 ## 연산자
# i = 8//3 # 2
# j = 8%3 # 2
# k = 2**4 # 16
# print(i,j,k)

 ## 타입변환
# i=2
# j=2.0
# k=3.14
# m='240'
# print(float(i),int(j),str(i),str(j),int(k))
# print(int(m),float(m))

 ## 홀수 찍기
# for i in range (1,100,2):
#   print(i)
#
# for i in range(1,100):
#   if i%2==0:
#     continue
#   print(i)

 ## 피보나치
# a=0; b=1
# fibo=a+b
# print(a)
# print(b)
# while fibo<1000 :
#   print(fibo)
#   a = b
#   b = fibo
#   fibo = a + b
 ## 피보나치(2)
# a,b = 0,1
# fibo = a+b
# print(f"{a}\n{b}")
# for i in range(1000) :
#     if fibo>1000 :
#         break
#     print(fibo)
#     a=b
#     b=fibo
#     fibo=a+b

 ## input
# name=input('이름을 입력하시오\n')
# age=input('나이를 입력하시오\n')
# print(name, age)

 ## 1000이하의 소수
# for a in range(2, 1001):
#     for b in range(2, a+1):
#         if(a % b == 0):
#             break
#     if(a == b) :
#         print(a)

 ## 피라미드
# for i in range (1,12) :
#     print("*"*i)
# else :
#     for i in range (i,0,-1) :
#         print("*"*i)

 ## 최대공약수, 최소공배수
# while True:
#     a=input('수를 입력하세요\n')
#     b=input('수를 입력하세요\n')
#     a,b=int(a),int(b)
#     p=1
#     if (a==b):
#         print("같은 수를 입력하셨습니다.")
#         continue
#     if (a<b):
#         while True:
#             for x in range(2, a + 1):
#                 if a % x == 0 and b % x == 0:
#                     a = a // x
#                     b = b // x
#                     p = p * x
#                     break
#                 else:
#                     continue
#             else:
#                 print('최대공약수 : ', p)
#                 print('최소공배수 : ', p * a * b)
#                 break
#     elif (b<a):
#         while True:
#             for x in range(2, b + 1):
#                 if a % x == 0 and b % x == 0:
#                     a = a // x
#                     b = b // x
#                     p *= x
#                     break
#                 else:
#                     continue
#             else:
#                 print('최대공약수 : ', p)
#                 print('최소공배수 : ', p * a * b)
#                 break
#     break

 ## 최대공약수 최소공배수 (2)
# for i in range(min(a,b),0,-1):
#     if a%i == 0 and b%i==0:
#         print(i)
#         break
# for i in range(max(a,b),(a*b)+1):
#     if i%a==0 and i%b==0:
#         print(i)
#         break

## 최대공약수 최소공배수 (3)
# a=input('수를 입력하세요\n')
# b=input('수를 입력하세요\n')
# a,b=int(a),int(b)
# if b<a:
#     a, b = b, a
# for x in range(2, a + 1):
#     if a % x == 0 and b % x == 0:
#         c = a / x
#         d = b / x
#         p = 1
#         p = p * x
# else:
#     print(p,p*c*d)

 ## 이차방정식 해 구하기
# a=input('a를 입력하세요\n')
# b=input('b를 입력하세요\n')
# c=input('c를 입력하세요\n')
# a,b,c=int(a),int(b),int(c)
#
# x1 = (-b-math.sqrt(b**2-4*a*c)) / (2*a)
# x2 = (-b+math.sqrt(b**2-4*a*c)) / (2*a)
#
# print (f"x = {x1} or {x2}")

 ## 파이썬 함수
# def plus(a,b,c):
#     return a+b+c
# print(plus(10,7,5))
#
# def minus(a,b,c):
#     print(a-b-c)
# minus(10,7,5)