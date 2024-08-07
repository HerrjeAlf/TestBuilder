import random

from sympy import *
from skripte.funktionen import *

a, b, c, d, e, f, g, h, x, y, z = symbols('a b c d e f g h x y z')

# b = list(range(1,4))
# print(b)
#
# i = 0
# for m in range(1,7):
#     for n in range(1,7):
#         if m + n > 9:
#             print ('m: ' + str(m) + ' und n: ' + str(n) + ' und m+n:' + str(m+n))
#             i += 1
# print(i)
# a = [[1,2],[2,3]]


# teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i']
# liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# if len([element for element in teilaufg if element in liste_teilaufg[8:11]]) > 0:
#     if len([element for element in teilaufg if element in liste_teilaufg[0:7]]) > 0:
#         print([element for element in teilaufg if element in liste_teilaufg[8:11]])
#         print([element for element in teilaufg if element in liste_teilaufg[0:7]])

# print('seite_' + str(i for i in range(1,2)))

# wert = 123.3
# wert_neu = str(wert).replace('.', ',')

xwert_extrema1 = -1 * nzahl(1, 4)
ywert_extrema1 = zzahl(1,10)
abstand = nzahl(1, 3)
xwert_extrema2 = xwert_extrema1 + abstand * 2
xwert_wendepkt = xwert_extrema1 + abstand
nst = xwert_extrema1 + random.randint(1, abstand*2-1)
print(xwert_extrema1)
print(nst)
print(xwert_extrema2)
glsystem = Matrix(((nst**3, nst**2, nst, 1, 0),
                 (xwert_extrema1**3, xwert_extrema1**2, xwert_extrema1, 1, ywert_extrema1),
                 (3*xwert_extrema1**2, 2*xwert_extrema1, 1, 0, 0),
                 (3*xwert_extrema2**2, 2*xwert_extrema2, 1, 0, 0)))
lsg = solve_linear_system(glsystem, a, b, c, d)
lsg_gzahl = vektor_kürzen((lsg[a],lsg[b],lsg[c],lsg[d]))
print(lsg_gzahl)
faktor = zzahl(3,7)/2
fkt = faktor*(lsg_gzahl[0]*x**3 + lsg_gzahl[1]*x**2 + lsg_gzahl[2]*x + lsg_gzahl[3])
fkt_partial = collect(simplify(fkt/(x-nst)),x)
print(fkt_partial)
fkt_partial_pq = collect(simplify((lsg_gzahl[0]*x ** 3 + lsg_gzahl[1] * x ** 2 + lsg_gzahl[2] * x + lsg_gzahl[3]) / (x - nst)), x)
print(fkt_partial_pq)
lsg_nst = solve(fkt,x)
lsg_nst.sort()
print(lsg_nst)
print(-1*(lsg_nst[0] + lsg_nst[2]))
print(lsg_nst[0]*lsg_nst[2])
print(fkt)
plot(fkt, (x, int(lsg_nst[0])-1, int(lsg_nst[-1])+1))

