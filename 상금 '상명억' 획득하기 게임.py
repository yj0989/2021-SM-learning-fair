# 1 번째 게임 <가위 바위 보 게임>

print("게임에 참가하신 여러분, 진심으로 환영합니다.")
print("참가자들이 참여하실 게임은 총 3가지이며 모두 통과할 경우 상금 상명억이 주어집니다.")
print("만약 각각의 게임을 실패할 경우 다음 게임으로 넘어가되 최종적으로 상금 상명억을 받을 수 없게됩니다.")
print("게임에 참가한 참가자들은 3가지 게임을 모두 이겨서 상금 상명억을 획득하길 바라겠습니다.")
print("그럼 지금부터 게임을 시작하겠습니다. 첫 번째 게임은 가위, 바위, 보 게임입니다. 지거나 비길 시 탈락입니다. 하나의 숫자를 선택해 주십시오.")
    
바위 = '''


      ****
      ****
'''

가위 = '''
    *      *
     *    *
      ***
       *
'''

보 = '''
    ********
    ********
    ********
    ********
'''

import random

game_option = [바위, 가위, 보]
컴퓨터_선택 = random.randint(0,2)

참가자_선택 = int(input(" 0: 바위, 1: 가위, 2: 보 >>> ") )

print("참가자 선택 :  ")
print(game_option[참가자_선택])

print("컴퓨터 선택 : ")
print(game_option[컴퓨터_선택])


if 컴퓨터_선택 == 참가자_선택:
    print("안타깝네요.. 참가자는 가위바위보 게임에 졌습니다.")
    print("상명억 획득은 다음 기회를 노려보세요^^")
    print("다음 게임은 부담없이 즐겨보시길 바랍니다!")

elif 참가자_선택 - 컴퓨터_선택 == -1 or (참가자_선택 ==2 and 컴퓨터_선택 ==0):
    print("이겼습니다. 상명억을 획득할 기회! 1/3 통과 입니다")
    print("첫 번째 게임을 이긴 참가자, 다음 게임도 좋은 결과 기대하겠습니다!")
else:
    print("안타깝네요.. 참가자는 가위바위보 게임에 졌습니다.")
    print("상명억 획득은 다음 기회를 노려보세요^^")
    print("다음 게임은 부담없이 즐겨보시길 바랍니다!")
    
# 2 번째 <파이썬 용어 퀴즈 게임>
print()
print()
print("두 번째 게임은 파이썬 용어 퀴즈 입니다! 서로 다른 문제 5문제 이상 맞출 시 성공이며 상명억 획득의 기회가 주어집니다.")
print("서로 다른 5문제를 모두 맞췄을 경우 종료 버튼인 숫자 0을 선택하시면 다음 게임으로 넘어갈 수 있습니다.")
print("주의할 부분은 같은 문제가 또 나와서 또 풀어도 1문제로만 인정 됩니다! 이 점 유의해주시길 바랍니다.")
print("그리고 만약 문제의 답을 틀렸을 시 종료 버튼 숫자 0을 선택하시고 게임을 끝내시면 됩니다. 이번 게임에 실패할 경우 다음 게임으로 넘어가되 상명억 획득의 기회는 사라집니다.")
print("자, 지금부터 문제를 읽고 답을 선택하시면 됩니다.")
print()
import random

eng_word = [["for문", "반복문-for"], ["while문", "반복문-while"],
            ["print()", "모니터에 텍스트를 출력해주는 함수"], ["str", "문자열"],
            ["Recursive call", "재귀 호출"], ["break", "반복문을 탈출"],
            ["input()", "키보드로부터 입력을 받고자 할 때 사용하는 함수"], ["append", "리스트 제일 뒤에 항목을 추가한다"],
            ["insert()", "지정된 위치에 값을 삽입한다"], ["len()", "리스트에 포함된 전체 항목의 개수를 센다"],
            ["Dictionary", "사전"], [ "argument", "인수"]
            ]

quiz_on = True
score = 0
quiz_num = 0

while quiz_on:
    #4지선다 보기 항목
    quiz_num += 1
    multi_choice = random.sample(eng_word, 4)
    answer_index = random.randint(0, 3) #0, 1, 2, 3

    print(f"문제{quiz_num}번. {multi_choice[answer_index][0]}의 뜻은?")
    #보기 출력
    for i in range(4):
        print(f"{i+1}. {multi_choice[i][1]}")

    print()
    user_input = int(input("정답을 입력해 주세요. 종료: 0 >>>>   "))

    if user_input == 0:
        quiz_on = False
        print("파이썬 퀴즈가 종료되었습니다.")
        print(f"총 {quiz_num-1}문제 중 {score}문제를 맞혔습니다.")
        print("모두 맞춘 참가자, 정말 대단합니다. 상명억 획득 기회 2/3 통과입니다. 다음 마지막 게임 행운을 빕니다!")
        print()
        print("아쉽습니다..5문제 이상 답을 못 맞춘 참가자, 다음 게임만 통과하면 상금 상명억 획득이었는데..")
        print("비록 상명억 획득의 기회는 날아갔지만 다음 게임에 함께 참가해보시죠!")
    elif user_input ==  answer_index + 1:
        score += 1
        print("정답입니다.")
    else:
        print(f"오답입니다. 정답은 {answer_index + 1}번 입니다.")
    print()
    
# 3 번째 게임 <로드 게임>
print()
print()
road = '''

            A     A             B       B       C      C
             A  1  A           B   2   B      C   3   C
              A     A         B       B      C      C
               A     A       B       B      C     C
                A     A      B     B      C      C
                 A     A    B     B      C      C
                  A     A  B       B   C     C
                   A     A B      B   C    C
                    A    A B      B C     C
                     A   A B      BC     C
                      A   A       B    C

'''
import random
print("두 번째 게임까지 통과하신 여러분 진심으로 축하합니다.")
print("마지막 세 번째 게임은 길 탈출하기 게임입니다.")
print("마지막 게임인 만큼 이번 게임에 통과할 경우 참가자님이 배팅하신 금액의 2배를 상금으로 받으실 수 있습니다.")
print("단 게임에 실패하실 경우 상명억뿐만 아니라 참가자님이 배팅하신 금액은 받을 수 없습니다.")
print("3 번째 게임도 통과하신 분들은 배팅하신 금액의 2배의 상금과 상금 상명억이 주어집니다.")
print("부디 좋은 결과 있으시길 바랍니다. 바로 게임을 시작합니다.")
print()

bet = int(input("배팅 금액을 입력하세요. 단위 $ >>> "))
print(f"총 ${bet} 배팅하셨습니다.")

print(road)
winning_num = random.randint(1,3)
print(winning_num)
user_choice = int(input("3갈래의 길로 나뉘어 있습니다. 어느 길을 선택하시겠습니까? 1,2,3 >>>"))

if user_choice == winning_num:
    print(f"축하합니다! 2배 획득!! 총 금액은 ${bet *2}가 되었습니다. 모든 게임을 통과하시고 상명억을 획득한 참가자 대단합니다! 짝짝짝")
else:
    print("모든 배팅 금액을 잃었습니다. 3 번째 게임에서 탈락하신 참가자 안타깝지만 다음 게임에 다시 도전해주세요.")

print("상명억 획득 게임 끝!!")
