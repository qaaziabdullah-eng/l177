try:
    n1=int(input("enter first number: "))
    n2=int(input("enter second number: "))
    result=n1/n2
    print("result: ",result)
    print("result2",result2)

except ZeroDivisionError:
    print("enter only integer value")

except ValueError:
    print("enter only integer value")

except NameError:
    print("Variable result2 is not defined") 

except Exception as e:
    print("Exception occurred: ",e)

finally:
    print("finally block executed")
