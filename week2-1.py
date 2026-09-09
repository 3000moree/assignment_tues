import numpy as np

#2x + y = 3
#2x - y = 1
# x - 2y = -1


A = np.array([
    [2, 1],
    [2, -1],
    [1, -2]
], dtype=float)

b = np.array([3, 1, -1], dtype=float)

solution, residuals, rank, singular_values = np.linalg.lstsq(
    A, b, rcond=None
)

x, y = solution

print(f"x = {x:.6f}")
print(f"y = {y:.6f}")

print("A @ solution =", A @ solution)
print("b = ", b)

if np.allclose(A @ solution, b):
    print("공통해가 존재합니다.")
    print(f"공통해: ({x:.0f}, {y:.0f})")
else:
    print("세 방정식을 동시에 만족하는 정확한 공통해가 없습니다.")
    