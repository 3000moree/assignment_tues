from fractions import Fraction

#행렬을 이쁘게 출력
def print_matrix(name, M):
    print(name)
    for row in M:
        print("[" + " ".join(f"{str(v):>5}" for v in row) + "]")
    print()

#주어진 행렬
A = [
    [1, 2, 1],
    [2, 3, 3],
    [-3, -10, 2]
]

n = len(A)

#U는 A의 복사본에서 시작
#Fraction을 사용해 분수를 정확히 계산
U = [[Fraction(v) for v in row] for row in A]

#L은 단위행렬에서 시작됨
L = [
    [Fraction(1 if i == j else 0) for j in range(n)]
    for i in range(n)
]

print_matrix("초기행렬 A", A)

#가우스 소거법: 피벗 아래의 원소를 0으로
for k in range(n-1):
    if U[k][k] == 0:
        raise ValueError("피벗이 0이므로 행 교환 필요")

    for i in range(k+1, n):
        #소거 배수 = 없앨 원소 / 피벗
        multiplier = U[i][k] / U[k][k]

        #소거 배수를 L에 저장
        L[i][k] = multiplier

        #R1 = R1 - multiplier x Rk
        U[i] = [
            U[i][j] - multiplier * U[k][j]
            for j in range(n)
        ]

        print(f"R{i+1} = R{i + 1} - ({multiplier}) x R{k+1}")
        print_matrix("현재 U", U)

print_matrix("푀종 하삼각행렬 L", L)
print_matrix( "최종 상삼각행렬 U",U)

#행렬 곱 LU 계산

LU = [
    [
        sum(L[i][k] * U[k][j] for k in range(n))
        for j in range(n)
    ]
    for i in range(n)
]

print_matrix("검산: L x U", LU)
print("LU = A 확인: ", LU == A)