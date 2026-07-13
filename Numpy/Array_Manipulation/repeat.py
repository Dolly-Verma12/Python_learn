import numpy as np
arr1=np.array([1,2,3,4])
new=np.repeat(arr1,2)
new1=np.tile(arr1,2)
print(f"repeat Array is:\n{new}")
print(f"Tile Array is:\n{new1}")