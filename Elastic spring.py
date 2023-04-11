# Написал студент группы ЭВТ-20-1б  
# Новиков Денис Владиславович 
import numpy as np
from numpy import cos
from numpy import pi as π
import matplotlib.pyplot as plt

'''
Имеется груз, подвешанный на упругой пружине.
на него действует сила тяжести и сила упругости.
В начальный момент времени тело покоиться.
Используя numpy описать повидение системы до, после и в момент нарушения равновесия.
Считать, что пружина абсолютно упругая, сопротивление воздуха не учитовать.
'''

xm = 1 #Амплитуда
g = 9.81  #Ускарение свободного подения, м/с
m = 0.5  #Масса материальной точки, кг
k = 0.9751 #Коэффициент упругости пружины
φ0 = 0  #Начальная Фаза
t_distroy = 3.5  #Момент времени нарушения равновесия
x0 = m*g/k   #Точка пакоя
ω = (k/m)**0.5   #Круговая частота

fx = lambda t, A = xm, w0 =ω, fi0 = φ0: A * cos(w0*t + fi0)

start_time = 0
end_time = 10
dt = 0.001
time = list(np.arange(start_time, end_time, dt))
mas_x = []
for t in time:
    if t < (start_time + t_distroy):
        mas_x.append(x0)
    else:
        mas_x.append(x0 + fx(t))

fg, ax = plt.subplots(figsize=(7.5, 3.5), layout='constrained')
ax.plot(time, mas_x, label=f'x')
ax.set_xlabel('Время, с')
ax.set_ylabel('X, м')
ax.set_title("График горманических колебаний пружиного маятника")
ax.grid()

plt.show()
