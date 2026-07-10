import  numpy as np

print("1-D Array ")
arr= np.array([10,20,30])
print(arr)


print("\n 2-D Array ")
arr1=np.array([[10,90,80],
              [20,30,45]])
print(arr1)


print("\n 3-D Array ")
arr3=np.array([
    [[1,2],[3,4]],
    [[5,4],[10,20]]
])
print(arr3)


print("\n numpy Array copy the list then convet the data into the array!!")
list=[2,1,3,4]
ap=np.array(list)
print("Before updation :")
print(ap)
ap2=np.array(ap)
list[0]=5
print(" list[0]=5 After updation :")
print(ap2)
