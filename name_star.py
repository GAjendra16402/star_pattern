#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


# factor of number
def factors_number(num):
    factors = []
    for i in range(1, num+1):
        if num % i ==0:
            factors.append(i)
    return factors
number = int(input("enter a number:"))
print('factors of',number,'are:',factors_number(number))


# In[4]:


def star_pattern(n):
    for i in range (1, n+1):
        print("*"*i)
rows = int(input("enter number:"))
print("pattern")
star_pattern(rows)


# In[5]:


def star_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

rows = int(input("Enter a number: "))
print("Pattern:")
star_pattern(rows)


# In[6]:


def rearrange_string_with_number_last(string):
    words = string.split()
    rearranged_words = []
    for word in words:
        if word.isalpha():
            rearranged_words.append(word + '1')
    return ' '.join(rearranged_words)

sentence = input("Enter a sentence: ")
print("Rearranged sentence:", rearrange_string_with_number_last(sentence))


# In[8]:


def vertical_histogram(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            if char in frequency:
                frequency[char] = +1
            else:
                frequency[char] = 1
                
    max_freq = max(frequency.values())
    for i in range(max_freq, 0, -1):
        for char in frequency:
            if frequency[char] >=i:
                print(char, end = ' ')
            else:
                print(' ', end=' ')
            print()
            
sentence = input('enter a sentence for vertical histogram:')
print('Vertical Histogram:')
vertical_histogram(sentence)


# # PATTERN PRINTING 

# In[9]:


def number_pattern(n):
    for i in range (1, n+1):
        for j in range(i, 0, -1):
            print(j, end='')
        print()
n = int(input("enter number"))
print("pattern")
number_pattern(n)


# In[10]:


def pattern_print(n):
    for i in range(n):
        for j in range(n):
            if j < n - i -1:
                print('$',end='')
            else:
                print('*',end='')
        print()
        
n = int(input('enter the number of rows'))
pattern_print(n)


# In[11]:


def star_pattern(n):
    for i in range (1, n+1):
        print("*"*i)
rows = int(input("enter number"))
print("pattern")
star_pattern(rows)


# In[ ]:


def pattern_star(n):
    for i in range(n):
        for j in range(n):
            if j < n-i-1:
                print(' ',end='')
            else:
                print('*',end='')
        print()
        
n = int(input('enter the number of row'))
pattern_star(n)


# In[ ]:


def star_print(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(96+j), end='')
        print()
        
n = int(input('enter number of rows'))
star_print(n)


# In[ ]:


x=1

for i in range(4):
    for j in range(0,x):
        print("*", end=" ")
    x=x*2
    print("")


# In[ ]:


n = int(input())

for i in range (0,n):
    for j in range(0,i+1):
        print(i+1,end = "")
        
    print(" ")
    


# In[ ]:


def right_angle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j == 1 or i == n or i == j:
                print('*', end='')
            else:
                print(" ", end='')
        print()
n = int(input('enter the number of rows'))
right_angle(n)


# In[ ]:


def print_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j == 0 or i == rows - 1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()
n = int(input('enter the row'))
print_pattern(n)


# In[ ]:


def print_shape(n):
    for i in range(n):
        for j in range(n):
            if j == n-1 or j==n-i-1 or i==0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        
n = int(input())
print_shape(n)




# In[ ]:


def pattern_star(n):
    for i in range(n):
        for j in range(n):
            if j < n-i-1:
                print(' ',end='')
            else:
                print('*',end='')
        print()
        
n = int(input('enter the number of row'))
pattern_star(n)


# In[ ]:


n = 6
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(' ',end="")
    for k in range(1,i+1):
        if k ==1 or k == i or i == n:
            print('*',end='')
        else:
            print(' ',end='')
        
    print('')


# In[ ]:


def print_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j == 0 or j == rows - 1 or i == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
rows = int(input())
print_pattern(rows)


# In[ ]:





# In[ ]:





# In[ ]:


def print_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if j == rows - 1 or i == 0 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

n = int(input('Enter the number of rows: '))
print_pattern(n)


# In[ ]:


for i in range(1,6):
    for j in range(6,i,-1):
        if j==i+1 or  j== 6 or i ==1 :
            print('*',end='')
        else:
            print(' ',end = '')
    print(' ')


# In[ ]:


def print_rhombus(rows):
    for i in range(rows):
        print(" " * i + "*" * rows)

# Take user input for the number of rows
rows = int(input("Enter the number of rows for the rhombus: "))
print_rhombus(rows)


# In[16]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or i==n-1 or(j==n-1 and i>=2) or (i==2 and j>=2)):
            print("*", end= " ")
        else:
            print(" ", end=' ')
    print("")
            


# In[26]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or j==n-1 or i==(n//2)):
            print("*", end= " ")
        else:
            print(" ", end=' ')
    print("")


# In[29]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==2 or (i==n-1 and j<=2)or (j==0 and i>=3)):
            print("*", end= " ")
        else:
            print(" ", end=' ')
    print("")
            


# In[33]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or i==n-1 or i==2):
            print("*", end= " ")
        else:
            print(" ", end=' ')
    print("")


# In[37]:


n = int(input())
for i in range(0,n):
    for j in range(0,n):
        if j in (0,n-1) or (i==j):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[119]:


n= int(input())
for i in range(0,n):
    for j in range(0,n):
        if (j==1 or ((i==0 or i==n-1) and (j>1 and j<n-2)) or (j==n-2 and i!=0 and i!=n-1)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[79]:


# n= int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if(j==0 or i==0 or i==2 or(j==n-1 and i<=2)):
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print(' ')

n = int(input())
for i in range(0, n):
    for j in range(0, n):
        if (j == 0 or i == 0 or i == 2 or (j == n - 1 and i <= 2) or (i==j)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[28]:


n= int(input())

for i in range(0,n):
    for j in range(0,n):
        if (i==0 or j==0 or j==n-1 or i==(n//2)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[33]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==n-1 or i==2 or (j==n-1 and i>=2)or j==0 and i<=2):
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[36]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or i==n-1 or j==2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[44]:


n=int(input())

for i in range(0,n):
    for j in range(0,n):
        if(j==0 or j==n-1 or i==j):
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print(' ')


# In[55]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or i==n-1 or(j==n-1 and i>=2)or(i==2 and j>=2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
            
    print(' ')


# In[1]:


n = int(input())

for i in range(0,n):
    for j in range(0,n):
        if(j==0 or j==n-1 or i==2):
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print(' ')

