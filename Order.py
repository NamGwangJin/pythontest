import Menu
from Sales import *
class Order (Menu.Menu):
    def __init__(self):
        self.sales = Sales()
        self.orderList = []
        super().__init__()
        self.mobile = ''

    def addOrder(self):
        self.display()
        while True:
            num = input('주문하실 메뉴번호를 입력해주세요. [enter:종료]')
            if num == '':
                break
            num = int(num) - 1
            qty = int(input('수량을 입력해주세요.'))
            total = qty * self.menuList[num]['price']
            self.orderList.append( { 'name':self.menuList[num]['menu'], 'qty':qty, 'total':total } )

    def displayOrder(self):
        sum = 0
        totalQty = 0
        print('-'*10 + '주문내역' + '-'*10)
        for i in self.orderList:
            sum += i['total']
            totalQty += i['qty']
            print( self.orderList.index(i) + 1, "{0:>12}".format(i['name']), f"{i['qty']}개", f"{i['total']}원" )
        print('-'*27 + '\n' + "{0:>16}".format(totalQty) + "개 " + f"{sum}원")

    def deleteOrder(self):
        self.displayOrder()
        while True:
            delete = input('삭제할 주문 번호를 입력해주세요 [enter:삭제 종료]')
            if delete == "":
                print('메뉴 삭제를 종료합니다.')
                break
            del self.orderList[int(delete) - 1]
            print(delete+'번 주문 삭제 완료.')
        self.displayOrder()

    def controlOrder(self):
        while True:
            ment = input('주문 관리 모드입니다. [C:주문하기][R:주문내역출력][D:주문내역삭제][enter:주문완료]\n')
            if ment == "C" or ment == "c":
                self.addOrder()
            elif ment == "R" or ment == 'r':
                self.displayOrder()
            elif ment == "D" or ment == 'd':
                self.deleteOrder()
            elif ment == "":
                if len(self.orderList) <= 0:
                    print('담긴 메뉴가 없어 주문을 종료합니다.')
                    break
                mobile = input('모바일번호를 입력하세요.')
                if mobile == '':
                    print('적립을 건너뜁니다.')
                    self.sales.add(mobile, self.orderList)
                    self.orderList.clear()
                    break
                else:
                    print(mobile + '번호로 적립이 완료되었습니다.')
                    self.sales.add(mobile, self.orderList)
                    self.orderList.clear()
                    break
            else:
                print('잘못된 키를 입력하셨습니다.')
