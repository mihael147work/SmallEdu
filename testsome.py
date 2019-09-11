from numpyPlus import *

print("ak is\n", ak)
print("ap is\n", ap)

print("ak.SHAPE is\n", ak.shape)
print("ap.shape is\n", ap.shape)


print("ak[0][0] is\n", ak[0][0])
print("ak[0][1] is\n", ak[0][1])
print("ak[1][0] is\n", ak[1][0])


print("--------------------------------------------------")

matrix_mnoj(ak,ap,1)

print("--------------------------------------------------")

#
# i = 0
# j=0
# k=0
# print(i)
#
# mi = ak.shape[1]
# print(mi)
#
# mk = ak.shape[0]
# mj = ap.shape[1]
#
# print(mj)
# print(mk)
#
# print("---------begin---------")
#
#
# print("ak is", ak)
# print("ap is", ap)
#
# result = [[0 for k in range(mk)] for l in range(mk)]
#
#
# for j in range(mk):
#     print("j=", j)
#     for k in range(mk):
#         print("k=", k)
#         znacen = 0
#
#         print("-----------------")
#         print("j is -", j)
#         print("i is -", i)
#
#         print("k is -", k)
#         #print("p is -", p)
#         znacen = 0
#
#         for i in range(mi):
#             print("i=", i)
#             print("ak[", k, "][", i, "] is -", ak[k][i])
#             print("ap[", i, "][", j, "] is -", ap[i][j])
#             print("ak[", k, "][", i, "] * ap[", i, "][", j, "] is -", ak[k][i] * ap[i][j])
#
#             znacen += ak[k][i] * ap[i][j]
#         # znacen = massiv1[i][k]
#         print("znacen = ", znacen)
#         result[k][j] = znacen
#
#         i=0
#         znacen = 0
#
#
# # print("array slicing is work ak[:,1] ->", ak[:,1])
# # print("array slicing is work ap[2,:] ->", ap[2,:])
#
# print(result)