slicing

import math
import time
start=time.time_ns()
s=input()
print(s[::-1])
end=time.time_ns()
print(end-start)


recursion

import time
start=time.time()
def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1:])+s[0]
s=input()
print(rev(s))
end=time.time()
print(end-start)

recursion using two pointers

import time
start=time.time()
def reverse(l,a,b):
    if a>=b:
        return
    else:
        l[a],l[b]=l[b],l[a]
        reverse(l,a+1,b-1)
s=input()
l=list(s)
reverse(l,0,len(l)-1)
print(''.join(l))
end=time.time()
print(end-start)


