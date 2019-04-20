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


bam = np.array([am, bm, cm, dm])
bxm = np.array([xm, ym, zm, qm])

############################################

rm = np.array(range(12), float).reshape(3,4)
arm = np.arange(6, dtype=float)
arm2 = np.arange(-2, 18, 2, dtype=float)
