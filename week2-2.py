import numpy as np
import matplotlib.pyplot as plt

#2x + y = 3     y = -2x + 3
#2x - y = 1     y = 2x + 1
# x - 2y = -1   y = (x + 1) / 2

#x값 범위: -2 ~ 3 사이에 500개 생성
x = np.linspace(-2, 3, 500)

y_eq1 = -2*x + 3
y_eq2 = 2*x + 1
y_eq3 = (x + 1) / 2

#그래프 생성
plt.figure(figsize=(8, 7))

#선 그래프
plt.plot(
    x, y_eq1, label='2x + y = 3', color = 'blue', linewidth=2.5
)

plt.plot(
    x, y_eq2, label='2x - y = 1', color = "deeppink", linewidth=2.5
)

plt.plot(
    x, y_eq3, label='x - 2y = -1', color = "green", linewidth=2.5
)

solution_x = 1
solution_y = 1

#점 그래프
plt.scatter(
    solution_x, solution_y,
    color="black",
    s=70,
    zorder=5
)

#주석 표시 함수
plt.annotate(
    "(1,1)",
    xy=(solution_x, solution_y),
    xytext=(1.15, 1.2),
    fontsize=14
)

#공통해를 나타내는 선 그리기
plt.plot(
    [solution_x, solution_y],
    [0, solution_y],
    color="deeppink",
    linestyle="--",
    linewidth=1
)

plt.plot(
    [solution_x, solution_y],
    [solution_x, 0],
    color="deeppink",
    linestyle="--",
    linewidth=1
)

#x축, y축 그리기
plt.axhline(0, color="black", linewidth=1)      #가로선
plt.axvline(0, color="black", linewidth=1)      #세로선

#그래프 범위 설정
plt.xlim(-2, 3)
plt.ylim(-3,5)
plt.xlabel("x", fontsize = 14)
plt.ylabel("y", fontsize = 14, rotation=0, labelpad=15)
plt.title("Three linear Equations", fontsize = 16)
plt.grid(alpha=0.25)
plt.legend(fontsize = 12)
plt.gca().set_aspect("equal", adjustable="box")

plt.tight_layout()
plt.show()