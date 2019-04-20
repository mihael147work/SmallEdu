from numpyPlus import *

"""Math methods wit arrays"""

print("y \n", y)
print("x \n", x)
print("y + x \n", x + y)
print("x - y \n", x - y)
print("x * y \n", x * y)
print("y / x \n", y / x)
print("y % x \n", y % x)

print("--------------------------------------------------")

print("am \n", am)
print("bm \n", bm)

print("am * bm \n", am * bm)

print("--------------------------------------------------")

aa = np.array([[1, 2], [3, 4], [5, 6]], float)

bb = np.array([-1, 3], float)

print("aa \n", aa)
print("bb \n", bb)
print("aa + bb \n", aa + bb)

print("--------------------------------------------------")


aa = np.zeros((2,2), float)
bb = np.array([-1., 3.], float)

print("aa \n", aa)
print("bb \n", bb)
print("aa + bb \n", aa + bb)
print("aa + bb[np.newaxis,:] \n", aa + bb[np.newaxis,:])
print("aa + bb[:,np.newaxis] \n", aa + bb[:,np.newaxis])

print("--------------------------------------------------")

