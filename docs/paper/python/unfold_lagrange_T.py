import sympy
from sympy import symbols, cos, sin, diff

x = symbols("x_1 x_2 x_3 x_4 x_5 x_6")
y = symbols("y_1 y_2 y_3 y_4 y_5 y_6")
l = symbols("l_1 l_2 l_3 l_4 l_5 l_6")
t = symbols("t_1 t_2 t_3 t_4 t_5 t_6")
m = symbols("m_1 m_2 m_3 m_4 m_5 m_6")

a = [l[i] * cos(t[i]) for i, _ in enumerate(x)]
b = [l[i] * sin(t[i]) for i, _ in enumerate(x)]

da = [-l[i] * t[i] * sin(t[i]) for i, _ in enumerate(x)]
db = [l[i] * t[i] * cos(t[i]) for i, _ in enumerate(x)]

x = [
    a[0] + a[1] + a[2] + a[3],
    a[1] + a[2] + a[3],
    a[2] + a[3],
    a[3],
    a[4] + a[3],
    a[5] + a[4] + a[3]
]

y = [
    b[0] + b[1] + b[2] + b[3],
    b[1] + b[2] + b[3],
    b[2] + b[3],
    b[3],
    b[4] + b[3],
    b[5] + b[4] + b[3]
]



#
#x1 = l1 * cos(t1) + l2 * cos(t2) + l3 * cos(t3) + l4 * cos(t4)
#x2 = l2 * cos(t2) + l3 * cos(t3) + l4 * cos(t4)
#x3 = l3 * cos(t3) + l4 * cos(t4)
#x4 = l4 * cos(t4)
#x5 = l5 * cos(t5) + l4 * cos(t4)
#x6 = l6 * cos(t6) + l5 * cos(t5) + l4 * cos(t4)
#
#y1 = l1 * sin(t1) + l2 * sin(t2) + l3 * sin(t3) + l4 * sin(t4)
#y2 = l2 * sin(t2) + l3 * sin(t3) + l4 * sin(t4)
#y3 = l3 * sin(t3) + l4 * sin(t4)
#y4 = l4 * sin(t4)
#y5 = l5 * sin(t5) + l4 * sin(t4)
#y6 = l6 * sin(t6) + l5 * sin(t5) + l4 * sin(t4)
#
