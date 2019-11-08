import numpy as np
#data = np.random.randn(2,3)
#print(data)
#print(data*10)
#print(data+data)
#print(data.shape)
#print(data.dtype)

data = [6,7.5,8,0,1]
#data = ([1,2],[2,3],[4,5])
npArr = np.array(data)
#print(npArr)

data = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,1],[3,4]]]
npArr1 = np.array(data)
#print(npArr1)
#print(npArr1.ndim)
#print(npArr1.shape)
#print(npArr.dtype)
#print(npArr1.dtype)

#empty = np.empty((3,6))
#zeros = np.zeros((3,6))
#ones = np.ones((3,6))
#print(zeros)

#range1 = np.arange(10)
#print(range1)

#arr1 = np.array([1,2,3],dtype=float)
#print(arr1)

#arr1 = np.array([1,2,3],dtype=int)
#print(arr1)

#arr2 = arr1.astype(str)
#print(arr2)

#arr1 = np.random.randn(2,3)
#arr1 = np.empty(8,dtype='u1')
#print(arr1)
#print(arr1*arr1)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 =  np.array([[0,4,1],[7,2,12]])
#print(arr1*arr1)
#print(arr1+arr1)
#print(arr1-arr1)
#print(1/arr1)
#print(np.array(arr1/4))
#print(np.array(arr1/4).astype(int))
#print(arr1>arr2)

#Operations between differently sized arrays is called broadcasting and will be dis‐
#cussed in more detail in Appendix A. Having a deep understanding of broadcasting is
#not necessary for most of this book.

# propagated (or broadcasted henceforth) to the entire selection. An important first dis‐
# tinction from Python’s built-in lists is that array slices are views on the original array.
# This means that the data is not copied, and any modifications to the view will be
# reflected in the source array.

arr = np.arange(10)

#print(arr[5:8])
# arr[5:8] = 12
# #print(arr)
# slice_arr = arr[5:8]
# slice_arr[0]=12324
# slice_arr[:]=64
# print(arr)

# arr_slice = arr[5:8].copy()
# arr_slice[:]=64
# print(arr_slice)
# print(arr)

#arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d[0][1])
# print(arr2d[0,1])
#print(arr2d[0:2])
#print(arr2d[:2,1:])

#names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
#data = np.random.randn(7,4)
#print(data)
#print("===============")
#print(names=='Bob')
#print(data[names=="Bob"])
#print(data[np.array([True,False,True,False,False,False,False])])
#print(data[names=='Bob',2:])
#print(data[names=='Bob',3])
#print(data[names!='Bob'])
#print("==============")
#print(data[~(names=='Bob')])
#print("==================")
#cond = names=='Bob'
#print(data[~cond])
#mask = (names=='Bob') | (names=='Will')
#print(data[mask])
#data[data<0]=0
#print("===============")
#data[names!='Joe']=7
#print(data)


# arr = np.empty((8,4),dtype=int)
# for i in range(8):
#     arr[i]=i*2
# print(arr)
# print("===========")
# print(arr[1,2])
# print("===========")
# print(arr[[1,2]])
# print("===========")
# print(arr[np.array((3,2))])
# print(arr[[-5,-3,-7]])


