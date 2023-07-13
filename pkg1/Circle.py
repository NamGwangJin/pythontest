import math
'''
around = lambda r: 2*math.pi*r
square = lambda r: math.pi*r**2
volume = lambda r: 4/3*math.pi*r**3
'''
def around(r=4):
    return 2*math.pi*r
def square(r=4):
    return math.pi*r**2
def volume(r=4):
    return 4/3*math.pi*r**3

if __name__ == '__main__':
    radius = float(input('반지름:'))
    if radius != '':
        radius = float(radius)
        print( '둘레 : ',around(radius),'m\n면적 : ',square(radius),'m2\n체적',volume(radius),'m3')
    print('둘레',around(),'m\n면적:',square(),'m2\n체적:',volume(),'m3')