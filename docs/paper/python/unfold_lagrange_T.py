import sympy
from sympy import symbols, cos, sin, diff, Rational, latex, factor, expand

x = symbols("x_1 x_2 x_3 x_4 x_5 x_6")
y = symbols("y_1 y_2 y_3 y_4 y_5 y_6")
l = symbols("l_1 l_2 l_3 l_4 l_5 l_6")
t = symbols("\\theta_1 \\theta_2 \\theta_3 \\theta_4 \\theta_5 \\theta_6")
dt = symbols("\\dot{\\theta_1} \\dot{\\theta_2} \\dot{\\theta_3} \\dot{\\theta_4} \\dot{\\theta_5} \\dot{\\theta_6}")
m = symbols("m_1 m_2 m_3 m_4 m_5 m_6")

a = [l[i] * cos(t[i]) for i, _ in enumerate(x)]
b = [l[i] * sin(t[i]) for i, _ in enumerate(x)]

da = [-l[i] * dt[i] * sin(t[i]) for i, _ in enumerate(x)]
db = [ l[i] * dt[i] * cos(t[i]) for i, _ in enumerate(x)]

dx = [
    da[0] + da[1] + da[2] + da[3],
    da[1] + da[2] + da[3],
    da[2] + da[3],
    da[3],
    da[4] + da[3],
    da[5] + da[4] + da[3]
]

dy = [
    db[0] + db[1] + db[2] + db[3],
    db[1] + db[2] + db[3],
    db[2] + db[3],
    db[3],
    db[4] + db[3],
    db[5] + db[4] + db[3]
]

T = [m[i] * (dx[i] ** 2 + dy[i] ** 2) for i, _ in enumerate(x)]
for temp in T:
    print(latex(expand(temp)))
    print()

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
