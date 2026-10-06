#행렬의 합
def add_square_matrices(A, B):
  """같은 크기의 두 정방행렬을 더해서 새로운 행렬 반환"""

  n = len(A)
  
  #두 행렬의 행 개수 확인
  if n == 0 or len(B) != n:
    raise ValueError("두 행렬은 비어있지 않고 크기가 같아야 합니다")

  #각 행의 원소 개수가 n개인지 확인: n*n 정방행렬 검사
  if any(len(row) != n for row in A):
    raise ValueError("A는 정벙행렬이어야 함")

  if any(len(row) != n for row in B):
    raise ValueError("B는 A와 같은 크기의 정방행렬이어야 함")

  #결과를 저장할 n*n 행렬을 0으로 초기화
  C = [[0 for _ in range(n)] for _ in range(n)]

  #같은 위치의 원소끼리 덧셈
  for i in range(n):    #행 인덱스
    for j in range(n):  #열 인덱스
      C[i][j] = A[i][j] + B[i][j]

  return C

#두 정방행렬 정의
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]

]

#행렬 덧셈
C = add_square_matrices(A, B)

#결과 출력
print("A + B =")
for row in C:
  print(row)