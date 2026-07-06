import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(np.version)

a = np.array(1)
b = np.array([1,2,3,4])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr5 = np.array([1,2,3,4], ndmin=5)

print(arr5)
print(f"number of dimension = {arr5.ndim}")

#exercide
arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr1[1, 0])
print(arr1[0] + arr[1])

#Checking Data Type
"""
data type:
- `i` - integer
- `b` - boolean
- `u` - unsigned integer
- `f` - float
- `c` - complex float
- `m` - timedelta
- `M` - datetime
- `O` - object
- `S` - string
- `U` - unicode string
- `V` - fixed chunk of memory for other type ( void )
"""
print(arr.dtype)

#define type
arr67 = np.array([1,2,3], dtype='S')
print(arr67.dtype)
#define size for i, u, f, s
arr123 = np.array([1,2,3], dtype='i4')
print(arr123.dtype)

#converting data type

arr = np.array([1.1, 2.1, 3.1])

newarr =arr.astype('i')

print(newarr)
print(newarr.dtype)

#converting existinf data type
arr = np.array([1.2, 1.23, 2.33])

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#copy vs view
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)



arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

#when copy own its data and return the same thing
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

#reshape
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)
print(newarr)

""" output: 
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
 """
newarr = arr.reshape(2,3,2)
print(newarr)
""" output:
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
  """

#check returned array is copy or view
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

#calculate dimention reshape
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)