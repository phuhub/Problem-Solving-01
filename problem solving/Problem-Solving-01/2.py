import time
def one (n):
    a = 0
    for i in text2[0]:
        result=ord(i)
        a += result
    return(a)
def two (n):
    a = 0
    for i in text2[1]:
        result=ord(i)
        a += result
    return(a)
def three (n):
    a = 0
    for i in text2[2]:
        result=ord(i)
        a += result
    return(a)
def four (n):
    a = 0
    for i in text2[3]:
        result=ord(i)
        a += result
    return(a)
def five (n):
    a = 0
    for i in text2[4]:
        result=ord(i)
        a += result
    return(a)
def six (n):
    a = 0
    for i in text2[5]:
        result=ord(i)
        a += result
    return(a)
def seven (n):
    a = 0
    for i in text2[6]:
        result=ord(i)
        a += result
    return(a)
def eight (n):
    a = 0
    for i in text2[7]:
        result=ord(i)
        a += result
    return(a)
def nine (n):
    a = 0
    for i in text2[8]:
        result=ord(i)
        a += result
    return(a)

text="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
text2=text.split()
start = time.time()
print(one(text)+two(text)+three(text)+four(text)+five(text)+six(text)+seven(text)+eight(text)+nine(text))
print('Time: ',(time.time()-start)*1000)
