import time
def main(n):
    a = 0
    for i in text:
        b = ord(i)
        a += b
    return(a)

text = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
text2=text.split()
text3=(len(text2)-1)
text4=(ord(" ")*text3)
start = time.time()
print((main(text)-text4))
print('Time: ',(time.time()-start)*1000)