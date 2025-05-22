import numpy as np
import pandas as pd
#1. GÖREV
arr=np.array([1,2,3,4,5],dtype=int)
print(arr)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

#2. GÖREV
arr2=np.array([[1,2,6,7],[4,3,9,5]])
print(arr2)
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype)
print(arr2.shape)

arr3=np.array([[[7,5,14],
                [21,8,11]],

               [[8,6,20],
                [14,3,9]]])
print(arr3)
print(arr3.ndim)
print(arr3.size)
print(arr3.dtype)
print(arr3.shape)

#3. GÖREV
print(arr2[0,1])
print(arr2[0,3])
print(arr3[1,1,2])
print(arr3[0,0,1])

#4. GÖREV
print(arr3[0,1,0:])
print(arr3[1,0,1:])
print(arr2[0,1:3])
print(arr2[1,1:])

#5. GÖREV
sifir=pd.DataFrame(np.zeros((5,3)))
bir=pd.DataFrame(np.ones((5,3)))
print(pd.concat([sifir,bir],axis=1,ignore_index=True))
print(pd.concat([sifir,bir],axis=0,ignore_index=True))
