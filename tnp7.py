from numpyPlus import *

print("Mass am is \n", am)
print("----")

for p in am:
    print(p)

print("----")


i=0
while i < 4:
    j = 0
    while j < 4:
        print("am[", i, "][", j, "] = ", am[i][j])
        j += 1
    i += 1

print("----")

for (x,y,z,q) in am:
    print("x = ", x, " y = ", y, " z = ", z, " q = ", q)

print("----")

for x in am[3]:
    print("x = ", x)

print("-----------")

masrazm = np.array([0], int)
i = 0
for x in am.shape:
    if i == 0:
        masrazm[i] = x
        print("i = ", i, " x = ", x)
    else:
        masrazm = np.append(masrazm, [x])
        print("i = ", i, " x = ", x)
    i += 1
    #print(x)

print(masrazm)

print("-----------")

print("amm is \n", amm)

masrazm = np.array([0], int)
i = 0
for x in amm.shape:
    if i == 0:
        masrazm[i] = x
        print("i = ", i, " x = ", x)
    else:
        masrazm = np.append(masrazm, [x])
        print("i = ", i, " x = ", x)
    i += 1
    #print(x)

print("Mass razm is ", masrazm)
print("Razmernost for masrazm is ", i)

print("-----------")


i = 0
while i < masrazm[0]:
    j = 0
    while j < masrazm[1]:
        k = 0
        for x in amm[i][j]:
            print("i = ", i, " j = ", j, " k = ", k)
            print("amm[", i, "][", j, "][", k, "] = ", amm[i][j][k])
            print("Parametr x = ", x)
            k += 1
        j += 1
    i += 1



