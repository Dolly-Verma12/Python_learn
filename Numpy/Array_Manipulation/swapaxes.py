import numpy as np 

arr=np.arange(8).reshape(2,2,2)
print(f"Array:\n {arr}")
print(f"Swape Array is:\n {np.swapaxes(arr,0,1)}")