from numpyPlus import *


# begin work with numpy instruments
print("am.shape ->", am.shape)
print("am.dtype ->", am.dtype)
print("type(am) ->", type(am))
print("am is\n", am)
print("array slicing is work am[:,1] ->", am[:,1])
print("array slicing is work am[2,:] ->", am[2,:])


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
lm = am.reshape(16).copy()
lm[0]=100
print("lm is \n", lm)

print("am is \n", am)
print("am.reshape(2,2,4) is\n", am.reshape(2,2,4))


print("--------------------------------------------------")

print("am.tolist()\n", am.tolist())
print("list(am)\n", list(am))

