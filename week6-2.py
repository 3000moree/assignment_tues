#첨가행렬로 역행렬 구하기
import numpy as np
np.set_printoptions(suppress=True, precision=2)

#행렬 A
A = np.array([
    [1, -1, 4],
    [2, -5, 7],
    [0, 1, 1]
], dtype=float)

#단위행렬 I
I = np.eye(3)

#첨가행렬 [A|I]
AI = np.hstack((A,I))

def show_matrix(title):
    print(f"\n{title}")

    for row in AI:
        left = "".join(f"{value:6.1f}" for value in row[:3])
        right = "".join(f"{value:6.1f}" for value in row[3:])
        print(f"[{left} | {right}]")

#초기 첨가행렬
show_matrix("초기 첨가행렬 [A|I]")

#1단계: R2 = (-2)R1 + R2
AI[1] = -2*AI[0] + AI[1]
show_matrix("R2 = (-2)R1 + R2")

#2단계: R3 = R2 + R3
AI[2] = AI[1] + AI[2]
show_matrix("R3 = R2 + R3")

#3단계ㅣ R1 = 3R2 + R1
AI[0] = 3*AI[1] + AI[0]
show_matrix("R1 = 3R2 + R1")

#왼쪽 A부분과 오른쪽 부분 분리
left_matrix = AI[:, :3]
right_matrix = AI[:, 3:]

print('\n행 연산 후 왼족 행렬')
print(left_matrix)
print("\n행 연산 후 오른쪽 행렬")
print(right_matrix)

#역행렬 존재 여부 확인
if np.linalg.matrix_rank(A) < A.shape[0]:   #행 개수가 피벗 개수보다 많다면
    print("\n A의 행들이 선형종속입니다.\n왼쪽 행렬에 모든 원소가 0인 행이 발생했습니다.\n따라서 A를 단위행렬로 만들 수 없습니다.")
    print("행렬 A의 역행렬은 존재하지 않음")
else:
    A_inverse = right_matrix
    print("\nA의 역행렬")
    print(A_inverse)

det_A = np.linalg.det(A)
print("det(A) =", round(det_A))