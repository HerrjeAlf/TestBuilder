from sympy import *
# b = list(range(1,4))
# print(b)
#
# i = 0
# for m in range(1,7):
#     for n in range(1,7):
#         if m + n > 9:
#             print ('m: ' + str(m) + ' und n: ' + str(n) + ' und m+n:' + str(m+n))
#             i += 1
#
# print(i)
#
#
# a = [[1,2],[2,3]]


teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i']
liste_teilaufg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
if len([element for element in teilaufg if element in liste_teilaufg[8:11]]) > 0:
    if len([element for element in teilaufg if element in liste_teilaufg[0:7]]) > 0:
        print([element for element in teilaufg if element in liste_teilaufg[8:11]])
        print([element for element in teilaufg if element in liste_teilaufg[0:7]])