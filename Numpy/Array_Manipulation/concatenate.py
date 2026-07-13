import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
print(f"Array 1 is:\n{arr1}")
print(f"Array 2 is:\n{arr2}")
new=np.concatenate((arr1,arr2))
print(f"Concatenate Array is:\n{new}")