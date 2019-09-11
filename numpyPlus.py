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

ak = np.array([[-1, 1], [2, 0], [0, 3]])
ap = np.array([[3, 1, 2], [0, -1, 4]])

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

rm = np.array(range(12), float).reshape(3, 4)
arm = np.arange(6, dtype=float)
arm2 = np.arange(-2, 18, 2, dtype=float)


def matrix_mnoj(massiv1, massiv2, flag=0):
    mi = massiv1.shape[1]
    mk = massiv2.shape[1]
    result = [[0 for k in range(mk)] for l in range(mk)]

    if massiv1.shape[1] == massiv2.shape[0]:

        for j in range(mk):
            for k in range(mk):
                znacen = 0

                for i in range(mi):
                    znacen += massiv1[k][i] * massiv2[i][j]
                result[k][j] = znacen

        if flag == 1:
            print("shape of result ", massiv1.shape[0], "x", massiv2.shape[1])
            print(result)
        else:                               # - можно убрать - отладочный маркер про флаг
            print("Print-flag is not 1")    # - Есть необязательный параметр после матриц - если указать 1 то выводит результат в консоль
    else:
        print("razmernost matric ne correctna")

    return result


# def matrix_mnoj(massiv1, massiv2, flag=0):
#     mi = massiv1.shape[1]
#     mj = massiv1.shape[0]
#     mk = massiv2.shape[1]
#
#     if massiv1.shape[1] == massiv2.shape[0]:
#         #print("shape of matrix is correct")
#         #print("shape of result ", massiv1.shape[1], "x", massiv2.shape[0])
#         razm = massiv1.shape[1]
#         res = np.array
#
#         i = 0
#         j = 0
#         k = 0
#
#         # print("---------begin---------")
#         #
#         # print("massiv1 is", massiv1)
#         # print("massiv2 is", massiv2)
#
#         result = [[0 for k in range(mk)] for l in range(mk)]
#
#         for j in range(mk):
#             # print("j=", j)
#             for k in range(mk):
#                 # print("k=", k)
#                 znacen = 0
#
#                 # print("-----------------")
#                 # print("j is -", j)
#                 # print("i is -", i)
#                 #
#                 # print("k is -", k)
#                 # print("p is -", p)
#                 znacen = 0
#
#                 for i in range(mi):
#                     # print("i=", i)
#                     # print("massiv1[", k, "][", i, "] is -", massiv1[k][i])
#                     # print("massiv2[", i, "][", j, "] is -", massiv2[i][j])
#                     # print("massiv1[", k, "][", i, "] * massiv2[", i, "][", j, "] is -", massiv1[k][i] * massiv2[i][j])
#
#                     znacen += massiv1[k][i] * massiv2[i][j]
#                 # znacen = massiv1[i][k]
#                 # print("znacen = ", znacen)
#                 result[k][j] = znacen
#
#                 i = 0
#                 znacen = 0
#
#         # print("array slicing is work ak[:,1] ->", ak[:,1])
#         # print("array slicing is work ap[2,:] ->", ap[2,:])
#
#         if flag == 1:
#             print("shape of matrix is correct")
#             print("shape of result ", massiv1.shape[1], "x", massiv2.shape[0])
#             print(result)
#         else:
#             print("flag is not 1")
#     else:
#         print("razmernost matric ne correctna")
#
#
#     return result


def masrazm(massiv):
    masrazmer = np.array([0], int)
    i = 0
    for x in massiv.shape:
        if i == 0:
            masrazmer[i] = x
            # print("i = ", i, " x = ", x)
        else:
            masrazmer = np.append(masrazmer, [x])
            # print("i = ", i, " x = ", x)
        i += 1
        # print(x)

    return masrazmer


def masrazm_print(massiv):
    masrazmer = np.array([0], int)
    i = 0
    for x in massiv.shape:
        if i == 0:
            masrazmer[i] = x
            # print("i = ", i, " x = ", x)
        else:
            masrazmer = np.append(masrazmer, [x])
            # print("i = ", i, " x = ", x)
        i += 1
        # print(x)

    print("Mass razm is ", masrazmer)
    print("Razmernost for masrazm is ", i)
    return masrazmer
