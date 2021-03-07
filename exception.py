class InvalidLengthException (Exception):
    pass
class Mobile:
    def __init__ (self,mob_no):
        self.__mob_no=mob_no
    def validate_mobile_number(self):
        try:
            if(len(self.__mob_no)!=10):
                raise InvalidLengthException
            else:
                print("Valid Mobile Number")
        except InvalidLengthException:
            print("Invalid Length inside class")
        print("Inside the class")
mob=Mobile("987665")
try:
    mob.validate_mobile_number()
    print("Outside the class")
except InvalidLengthException:
    print("Invalid Length - outside class")
