import numpy as np


"""Import NymPy and some data"""

### init integer arrays
a = np.array([1, 2, 3, 4], int)
b = np.array([5, 6, 7, 8], int)
c = np.array([9, 10, 11, 12], int)
d = np.array([13, 14, 15, 16], int)

### init float arrays
x = np.array([1., 2., 3., 4.], float)
y = np.array([5., 6., 7., 8.], float)
z = np.array([9., 10., 11., 12.], float)
q = np.array([13., 14., 15., 16.], float)

### init 2 metrik arrays
am = np.array([a, b, c, d])
xm = np.array([x, y, z, q])

bm = am.copy()
cm = am.copy()
dm = am.copy()

ym = xm.copy()
zm = xm.copy()
qm = xm.copy()

# init 3 metrik arrays

amm = np.array([am, bm, cm, dm])
xmm = np.array([xm, ym, zm, qm])

bmm = amm.copy()
cmm = amm.copy()
dmm = amm.copy()

ymm = xmm.copy()
zmm = xmm.copy()
qmm = xmm.copy()


bam = np.array([am, bm, cm, dm])
bxm = np.array([xm, ym, zm, qm])


# init 4 metrik arrays

ammm = np.array([amm, bmm, cmm, dmm])
xmmm = np.array([xmm, ymm, zmm, qmm])


############################################

rm = np.array(range(12), float).reshape(3,4)
arm = np.arange(6, dtype=float)
arm2 = np.arange(-2, 18, 2, dtype=float)

def masrazm(massiv):
    masrazmer = np.array([0], int)
    i = 0
    for x in massiv.shape:
        if i == 0:
            masrazmer[i] = x
            #print("i = ", i, " x = ", x)
        else:
            masrazmer = np.append(masrazmer, [x])
            #print("i = ", i, " x = ", x)
        i += 1
        # print(x)

    return masrazmer

def masrazm_print(massiv):
    masrazmer = np.array([0], int)
    i = 0
    for x in massiv.shape:
        if i == 0:
            masrazmer[i] = x
            #print("i = ", i, " x = ", x)
        else:
            masrazmer = np.append(masrazmer, [x])
            #print("i = ", i, " x = ", x)
        i += 1
        # print(x)

    print("Mass razm is ", masrazmer)
    print("Razmernost for masrazm is ", i)
    return masrazmer
