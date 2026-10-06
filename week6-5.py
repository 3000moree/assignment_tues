#2x2 행렬의 행렬식 계산 함수
def determinant_2x2(matrix):
    return(
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )

#계수 행렬 A
A = [
    [3, -2],
    [-5, 4]
]

#상수 벡터 b
b = [6, 8]

#A1: A의 첫 번째 열을 b로 교체
A1 = [
    [b[0], A[0][1]],
    [b[1], A[1][1]]
]

#A2: 두 번째 열을 교체
A2 = [
    [A[0][0], b[0]],
    [A[1][0], b[1]]
]

#각각의 행렬식 계산
D = determinant_2x2(A)
D1 = determinant_2x2(A1)
D2 = determinant_2x2(A2)

print("계수 행렬 A = ", A)
print("A1 = ", A1)
print("A2 = ", A2)
print("\n det(A) =", D)
print("det(A1) =", D1)
print("det(A2)= ", D2)

#크래머의 규칙 적용
if D == 0:
    print("\n det(A) = 0이므로 크래머 규칙 적용 불가")
else:
    x1 = D1/D
    x2 = D2/D
    print("\n 크래머의 규칙 계산")
    print(f"x1 = det(A1)/det(A) = {x1}")
    print(f"x2 = det(A2)/det(A) = {x2}")

    #검산
    result1 = 3*x1 - 2*x2
    result2 = -5*x1 + 4 *x2
    print("\n 검산")
    print(f"3x1 - 2x2 = {result1}")
    print(f"-5x1 + 4x2 = {result2}")