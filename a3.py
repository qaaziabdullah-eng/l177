try:
    age=int(input("enter a age"))
    if age<18:
        raise ValueError
    else:
        print("Valid age")
except ValueError:
  print("Inalid age")