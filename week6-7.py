import math
#2x2 행렬식 계산 함수
def determinant_2x2(matrix):
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )

#각도를 라디안으로
angle25 = math.radians(25)
angle15 = math.radians(15)

#계수 행렬 A
A = [
    [math.cos(angle25), -math.cos(angle15)],
    [math.sin(angle25), math.sin(angle15)]
]
#상수벡터 b
b = [0, 30]

#A1: 첫 번째 열을 b로 교체
A1 = [
    [b[0], A[0][1]],
    [b[1], A[1][1]]
]


#A2: 두 번째 열을 b로 교체
A2 = [
    [A[0][0], b[0]],
    [A[1][0], b[1]]
]

#행렬식 계산
D = determinant_2x2(A)
D1 = determinant_2x2(A1)
D2 = determinant_2x2(A2)

print("계수 행렬 A")
for row in A:
    print(row)
print("\nA1: 첫 번째 열을 b로 교체")
for row in A1:
    print(row)
print("\nA2: 두 번째 열을 b로")
for row in A2:
    print(row)

print(f"\nD = det(A)= {D:.6f}")
print(f"D1 = det(A1) = {D1:.6f}")
print(f"D2 = det(A2) = {D2:.6f}")

#크래머의 규칙
if math.isclose(D, 0.0, abs_tol=1e-12):
    print("det(A)=0이므로 유일한 해가 없습니다")

else:
    T1 = D1 / D
    T2 = D2/ D
    print("그래머 규칙 계산")

    print("T1 = D1 / D = {T1:.6f}")
    print(f"T2 = D2 / D = {T2:.6f}")

    #검산
    equation1 = (
        math.cos(angle25)*T1 - math.cos(angle15)*T2
    )
    equation2 = (
        math.sin(angle25)*T1 + math.sin(angle15)*T2
    )
    print("\n 검산")
    print(f"수평 방향 힘 = {equation1:.6f}")
    print(f"수직 방향 힘 = {equation2:.6f}")