class Menu:
    def __init__(self):
        self.menuList = []
        self.build()
        # self.sum = 0
    def build(self):
        try:
            f = open('c:/temp/menu.txt','r')
            arMenu = f.readlines()
            for i in range(len(arMenu)):
                menu = arMenu[i].split(',')
                self.menuList.append({'menu':menu[0],'price':int(menu[1])})
            print('메뉴를 불러왔습니다.')
        except:
            print('메뉴를 불러오지 못했습니다.')
        f.close()

    def save(self):
        try:
            f = open('c:/temp/menu.txt','w')
            for i in self.menuList:
                arMenu = i['menu']+","+str(i['price'])+'\n'
                f.write(arMenu)
            print('메뉴 저장이 완료되었습니다.')
        except:
            print('메뉴를 저장하지 못했습니다.')
        f.close()

    def add(self):
        while True:
            name = input('추가할 메뉴명을 입력하세요. [enter: 메뉴 추가 종료]\n')
            if name == '':
                print('메뉴추가를 종료합니다.')
                break
            price = int(input(name+"의 가격을 입력하세요."))
            self.menuList.append({'menu':name,'price':price})
            print(name+" 메뉴 추가 완료")
            self.display()

    def display(self):
        print('-' * 10, '메뉴판', '-' * 10)
        for i in self.menuList:
            # self.sum += i['price']
            print(self.menuList.index(i) + 1,"{0:>12}".format(i['menu']),f"{i['price']:5d}원")
        # print(f"\n메뉴 총액 : {self.sum:8d}원")

    def update(self):
        self.display()
        while True:
            change = input('수정할 메뉴 번호를 입력해주세요. [enter: 수정 종료]')
            if change == "":
                print('메뉴 수정을 종료합니다.')
                break
            print(change+'번 메뉴 '+self.menuList[int(change) - 1]['menu']+" 수정을 진행합니다.")
            name = input('변경할 메뉴명을 입력해주세요.')
            price = int(input(name+'의 가격을 입력해주세요.'))
            self.menuList[int(change) - 1] = {'menu':name,'price':price}
            self.display()
        self.save()

    def delete(self):
        self.display()
        while True:
            delete = input('삭제할 메뉴 번호를 입력해주세요 [enter:삭제 종료]')
            if delete == "":
                print('메뉴 삭제를 종료합니다.')
                break
            del self.menuList[int(delete) - 1]
            print(delete+'번 메뉴 삭제 완료.')
            self.display()
        self.save()