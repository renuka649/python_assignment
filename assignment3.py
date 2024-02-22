# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:17:25 2023

@author: renuk
"""

#assignment 3 question 1
#take 5 numbers in list find out min of list and max of list
l1=[1,4,5,6,3]
min=l1[0]
max=l1[0]
for i in range(1,len(l1)):
    if l1[i]<min:
        min=l1[i]
    if l1[i]>max:
        max=l1[i]
print("the minimum is : ",min)
print("the maximum number is : ",max)

#question 2
#take a 5 string in a list make it reverse

List=['renuka','pooja','sakshi','prerna','sai']
t=List[::-1]
print(t)

#question 3
#take 10 numbers in list write script to search for value
l1=[1,4,5,6,3,22,45,23,12,43]
n=int(input("enter the number to be search : "))
for i in range(1,len(l1)):
    if n==l1[i]:
        print("values is found at index is :",i)
    
#question4

l=[1,4,1,2,3,5,2,5,6,3,2,7,9,6]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
    else:
        print(i,end='')

#question5
l=['a','t','e','f','u','t','r']
count=0
for i in range(len(l)):
    if l[i] in ('a','e','i','o','u'):
        count=count+1
print(count) 

      
      
      
      
      
      
      
      
      