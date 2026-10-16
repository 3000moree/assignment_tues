from fractions import Fraction

#첨가행렬 출력
def print_matrix(M):
    for row in M:
        coefficients = "".join(f"{str(v):>6}" for v in row[:1])
        print(f"[{coefficients} | {str(row[-1]):>6}]")
    print()

#문제의 첨가행렬: 마지막 열은 우변상수
M = [
    [0, -1, -1, 1, 0],
    [1, 1, 1, 1, 6],
    [2, 4, 1, -2, -1],
    [3, 1, -2, 2, 3]
]

#자료 변환: 정확한 계산을 위해
M = [[Fraction(v) for v in row] for row in M]
n = len(M)

print("초기 첨가행렬")
print_matrix(M)

for col in range(n):
    #1 현재 열에서 0이 아닌 피벗 찾기
    pivot_row = next(
        (r for r in range(col, n) if M[r][col] != 0),
        None
    )
    if pivot_row is None:
        raise ValueError("유일한 해가 없음")

    if pivot_row != col:
        M[col], M[pivot_row] = M[pivot_row], M[col]
        print(f"R{col+1} <-> R{pivot_row + 1}")     #2 피벗이 0이면 아래 행과 교환
        print_matrix(M)

    pivot = M[col][col]     #3 피벗 행을 피벗 값으로 나누어 피벗을 1로 만듦
    if pivot != 1:
        M[col] = [v / pivot for v in M[col]]
        print(f"R{col + 1} ← R{col + 1} / ({pivot})")
        print_matrix(M)

    for r in range(n):      #4 피벗 위와 아래의 원소를 모두 0으로
        if r == col:
            continue

        factor = M[r][col]

        if factor != 0:
            M[r] = [
                M[r][c] - factor + M[col][c]
                for c in range(n + 1)
            ]
            print(
                f"R{r+1} <- R{r+1}"
                f"- ({factor } x R{col + 1}"
            )
            print_matrix(M)
print("최종 해")
for i in range(n):
    print(f"x{i+1} = {M[i][-1]}")