# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:52:10 2023

@author: renuk
"""

# 1. Program to check if a list is empty
lst = [1,2,3,4,5]
if len(lst)==0:
    print('list is empty')
else:
    print('not empty')


# 2. Using list comprehension construct a list from the 
# squares of each element in the list
lst = [1,2,3,4,5]
lst1 = [i*i for i in lst ]
print(lst1)


# 3. Python script to check whether a given key
# already exists in a dictionary
dict = {1:12,2:24,3:36,4:67}
x = int(input("Enter a number:"))       
if x in dict:
    print("Already exist")
else:
    print("Not exist")


# 4.First, create a range from 100 to 160 with steps of 10
#  Second, using dict comprehension create a dictionary
#  where each number in the range is the key and
#  each item divided by 100 is the value
dict={x:x/100 for x in range(100,160,10) }
print(dict)


# 5. Create a dataframe which comprises course,fees
#   and duration and add tutor column
import pandas as pd
data = {'course' : ['Hadoop','Python','Java'],
        'Fees' : [25000,20000,30000],
        'Duration' : ['30days','45days','50days'],
    }
df = pd.DataFrame(data)
df
df['Tutor']= ['Renuka','Ishika','Shivani']
df


# 6. Write dataframe to csv
df.to_csv('data.csv')


# 7. Write a python function which returns multiple
#   values



# 8. Write a function which takes two arguments: a and b and
#   returns the multiplication of them using lambda function
x=lambda a,b:a*b
x(6,7) 

# 9. Write a numpy program to test if any of the 
#  elements of a given array are non-zero.
import numpy as np
arr=np.array([0,0,12,0])
print(np.any(arr))

# 10.Write a python programming to display a bar chart
#  of the popularity of programming languages
# Sample data:

import matplotlib.pyplot as plt
import pandas as pd
data=pd.Series([22.2,23,7,8.8,7.7,6.7],
               index=['java','python','PHP','Javascript','c#','c++'])
data.index
data
fig=plt.figure()
data.plot(kind='bar')
plt.show()   


    
    
    
    
    
    