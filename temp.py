b = list(range(1,4))
print(b)

i = 0
for m in range(1,7):
    for n in range(1,7):
        if m + n > 9:
            print ('m: ' + str(m) + ' und n: ' + str(n) + ' und m+n:' + str(m+n))
            i += 1

print(i)