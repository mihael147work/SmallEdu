from numpyPlus import *


# Warning - tostring and fromstring work correct only with the float
print("-----Tostring intereg - don't work correct----")

print(a)
s = a.tostring()
print(s)
f = np.fromstring(s)
print(f)

print("-----Tostring float - work correct----")

print(x)
s = x.tostring()
print(s)
f = np.fromstring(s)
print(f)
print("--------------------------------------------------")
