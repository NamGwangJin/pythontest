class Sales:
    def __init__(self):
        self.salesList = []

    def add(self,mobile,oList):
        if mobile == '':
            mobile = '----비회원----'
        for i in oList:
            self.salesList.append( {'mobile':mobile, 'name':i['name'], 'qty':i['qty'], 'total':i['total']} )

    def display(self):
        print('-'*15 + '매출내역' + '-'*15)
        sum = 0
        for i in self.salesList:
            sum += i['total']
            print(f"{i['mobile']}", f"{i['name']:10s}", f"{i['qty']}개", f"{i['total']}원")
        print('-'*15 + '매출총액' + '-'*15 + '\n' + "{0:>20}".format(sum) + "원")

