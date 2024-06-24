# arr= [2,1,3,2,3]
# c=0
# n=5
# b=[]
# for i in range(n):
#   for v in range(i+1,n):
#     if arr[i]==arr[v]:
#      b.append(arr[i])
# s=set(b)     
# for z in (s)  :    
#     c=c+1
# if c!=0:
#      print(s)
# else:
#     print(-1)
#------------------------------------------------------
# B = [6, 5, 5, 4, 3, 4, 3, 7]
# N=8


# def check(A, B, N):

#         # return: True or False
#         v = 0
#         s=0
#         m=0
#         m2=0
#         for i in range(N+1):
#           v = A[i]+v
    
#         for i in range(N+1):
#           s=B[i]+s
     
        
#         for i in range(N+1):
#           m=A[i+1]+m
#         m1=A[0]-m
     
#         for i in range(N+1):
#          m2=B[i+1]+m2
#         m3=B[0]-m
#         if(s==v & m3==m1):
#             return True
#         else:
#             return False
# c=check(A,B,N)
#----------------------------------------------------------------------------------------------------------------------------------------
# srr=set(arr)
# c=0
# fn=1
# ff=1
# f3=1
# n=5
# c1=0
# for i  in (srr):
#   c=c+1
# for w in range(c,n):
  
#   for v in range(1,w+1):
#     fn=fn*v
#   f=c-w 
#   for v in range(1,f+1):
#     ff=ff*v
#   for v in range(1,3+1):
#     f3=f3*v
#   m=ff*f3       
#   o= fn/m
#   c1=o+c1
  
  
# print(c1)
  
  # ----------------------------------------------------------------------
# import cv2
 
# # To read image from disk, we use
# # cv2.imread function, in below method,
# img = cv2.imread("imgtl.png", cv2.IMREAD_COLOR)
 
# # Creating GUI window to display an image on screen
# # first Parameter is windows title (should be in string format)
# # Second Parameter is image array
# img
 
# # To hold the window on screen, we use cv2.waitKey method
# # Once it detected the close input, it will release the control
# # To the next line
# # First Parameter is for holding screen for specified milliseconds
# # It should be positive integer. If 0 pass an parameter, then it will
# # hold the screen until user close it.
# cv2.waitKey(0)
 
# # It is for removing/deleting created GUI window from screen
# # and memoryprint
# f={'hh':'hg','ff':'gu'}
# for k,v in f.items():
#   print(k,v)
# x= [5,301,3,299,800]
# for i in (x):
#  if(i<=300):
#     cost=3000
#  else:
#     cost=i*10
# from os import fork


# j=0
# def ll(i):
#    i=0
#    i=i+1
#    print(i)
#    return i
   
# j=ll(j)  
# j=ll(j)
# j=ll(j)
# fork()
# print("hom")
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
#     n=3
#     a=[]
#     b=[]
#     br=0
#     ar=0
    
#     if a[0]<b[0]:
#        br=br+1
#     else:
#        ar=ar+1
#     if a[1]<b[1]:
#        br=br+1
#     else:
#        ar=ar+1
#     if a[2]<b[2]:
#        br=br+1
#     else:
#        ar=ar+1 
#     a[3]=ar
#     b[3]=br    
#     return(ar,br)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     a = list(map(int, input().rstrip().split()))

#     b = list(map(int, input().rstrip().split()))

#     result = compareTriplets(a, b)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
# -------------------------------------------------------------

# n=6
# a=[[] for i in range(n)]
# i=0
# j=0
# for i in reversed(range(n-1)):
     
#       for j in  range(n):
#            if i
#           print('#')
#       j=j+1     
     
# import math
# import os
# import random
# import re
# import sys
# import html

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# def gradingStudents(grades):
#   for g in (grades):
#     if (g>=38):
#         m=g/5
#         m=int(m)
#         n=(m*5)+5
#         k=n-g
#         n=str(n)
#         if k<3:
#             return(n)
#         else:
#             return(g)
#     else:
#         return(g)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grades_count = int(input().strip())

#     grades = []

#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)

#     result = gradingStudents(grades)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
# c={3,45,67,7,776,67,6,5}
# v={5,9}
# v.add(8)
# print(v)
# # b.sizeof()

# s. See help(type(s))
# employees = [(111, 'John'), (123, 'Emily'), (232, 'David'), (100, 'Mark'), (1, 'Andrew')]
# for employee_id, employee_name in employees:
#   print(employee_id, employee_name)
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for i,value in my_dict.items():
#  print(value,i)
# def f(x):
#  return x**2
#  def g(f, x):
#   return f(x)
# s='&quot;&lt;tag&gt;text&lt;/tag&gt;&quot;'
# print(html.unescape(s)) 
# import glob
# a=glob.glob('*.py')
# print(a)
# with open('somefile.txt', 'wt') as f:
#  f.write(s)
#  f.write("hyiii")
#  print("hhhhhhh", file=f)
#  print("yyyyhhh", file=f)
# with open('somefile.txt', 'rt') as f:
#  data=f.read()
#  print(data)
# from tkinter import *
# from PIL import Image,ImageTk
# from tkinter import filedialog
# import os
# def ss():
#     nn=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetypes=(('jpg file','*.jpg'),('PNGfile','*.png'),('all file','*.*')))
#     img=Image.open(nn)
#     img=ImageTk.PhotoImage(img)
#     lbl.configure(image=img)
#     lbl.image=img
# root=Tk()
# root.title("browse image")
# root.title("CAMERA")

# # root.geometry("300X350")
# fr=Frame(root)
# fr2=Frame(root)
# fr.pack(side=BOTTOM,padx=15,pady=15)
# fr2.pack(side=TOP,padx=10,pady=10)
# lbl=Label(root)
# lbl.pack()
# Button2 = Button(  width=5, height=3, font="Helvetica 12 bold", text="STOP",  bg="red", fg="white")
# btn=Button(fr,text="browse image",command=ss)
# btn2=Button(fr2,text="CAMERA")
# btn.pack(side=LEFT)
# root.mainloop()
# _no_value = object
# def spam(a, b=_no_value):
#  if b is _no_value:
#   print('No b value supplied')

# spam(34,4)
#-------------------------------------------------------------------------------------------------------------
# def equaliseTwoStrings(n: int, p: str, q: str) -> str:
#  z=0
#  if p[0]!=q[0]and p[1]==q[1]:
#     q[j]=p[i]
#  for i in range(n):
#   for j in range(n):
#    if p[i]!=q[j]and( p[i-1]==q[j-1]):
#     q[j]=p[i]
#     break
#  for i in range(n):
#   for j in range(n) :  
#      if p[i]==q[j]:
#       z=z+1
#  if z==n:
#   return 'yes'
#  else:
#        return 'no'
# p='asdfgh'
# q='asdfrh'
# n=6
# print(equaliseTwoStrings (n, p, q))\
  
  
#-------------------------------------------------------------------------

# while(True):
#  try:
#   i=int (input('enter a no'))
#   a=1/i
#   print(a)
#  except Exception as e:
#   print(e)
#  finally:
#   print("yaaaa")

def ff(x,y):
  for i in range(pow(10,6)):
    a=x-1
    b=x+1
    if(a%y==0):
      return a
    if(b%y==0):
      return b
    if(a%y==0 and b%y==0):
      c=a/y
      d=b/y
      if(c>d):
        return a
      else:
        return b
x=int(input())
y=int(input())
r=ff(x,y)
print(r)