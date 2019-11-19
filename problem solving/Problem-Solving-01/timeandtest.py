import time
def Sequencesv1(n):
    total=0
    for i in range (n):
        total += (i+1)
    return(total)
n=int(input("Input Values : "))
start= time.time()
print("answer :",Sequencesv1(n))
print("Time : ",(time.time()-start)*1000)