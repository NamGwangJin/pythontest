class Menu:
    def __init__(self):
        self.menuList = []
        self.build()
    def build(self):
        try:
            f = open('c:/temp/menu.txt','r')
            arMenu = f.readlines()
            for i in range(len(arMenu)):
                menu = arMenu[i].split(',')
                self.menuList.append({'menu':menu[0],'price':int(menu[1])})
            f.close()
        except:
            print('메뉴를 불러오지 못했습니다.')

    def save(self):
        try:
            f = open('c:/temp/menu.txt','w')
            for i in self.menuList:
                arMenu = i['menu']+","+str(i['price'])+'\n'
                f.write(arMenu)
            f.close()
        except:
            print('메뉴를 저장하지 못했습니다.')

    def control(self):
        while True:
            ment = input('메뉴 관리 모드입니다. [C:메뉴추가][R:메뉴판출력][U:메뉴수정][D:메뉴삭제][enter:종료]\n')
            if ment == "C" or ment == "c":
                self.add()
            elif ment == "R" or ment == 'r':
                self.display()
            elif ment == "U" or ment == 'u':
                self.update()
            elif ment == "D" or ment == 'd':
                self.delete()
            elif ment == "":
                print('메뉴관리를 종료합니다.')
                self.save()
                break
            else:
                print('잘못된 키를 입력하셨습니다.')

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
            print(self.menuList.index(i) + 1,"{0:>12}".format(i['menu']),f"{i['price']:5d}원")

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