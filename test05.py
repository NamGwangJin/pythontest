# import re # Regular Expreesion module import
from datetime import date, datetime

# def checkEmail(email):
#     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     if re.fullmatch(regex, email):
#         return True
#     else:
#         return False
# def checkMobile(mobile):
#     regex = "(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
#     if re.fullmatch(regex, mobile):
#         return True
#     else:
#         return False
#
# phone = input('휴대폰 번호를 입력하세요.')
# if checkMobile(phone):
#     print('사용 가능한 휴대폰 번호입니다.')
# else:
#     print('잘못된 휴대폰 번호입니다.')
#
# userid = input('email을 입력하세요.\n')
# if checkEmail(userid):
#     print('사용 가능한 이메일입니다.')
# else:
#     print('잘못된 이메일 형식입니다.')

now = datetime.now()
print(now)
print(now.strftime("%Y/%m/%d %H:%M:%S"))