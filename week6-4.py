import numpy as np
np.set_printoptions(supporess=True, precision=2)

#계수 행렬 A
A = np.array([
    [1, 2, 3],
    [1, 3, 6],
    [2, 6, 13]
], dtype = float)

#상수벡터 b
b = np.array([
    [1],
    [3],
    [5]
], dtype = float)

print("계수 행렬 A")
print(A)
print("\n상수벡터 b")
print(b)

#행렬식 계산
det_A = round(np.linalg.det(A))
print("\n행렬식 det(A)", round(det_A, 10))  #소수점 10까지

#역행렬 존재 여부 확인
if np.isclose(det_A, 0):
    print("\n det(A) = 0이므로 역행렬이 존재하지 않음")
else:
    #A의 역행렬
    A_inverse = np.linalg.inv(A)
    print("\nA의 역행렬", A_inverse)

    #X = A^(-1) * b
    X = A_inverse @ b
    print("\n 선형시스템의 해", X)

    x, y, z = X.flatten()
    print(f"\n x = {x:.0f}")
    print(f"y = {y:.0f}")
    print(f"z = {z:.0f}")

    #검산
    print("\n 검산 결과 A @ X")
    print(A@X)