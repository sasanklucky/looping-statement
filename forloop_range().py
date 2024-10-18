"""
For Loop with range()
=====================
range()
======
range() is used for performing limits in order to execute for loop.
syntas is range(lowerlimits,upperlimits,updation)

"""


a=range(1,5)
print(a)# return a range object
print(list(a))# convert range object to list

#for loop in range

for i in range(1,5):
    print(i)

#printing sum of natural number in given range

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


#printing a given factorial number

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# checking given number is perfect number or not.

# A perfect number is a positive integer that is equal to the sum of its proper positive divisors except it self.
n=6
sum=0
for i in range(1,n):
   if n%i==0:
        sum+=i
if sum==n:
    print('perfect no')
else:
    print('not perfect')

#printiing sum of integer value from a list

l=[45,56,12,'sa',23,89]
sum=0
for i in l:
    if type(i)==int:
        sum+=i
print(sum)

#printing max value from a list
l=[78,45,56,89,12,57,88]
m=l[0]
for i in l:
    if i>m:
        m=i
print(m)


#for loop use in range and coolection data type  (index position of elements of cdt , multiple elements extraction)

# questions
s='hai python'
for i in range(len(s)):
    if s[i]=='h':
        print(i)


#q2
s='My soulmate is gorgeous'
sum=0
v='aeiouAEIOU'
for i in range(len(s)):
    if s[i] in v:
        sum+=i
print(sum)


#3
s="my soulmate is gorgeous"
sum=0
v='aeiouAEIOU'
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] not in v:
            sum+=i
print(sum)

#4

s="my soulmate is gorgeous"
v='aeiouAEIOU'
c=''
for i in range(len(s)):
    if s[i] in v :
        c+=str(i)
    else:
        c+=s[i]
print(c)

#5
s="my soulmate is gorgeous"
v='aeiouAEIOU'
c=''
for i in range(len(s)):
    if s[i] in v and i%2==0:
        c+=str(i)
    else:
        c+=s[i]
print(c)

#6 for extracting multiple value or elements
s='hai python'
v='hai'
l=len(v)
c=0
for i in range(len(s)-l+1):
    if s[i:i+l:1]==v:
        c+=1
    print(i,s[i:i+l:1])

#modify
s='hai python'
l=int(input('enter a number bet 1 to 5\n'))
k=[]
for i in range(len(s)-l+1):
    k.append(s[i:i+l:1])
print(k)