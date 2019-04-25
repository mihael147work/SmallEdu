from numpyPlus import *

masrazm_print(ammm)

print("a is \n", a)
print("a.sum() ", a.sum())
print("a.prod() ", a.prod())
print("np.sum(a) ", np.sum(a))
print("np.prod(a) ", np.prod(a))

print("a.mean() ", a.mean())        # srednee arifeti4
print("a.var() ", a.var())          # Variacia
print("a.std() ", a.std())          # Deviacia

print("a.min() ", a.min())
print("a.max() ", a.max())

print("a.argmin() ", a.argmin())
print("a.argmax() ", a.argmax(), "\n")

print("--------------------\n")

print("xm is \n", xm)

print("xm.mean(axis=0) ", xm.mean(axis=0))        # srednee arifeti4
print("xm.mean(axis=1) ", xm.mean(axis=1))        # srednee arifeti4


print("xm.min(axis=0) ", xm.min(axis=0))
print("xm.min(axis=1) ", xm.min(axis=1))
print("xm.max(axis=0) ", xm.max(axis=0))
print("xm.max(axis=1) ", xm.max(axis=1))

x = np.array([6, 2, 5, -1, 0], float)

print("x is \n", x)
print("sorted(x)", sorted(x))
x.sort()
print("x.sort()", x, "\n")

print("---------------------------\n")


print("x.clip(0, 3.5)", x.clip(0, 3.5), "\n")
print("---------------------------\n")

x = np.array([1, 1, 4, 5, 5, 5, 7], float)
y = np.array([3, 1, 5, 2, 4, 6, 8], float)
print("x is \n", x)

print("np.unique(x)", np.unique(x), "\n")

print("---------------------------\n")

print("xm is \n", xm)
print("xm.diagonal()", xm.diagonal(), "\n")

print("---------------------------\n")

print("x is \n", x)
print("y is \n", y)


print("x > y", x > y)

