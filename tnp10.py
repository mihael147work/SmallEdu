from numpyPlus import *


print("Filtracia mssiv")
print ("a is \n", a)
print("a < 3 ", a < 3)
print("a[a >= 3] ", a[a >= 3])
fil = (a >= 3)
print("a[fil] ", a[fil])
print("a[np.logical_and(a > 1, a < 4)] ", a[np.logical_and(a > 1, a < 4)])
print("---------------------------\n")


b = np.array([0, 0, 1, 3, 2, 1], int)
print ("a is \n", a)
print ("b is \n", b)
print("a[b]", a[b])

print("a[[0, 1, 0, 2, 0, 3, 2, 0]]", a[[0, 1, 0, 2, 0, 3, 2, 0]])
print("---------------------------\n")


a = np.array([[1, 4], [9, 16]], float)
b = np.array([0, 0, 1, 1, 0], int)
c = np.array([0, 1, 1, 1, 1], int)
print ("a is \n", a)
print ("b is \n", b)
print ("c is \n", c)
print("a[b, c]", a[b, c])
print("---------------------------\n")


a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int)
# only for integer
print ("a is \n", a)
print ("b is \n", b)
print ("a.take(b)", a.take(b))
print("---------------------------\n")


a = np.array([[0, 1], [2, 3]], float)
b = np.array([0, 0, 1], int)
print ("a is \n", a)
print ("b is \n", b)
print ("a.take(b, axis=0)", a.take(b, axis=0))
print ("a.take(b, axis=1)", a.take(b, axis=1))
print("---------------------------\n")





