num=int(input("Enter your 1st number: "))
num2=int(input("Enter your 2nd number: "))
try:

    ans=num/num2
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("2nd number Cannot be zero")
else:
    print("Answer is : ",ans)
finally:
    print("Thank you!!")
    