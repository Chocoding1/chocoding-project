import random

def make_num(): #난수생성을 위한 함수
    list = []
    
    while len(list) < 4:
        a = random.randrange(10)
        if a != 0 and len(list) == 0: #0이아닌 첫번째 수는 무조건 추가하기 위한 코드
            list.append(a)
        elif a == 0 and len(list) == 0: #첫번째 숫자가 0인 경우를 배제하기 위한 코드
            pass
        else:
            if list.count(a) == 0: #중복된 숫자가 없을 경우에만 리스트에 추가
                list.append(a)
            else:
                pass
    
    print('난수를 생성하였습니다.')
    game_progress(list) #게임진행 함수 호출

def game_progress(list): #게임진행하는 함수
    count = 10
    while True:
        strike = 0
        ball = 0
        print("남은 기회 : {}회".format(count))
        num = input('네자리 숫자를 입력하시오(중복된 숫자 사용금지) : ')
        
        for i in range(4):
            for j in range(4):
                if list[i] == int(num[j]) and i == j:
                    strike += 1
                elif list[i] == int(num[j]) and i != j:
                    ball += 1
                else:
                    pass

        print('{}b {}s'.format(ball, strike))
        count -= 1
        if strike  == 4:
            print("맞췄습니다.")
            break
        elif count == 0:
            print("남은 기회가 모두 소진되었습니다.")
            print("정답은 ", list)
            break
    
    restart_game()

def restart_game(): #게임 재시작을 위한 함수
    choice = input("게임을 재시작하겠습니까?(y/n)")

    if choice == 'Y' or choice == 'y':
        baseball_game()
    else:
        print("게임이 종료되었습니다.")


def baseball_game():
    make_num()#난수생성 함수 호출

baseball_game()#게임시작