import numpy as np
list=[12,23,45,12,1,2]
list[1]=56
arr=np.array(list)

print (f"Array is:\n{arr}\n") 
print(f"Reshape array in (2,3)is:\n{arr.reshape(2,3)}")
