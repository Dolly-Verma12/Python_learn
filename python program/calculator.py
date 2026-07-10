#CALCULATOR
a=int (input("Enter your number: "))
op=input("Enter operator: ")
b= int(input("Enter your 2nd Number: ")) 
def fn_ct(a,op,b):

     if (op=='*'):  
         print(a*b)
     elif(op=='+'):
        print(a+b)
     elif(op=='-'):
        print(a-b)
     elif(op=='/'):
        print(a/b)
     else:
        print("Please input valid operator!!")
     
fn_ct(a,op,b)





 