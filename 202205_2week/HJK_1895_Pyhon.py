"""문제
숫자 9개가 오름차순이나 내림차순으로 정렬되어 있을 때, 중앙값은 다섯 번째 숫자이다. 예를 들어, 1, 3, 4, 1, 2, 6, 8, 4, 10의 중앙값은 4이다. (1 ≤ 1 ≤ 2 ≤ 3 ≤ 4 ≤ 4 ≤ 6 ≤ 8 ≤ 10)

이미지 I는 크기가 R × C인 2차원 픽셀이다. (3 ≤ R ≤ 40, 3 ≤ C ≤ 40) 각 픽셀은 어두운 정도 V를 나타낸다. (0 ≤ V ≤ 255)

중앙 필터는 이미지에 있는 노이즈를 제거하는 필터이다. 필터의 크기는 3 × 3이고, 이미지의 중앙값을 찾으면서 잡음을 제거한다.

예를 들어, 아래와 같은 6 × 5 이미지가 있다.

필터링된 이미지의 크기는 4 × 3이고, 아래와 같다.

가장 왼쪽 윗 행에 필터를 두고, 오른쪽으로 움직이면서 중앙값을 찾는다. 한 행을 모두 이동했으면, 다음 행으로 이동해 다시 중앙값을 찾는다. 아래와 같은 순서를 가진다.

위의 그림에서 각각의 중앙값은 36, 36, 21이 된다. 이 값은 필터링된 이미지 J의 첫 행과 같다. 

이미지 I가 주어졌을 때, 필터링 된 이미지 J를 구하고, 값이 T보다 크거나 같은 픽셀의 수를 구하는 프로그램을 작성하시오.

예를 들어, T = 40일 때, 위의 예에서 정답은 7이다. 

입력
첫째 줄에 이미지의 크기 R과 C가 주어진다. 그 다음 R개의 각 줄에는 C개의 픽셀 값이 주어진다. 마지막 줄에는 T값이 주어진다.
6 5
49 36 73 62 21
27 88 14 11 12
99 18 36 91 21
45 96 72 12 10
12 48 49 75 56
12 15 48 86 78
40

출력
첫째 줄에 필터링 된 이미지 J의 각 픽셀 값 중에서 T보다 크거나 같은 것의 개수를 출력한다.
7

"""

# 입력부
r, c = map(int, input().split())
l1 = []

for i in range(r):
    l1.append(list(map(int, input().split())))

t = int(input())

cnt = 0 # t 보다 크거나 같은 갯수 저장
l2 = [] # 최종 필터 결과 저장

# 항상 9개의 숫자만 들어오므로 최소한의 연산만 하도록 작성
def median(l):    
    l.sort()
    return l[4]

for i in range(r-2): # 시작 행 번호
    for j in range(c-2): # 시작 열 번호

        l3 = [] # 중앙값 계산 위한 9개의 숫자 저장

        for ii in range(3):
            for jj in range(3):
                l3.append(l1[i+ii][j+jj]) # 3 x 3 필터 저장

        l2.append(median(l3)) # 9개 픽셀의 중앙값 저장

for i in map(int, l2):
    if i >= t:
        cnt += 1

print(cnt)