def primos (x):
    i=0
    primos2=0
    while primos2<x:
        i+=1
        div=0
        for j in range(1, i+1):
            if i%j==0:
                div+=1
        if div==2:
            print(i)
            primos2+=1
def main():        
    x=int(input())
    primos(x)
main()