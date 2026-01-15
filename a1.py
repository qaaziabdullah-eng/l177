try:
    n=int(input("enter a number: "))
    print(n)

except ValueError as e:
    print("exception ",e)

    print("out of exception")