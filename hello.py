'''
a=1.23
print(a)
print(type(a))
print(a,type(a))
b=type(a)
print(b,'\n')

c=str(b)
print(type(c))
print(c[3],'\n')

d='0123456789cho'
print(type(d))
print(d[0:4])
print(d[:6])
print(d[6:])
print(d[::2])
print(d[::-1],'\n')

print("안녕\n내이름을 소개하지\n내이름은 김하온")
print("""안녕
내이름을 소개하지
내이름은 김하온""")

#name=input('이름을 입력하세요>')
#print('너의 이름은',name)
#print(type(name))

aa=input('문자열입력>')
bb=input('문자열입력>')

print(aa,bb)
cc=aa
aa=bb
bb=cc
print(aa,bb)

#여러가지 출력방법
a="{} {}".format(11,22)
print(a)
a="{:10.3f}".format(52)
print(a)
a='%0.3f'%52
print(a)
a='I eat {} apples.'.format(3)
print(a)
a='I eat %d apples.'%3
print(a)
print('I eat',3,'apples')

name='int'
a=f'my name is {name}'
print(a)

a='hobby'
print(a.count('b'))#해당글자 개수 출력
print(a.find('y'))#해당글자가 있는 index 출력

a='My name is %s'%'seong jin'
print(a.upper())
print(a)

print('10'.isdigit())
print('aadg'.isalpha())

a=10==1000
print(a)

tic=input('예매할 티켓수 입력 :')

if int(tic)>1:
    print('티켓은 1장만 예약 가능합니다.')
else:
    time=input('시간을 입력하세요 : ')
    if int(time)>13:
        print('티켓이 예매되었습니다.')
    else:
        print('13시 이후에만 티켓예매가 가능합니다.')


pay=input('결제카드를 입력하세요:')

if pay=='우리' or pay=='신한':
    print('결제가 완료되었습니다.')
else:
    print('결제는 우리 또는 신한으로만 가능합니다.')


import datetime

now=datetime.datetime.now()
hour=now.hour
print(hour,'시')
print(type(hour))

if hour>=12:
    print('현재시각은 %d시로 오후입니다.'%hour)
else:
    print('오전입니다.')

a=[1,2,3]
a.append([4,5])
print(a)
a=[1,2,3]
a.extend([4,5,])
print(a)

num=[273,103,5,32,65,9,72,800,99]

for number in num:
    if number>100:
        print('- 100 이상의 수:',number)

num=[273,103,5,32,65,9,72,800,99]

for i in num:
    if i%2==0:
        print('%d는 짝수입니다.'%i)
    else:
        print('%d는 홀수입니다.'%i)

num=[273,103,5,32,65,9,72,800,99]

for i in num:
    print('%d는 %d자리수입니다.'%(i, len(str(i))))

list_of_list=[
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for i in list_of_list:
    for j in i:
        print(j)

num=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for i in num:
    output[i%3-1].append(i)

print(output)

pets=[
    {"name":'구름', "age":5},
    {"name":'초코', "age":3},
    {"name":'아지', "age":1},
    {"name":'호랑이', "age":1}
]

print("#우리 동네 애완 동물들")
for i in pets:
    print("%s %d살"%(i["name"],i["age"]))

num=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter={}

for i in num:
    counter[i]=0
for i in num:
    counter[i]+=1

print(counter)

character={
    "name": '기사',
    "level":12,
    "items":{
        "sword":'불꽃의 검',
        "armor":'풀플레이트',
    },
    "skill":['베기','세게 베기','아주 세게 베기']
}

for key in character:
    #print(key)
    #print(type(key))
    #print(type(character[key]))
    if type(character[key]) is str:
        print("%s : %s"%(key, character[key]))
    elif type(character[key]) is list:
        #print(character[key])
        for i in character[key]:
            print("%s : %s"%(key, i))
    elif type(character[key]) is dict:
        for i in character[key]:
            #print(character[key])
            #print(i,':', character[key][i])
            print("%s : %s"%(i,character[key][i]))
    else:
        print("%s : %d"%(key, character[key]))

for i in range(5):
    print(str(i)+'=반복변수')

for i in range(5,-3,-1):
    print(i)

for i in reversed(range(5)):
    print(i)

while True:
    print(".",end="\t")

import time

print(time.time())

key_list=["name","hp","mp","level"]
value=["기사",200,30,5]
character={}

for i in range(len(key_list)):
    character[key_list[i]]=value[i]
print(character)

limit=10
i=1
sum=0

while sum<=limit:
    sum+=i
    i+=1

print("%d를 더할 때 %d를 넘으며 그때의 값은 %d입니다."%(i-1,limit,sum))

max_value=0
a=0
b=0

for i in range(1,50+1):
    j=100-i

    sample=i*j

    if sample>max_value:
        max_value=sample
        a=i
        b=j

print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))

list_a=[1,2,3,4,5]
list_reversed=reversed(list_a)

print(list(list_reversed))
print(list_reversed)
print(reversed(list_a))

num=int(input('정수입력:'))

if num%2==0:
    print(
    '입력한 문자열은 {}입니다.\n'
    '{}는 짝수입니다.'.format(num,num))

output=[num for num in range(1,100+1)
    if "{:b}".format(num).count('0')==1]

for i in output:
    print("%d : %s"%(i,"{:b}".format(i)))
print("합계 :",sum(output))

a={1:'a',2:'b',3:'c'}

print(a.keys())
print(a.values())
print(a.items())

for i in a.keys():
    print(i)

s1=set([1,2,3])
#s1={1,2,3}
print(s1)

a=[1,2,3,4]

while a:
    print(a)
    del a[-1]

a=[1,2,3]
b=a
print(id(b))
a[1]=4
print(id(a))
print(id(b))
print(b is a)

a=[1,2,3]
b=a[:]
print(id(b))
a[1]=4
print(id(a))
print(id(b))
print(b is a)

a=3
b=4

a,b=b,a
print(a,b)

def print_3_times():
    for i in range(3):
        print('안녕하세요')

print_3_times()

def f(x):
    return 2*x+1
print(f(10))
def f(x):
    return x**2+2*x+1
print(f(10))

def mul(*values):
    gop=1
    for i in values:
        gop*=i
    return gop
print(mul(5,7,9,10))

def factorial(n):
    output=1
    print(list(reversed(range(n))))
    for i in reversed(range(1,n+1)):
        print(i)
        output*=i
    return output
print(factorial(3))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

def fibonacci(n):
    print('fibonacci(%d)를 구합니다.'%n)
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

dict={1:1,2:2}

def fibonacci(n):
    if n in dict:
        return dict[n]
    else:
        output=fibonacci(n-1)+fibonacci(n-2)
        dict[n]=output
        return output

print(fibonacci(5))

output=[]
def flatten(data):
    global output
    for i in data:
        if type(i)==int:
            output.append(i)
        elif type(i)==list:
            flatten(i)
    return output

example=[[1,2,3],[4,[5,6]],7,[8,9]]
#example=[[1,2,3],4,5,6,7,8,9]
print("원본:",example)
print("변환:",flatten(example))

seat_min=2
seat_max=10
tot=100
memo={}

def quest(rest,seat):
    key=str([rest,seat])

    if key in memo:
        pass
    if rest<0:
        pass
    if rest==0:
        pass

print(quest(100,2))

[a,b]=[1,2]
print(a,b)
a,b=b,a
print(a,b)
print(type([a,b]))

def func():
    print('출력a')
    yield 100

print(next(func()))

num=[1,2,3,4,5,6]

#print("::".join(str(i) for i in num))
print("::".join(map(str,num)))

num=list(range(1,10+1))

print("#홀수만 추출")
print(list(filter(lambda x:x%2==1,num)))
print()

print("#짝수만 추출")
print(list(filter(lambda x:x%2==0, num)))
print()

print("#3이상 7미만 추출")
print(list(filter(lambda x:x>=3 & x<7, num)))
print()

print("#제곱해서 50미만 추출")
print(list(filter(lambda x:x**2<50,num)))

def test():
    print("1")
    try:
        print("2")
        return
        print("3")
    except:
        print('4')
    else:
        print('5')
    finally:
        print("6")
    print("7")
test()

num=[52,1,2,3,4,5]

print("%d는 %d 위치에 있습니다."%(52,num.index(52)))
print()

number=10000
if number in num:
    print("%d는 %d 위치에 있습니다."%(52,num.index(52)))
try:
    print("%d는 %d 위치에 있습니다."%(number,num.index(number)))
except:
    print("리스트 내부에 없는 값입니다.")
print()

print("정상적으로 종료되었습니다.")

print([1,2,3,4,5][3])

import random

a=[1,2,3,4]
print(random.shuffle(a))
print(a)

import datetime

now=datetime.datetime.now()

a=now.strftime("%Y %m %d %H %M %S")
print(a)

from urllib import request

a=request.urlopen("http://google.com")
b=a.read()

print(b)

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
soup = BeautifulSoup(target, "html.parser")

print(soup.select("data"))

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()

import sys

print(sys.argv)

import time

print("A")
time.sleep(5)
print("B")

from urllib import request

target = request.urlopen("http://hanbit.co.kr")
content = target.read()

print(content[:100])

import os

output = os.listdir(".")
print("os.listdir():",output)
print()

print("#폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:",path)
    else:
        print("파일:",path)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_w():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route("/")

def hello():
    target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

    soup = BeautifulSoup(target, "html.parser")

    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string)
        output += "<hr/>"
    return output

if __name__ == '__main__':
    app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_hello():
    return 'Hello, SJ!'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

class Student:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    def get_sum(self):
        return self.korean+self.math+self.english+self.science

    def get_avg(self):
        return self.get_sum()/4

    def print_stu(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())

students=[
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90)]

for student in students:
    print(student.print_stu())

import math

class Circle():
    def __init__(self,radius):
        self.__radius=radius
    def get_circumference(self):
        return 2*math.pi*self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)

circle=Circle(10)
circle.radius=5
print("원의 둘레:",circle.get_circumference())
print("원의 넓이:",circle.get_area())

def GuGu(value):
    li=[]
    for i in range(9):
        li.append(value)
        value += 2
    return li

num = int(input('숫자를 입력하시오 : '))
print(GuGu(num))

sum = 0
num = int(input('어디까지 계산할까요 : '))

#for i in range(1,num):
#    if i % 3 == 0:
#        sum += i
#    elif i % 5 == 0:
#        sum += i
for i in range(1,num):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

def GetTotalPage(m, n):
    page = 0
    page += int(m / n)

    if m % n != 0:
        page += 1
    
    return page

m = int(input('게시물 총 건수 : '))
n = int(input('페이지당 보여줄 게시물 수 : '))

print('총 페이지 수 : ',GetTotalPage(m,n))
'''