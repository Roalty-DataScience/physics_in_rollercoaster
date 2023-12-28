import numpy as np
import matplotlib.pyplot as plt

# 원을 지나기 위한 조건: V^2 = 4 * r * g
r = 3.81  # 반지름
g = 9.81  # 중력 가속도
VV = (5 * r * g)  # V**2 계산

# 변수 범위 정의: 0에서 360도의 각도를 angle로 정의
angle = np.linspace(0, 359, 360)

# G와 angle의 관계 계산
G_values = ((VV / (r*g)) + (3 * np.cos(np.radians(angle)))) - 2

# 그래프 시각화
plt.figure(figsize=(10, 4))
plt.plot(angle, G_values)
plt.title('G-angle graph by 10116')
plt.xlabel('angle')
plt.ylabel('G')
plt.grid(True)
plt.show()
