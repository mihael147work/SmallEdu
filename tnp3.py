from numpyPlus import *


print("xm(4, 4) is \n", xm)

print("Use xm.fill(3)")

xm.fill(3)

print("xm(4, 4) is \n", xm)

print("--------------------------------------------------")

zz = np.array(range(12), float).reshape(3,4)

print(zz)

print("bb = zz.transpose()\n", zz.transpose())
bb = zz.transpose()
print("zz.flatten()\n", zz.flatten())
print("bb.flatten()\n", bb.flatten())

print("--------------------------------------------------")
print("x is \n", x)
print("y is \n", y)
print("z is \n", z)

print("np.concatenate((x, y, z)) is \n", np.concatenate((x, y, z)))
print("np.concatenate((a, b, c)) is \n", np.concatenate((a, b, c)))

print("--------------------------------------------------")

print("zm is \n", zm)
print("ym is \n", ym)

print("np.concatenate((zm, ym), axis=0) is \n", np.concatenate((zm, ym), axis=0))

ii = np.array(range(12), float).reshape(3,4)
jj = np.array(range(12), float).reshape(4,3)

print("ii is \n", ii)
print("jj is \n", jj)

print("np.concatenate((ii, jj.reshape(3,4)), axis=0) is \n", np.concatenate((ii, jj.reshape(3,4)), axis=0))

print("np.concatenate((ii, jj.reshape(3,4)), axis=1) is \n", np.concatenate((ii, jj.reshape(3,4)), axis=1))

print("--------------------------------------------------")

print("ii is \n", ii)
print("jj is \n", jj)

print("jj[:, np.newaxis] \n", jj[:,np.newaxis])
print("ii[np.newaxis, :] \n", ii[np.newaxis,:])

jj1 = jj[:,np.newaxis]
ii1 = ii[np.newaxis,:]

print("Old ii shape is ", ii.shape)
print("Old jj shape is ", jj.shape)

print("New ii shape is ", ii1.shape)
print("New jj shape is ", jj1.shape)
