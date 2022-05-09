"""문제
김지민은 N명이 참가하는 스타 토너먼트에 진출했다. 토너먼트는 다음과 같이 진행된다. 일단 N명의 참가자는 번호가 1번부터 N번까지 배정받는다. 그러고 난 후에 서로 인접한 번호끼리 스타를 한다. 이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서 떨어진다. 만약 그 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출한다. 다음 라운드에선 다시 참가자의 번호를 1번부터 매긴다. 이때, 번호를 매기는 순서는 처음 번호의 순서를 유지하면서 1번부터 매긴다. 이 말은 1번과 2번이 스타를 해서 1번이 진출하고, 3번과 4번이 스타를 해서 4번이 진출했다면, 4번은 다음 라운드에서 번호 2번을 배정받는다. 번호를 다시 배정받은 후에 한 명만 남을 때까지 라운드를 계속 한다.

마침 이 스타 대회에 임한수도 참가했다. 김지민은 갑자기 스타 대회에서 우승하는 욕심은 없어지고, 몇 라운드에서 임한수와 대결하는지 궁금해졌다. 일단 김지민과 임한수는 서로 대결하기 전까지 항상 이긴다고 가정한다. 1 라운드에서 김지민의 번호와 임한수의 번호가 주어질 때, 과연 김지민과 임한수가 몇 라운드에서 대결하는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다. N은 2보다 크거나 같고, 100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.

출력
첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다."""

n, KJM, IHS = map(int, input().split())

# 라운드 수
rnd = 1
# 선수 수만큼 0으로 초기화 한다
l = [0]*n
# 김지민, 임한수는 1로 표시한다
l[KJM-1] = 1
l[IHS-1] = 1

# 맡붙으면 False
r = True

while(r):
    # 김지민, 임한수가 나오면 그뒤로 나오는 대진표는 무시하기 위해 1의 갯수를 센다
    cnt = 0

    # 2명 이하로 남았으면 -1로 넣고 나간다
    if len(l) < 2:
        rnd = -1
        break

    # 승자만 넣을 새로운 리스트
    newL = []

    # 0, 2, 4, 6 ...
    for i in range(0, len(l), 2):

        # 이미 김지민, 임한수가 나왔으면 나머지 선수대진은 무시한다
        if cnt >= 2:
            break

        # 마지막 사람 홀수
        if i+1 == len(l):
            newL.append(l[i])
            cnt += l[i]
        # 인접 체크 하고 맞붙었으면 나간다
        elif l[i] == 1 and l[i+1] == 1:            
            r = False            
            break
        # 김지민 이나 임한수 둘 중 하나이면 1은 넣는다
        elif l[i] == 1 or l[i+1] == 1:
            newL.append(1)
            cnt += 1
        # 둘 다 아닌 다른 선수들
        else:
            newL.append(0)
        
    if r == True:
        # 맞붙지 않았으면 기존 대진표를 갱신, 라운도 횟수 1 추가        
        l = newL
        rnd += 1

print(rnd)