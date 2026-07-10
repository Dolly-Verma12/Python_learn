class InvaildPassError(Exception):
    pass
password=input("Enter 8 digit password: ")
try:
    if not password.isdigit():
        raise InvaildPassError("password contain only digit")
    if len(password)!=8:
       raise InvaildPassError("password must be 8 digit")
except InvaildPassError as e:
    print(e) 
except ValueError:
    print("Invalid data type")    
else:
    print("atm")
