"""1단원 : 파이썬 시본 함수
2단원 : 변수와 자료형
3단원 기본 입출력 

#67p 4qjs: 수핫ㄹ ㅕ행 어디로?
#1. 원하는 장소 입력받는데 동일한 입력은 무시
#1. 학생을 3명으로 가정

장소1 = input("희망하는 수학여행지를 입력하세요")
장소2 = input("희망하는 수학여행지를 입력하세요")
장소3 = input("희망하는 수학여행지를 입력하세요")

#장소들 = set([장소1, 장소2, 장소3])
장소들 = [장소1, 장소2, 장소3]
print('조사된 수학여행지는 {}입니다.'.format(set(장소들)))

#66p 2번:
Last_day_list = [31, 28,31,30,31,30,31,31,30,31,30,31]
                # 1 2   3   4  5 6   7  8  9 10 11 12

달 = input("1~12사이의 월을 입력하세요 >>>")

print("{}월은 {}일까지 있습니다.".format(달,Last_day_list[달-1]))
#1 ~100까지의 합을 구하는 프로그램
List_var = [1,2,3,4,5]

for i in range(0,101):
    if i % 10:
        print(i)
        
#1111111111111111111111111111111111111111111111111111111111111111111111
과일의수 = input("몇개의 과일을 보관할까요? >>>")

for idx in range(int(과일의수)):
    입력 = input("{}번쩨 과일을 입력하세요:".format(idx+1))
"""

 from turtle import *
 width(1)
    for x in range(1,200,5):
     forward(x)
     left(90)