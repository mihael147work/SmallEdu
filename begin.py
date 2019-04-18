import numpy as np

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
bam = np.array([am, bm, cm, dm])
bxm = np.array([xm, ym, zm, qm])


# begin work with numpy instruments
print("am.shape ->", am.shape)
print("am.dtype ->", am.dtype)
print("type(am) ->", type(am))
print("am is\n", am)
print("array slicing is work am[:,1] ->", am[:,1])
print("array slicing is work am[2,:] ->", am[2,:])


amm = np.array([am, bm, cm, dm])
xmm = np.array([xm, ym, zm, qm])


print("amm.shape is ", amm.shape)

bmm = amm.reshape(2, 4, 8)
print("bmm = amm.reshape(2,4,8) ")
print("bmm.shape is ", bmm.shape)
print("--------------------------------------------------")



len(bm)
n = 5 in x
print (n, "and ", len(x))

print("am is\n", am)
print("am.reshape(16) is\n", am.reshape(16))
print("am.reshape(2,2,4) is\n", am.reshape(2,2,4))

print("--------------------------------------------------")

print("am.tolist()\n", am.tolist())
print("list(am)\n", list(am))

print("--------------------------------------------------")


