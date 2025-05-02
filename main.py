def main():
    print("hello, world")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def steps(n):
    if n==1 or n==2:
        return n
    return steps(n-2) + steps(n-1)

if __name__ == "__main__":
    main()
    print("Factorial:",factorial(10))
    print("Steps:",steps(10))