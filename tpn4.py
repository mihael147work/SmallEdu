from numpyPlus import *


renmass = np.array(range(12), float).reshape(3,4)
armass = np.arange(6, dtype=float)
armass2 = np.arange(-2, 18, 2, dtype=float)

print("np.array(range(12), float).reshape(3,4) \n", renmass)
print("np.arange(6, dtype=float) \n", armass)
print("np.arange(-2, 18, 2, dtype=float) \n", armass2)


print("--------------------------------------------------")

print("np.ones((2,3), dtype=float) \n", np.ones((2,3), dtype=float))
print("np.zeros(7, dtype=int) \n", np.zeros(7, dtype=int))


print("--------------------------------------------------")

print("renmass is \n", renmass)
print("np.zeros_like(renmass) \n", np.zeros_like(renmass))
print("np.ones_like(renamss) \n", np.ones_like(renmass))


print("------------------Matrix---------------------------")

print("np.identity(4, dtype=float) \n", np.identity(4, dtype=float))

print("np.eye(5, k=2, dtype=float) \n", np.eye(5, k=2, dtype=float))


