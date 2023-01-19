def main():
    n=int(input("Digite o valor de n: "))
    num=1
    while n>0:
        if num%2==1:
           print(num) 
           n-=1
        num+=1
        
main()