def main():
    num=int(input("Entre com o número\n"))
    if num%5==0 and num%3==0:
        print("FizzBuzz")
    else:
        print(num)
main()