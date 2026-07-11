import numpy as np


list=[12,13,14,15,12,16]
print(f"1-D Array:\n{list}")
arr=np.array(list)
print("Size of the array is:\n{}".format(arr.size))

#list 2
list2=[[12,13,1],[13,24,35]]
print(f"\n2-D Array:\n{list2}")
arr=np.array(list2)
print("Size of the array is:\n{}".format(arr.size))

#list 3
list3=[[[12,23],[133,14]],
       [[14,45],[34,56]]
       ]
print(f"\n3-D Array:\n{list3}")
arr=np.array(list3)
print("Size of the array is:\n{}".format(arr.size))

