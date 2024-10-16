"""
Looping Statements
===================
when we have some set of instruction to execute repeatedly we will go for looping statements.
we have 2 types of looping statements.
1. for loop
2. while loop

1.for loop
-----------------
when we know how many time we will iterate our programm.
we will use for loop.
for loop will perform based on some rules that
   1st Initializing
   2nd traversing

for loop can perform two ways that 
with collection data type
with range() function


"""

# for loop with collection data type
fruits = ['apple', 'banana', 'cherry']
for var in fruits:
    print(var)
print('for list')


s='sasank sekhar baral' 
for i in s:
    print(i)
print('for string')


t=(78,45,56,23)
for i in t:
    print(i)
print('for tuple')



st={78,89,45,56,12}
for i in st:
    print(i)
print('for set')

d={'name':'sasank','age':24,'gender':'male'}
for i in d:
    print(i,d[i])
    
print('for dictionary')

#printing how many elements are present in a given string.
strr=input('Enter a string\n')
count=0
for i in strr:
    count+=1
print("counting of string is  ", count)

#printing how many time given substring is present in given string
string=input('Enter any string\n')
sub=input('choose a charector from given string\n')
count=0
for i in string:
    if i == sub:
        count+=1
print('Repeated Given Substring is',count)

#printing how many vowels are present in a given string
var='printing how many vowels are present in a given string'
vowels='aeiouAEIOU'
count=0
for i in var:
    if i.isalpha():
        if i in vowels:
            count+=1
print('vowels are ',count)

#printing how many consonants are presents in given string

vars="I stopped eating unhealthy food via identity change"
vowels='aeiouAEIOU'
count=0
for i in vars:
    if i.isalpha():
        if i not in vowels:
            count+=1
print(count)


#printing how many digits are presents in given string

s='someth5ing i6s bet1ter th7an no2thing'
count=0
for i in s:
    if i.isdigit():
        count+=1
print(count)



# printing how many word is present in a given string
v='something is better than nothong'
word=v.split()
count=0
for i in word:
    count+=1
print(count)



#printing how many times given word is present in a given string.
v='''
I recently stopped smoking and the difference between
 I don’t smoke and I can’t smoke is a powerful trainer of my brain.
   The positive message of I don’t smoke is that I have not “given up” anything. 
   I am not sacrificing a pleasure. 
   I am investing in my future happiness and wellbeing.
   '''
lis=v.split()
word='smoke'
count=0
for i in lis:
    if i==word:
        count+=1
print(count)


#printing sum of digits present in given string
s='someth5ing i6s bet1ter th7an no2thing'
sum=0
for i in s:
    if i.isdigit():
        sum+=int(i)
print(sum)


#printing sum of given even number are present in given string

s='someth5ing i6s bet1ter th7an no2thing'
sum=0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            sum+=int(i)
print(sum)


#printing sum of ood number are present in given string

s='someth5ing i6s bet1ter th7an no2thing'
sum=0
for i in s:
    if i.isdigit():
        if int(i)%2!=0:
            sum+=int(i)
print(sum)



s='I Love My Soulmate'
#o/p is Soulmate My Love I
l=s.split()
rev=l[::-1]
print(' '.join(rev))


s='I Love My Soulmate'
#o/p is  I evoL yM etamluoS
Lis=s.split()
l=[]
for i in Lis:
    rev=i[::-1]
    l.append(rev)
print(' '.join(l))


s='I Love My Soulmate'
#o/p is etamluoS yM  evoL I

li=s.split()
rev=li[::-1]
l=[]
for i in rev:
    k=i[::-1]
    l.append(k)
print(' '.join(l))

