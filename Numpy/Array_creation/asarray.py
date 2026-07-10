import numpy as np

print("Convert existind data into a numpy array")
list=[12,13,14,20]
print(f"Data list is:\n{list}\n")
arr=np.asarray(list)
arr2=np.asarray(arr)
print(f"Data numpy Array(asarray) is:\n{arr}\n")
list[0]=1
print(f"Updated Data list is:\n{list}\n")
print(f"After updation numpy Array(asarray) is:\n{arr2}\n")