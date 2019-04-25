from numpyPlus import *



x = np.array([1, 1, 4, 5, 5, 5, 7], float)
y = np.array([3, 1, 5, 2, 4, 6, 8], float)

xy = y > x

print("x is \n", x)
print("y is \n", y)
print(xy)

print("x > 2", x > 2)
print("---------------------------\n")

print("xy is \n", xy)
print("any(xy)", any(xy))
print("all(xy)", all(xy))

print("---------------------------\n")

a = np.array([1, 3, 0], float)
print("a is \n", a)
print("np.logical_and(a > 0, a < 3)", np.logical_and(a > 0, a < 3))


b = np.array([True, False, True], bool)
print("b is \n", b)
print("np.logical_not(b)", np.logical_not(b))


c = np.array([False, True, False], bool)
print("c is \n", c)
print("np.logical_or(b, c)", np.logical_or(b, c))


print("---------------------------\n")

# where(boolarray, truearray, falsearray):
print("a is \n", a)
#print("np.where(a != 0, 1 / a, a)", np.where(a != 0, 1 / a, a))
print("np.where(a > 0, 3, 2)", np.where(a > 0, 3, 2))

print("---------------------------\n")

xm[1][3] = 0
xm[3][2] = 0
xm[2][0] = 0
xm[2][3] = 0

print("xm is\n", xm)

a = xm.nonzero()
print("xm.nonzero()", a)

a = np.array([[0, 1, 3, 0], [3, 0, 3, 0]], float)
print("a.nonzero()", a.nonzero())


print("---------------------------\n")

a = np.array([1, np.NaN, np.Inf], float)
print("a is \n", a)

print("np.isnan(a)", np.isnan(a))
print("np.isfinite(a)", np.isfinite(a))


print("---------------------------\n")





