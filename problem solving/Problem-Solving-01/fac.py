def fac(N):
    if N > 1 :
        factorial=N*fac(N-1)
    else:
        factorial=1
    return(factorial)
def main ():
    global N
    N=int(input('Enter N : ')) 
    fac(N)
    print(fac(N))
main()

