# Remove '#' before the object and method of the class to access the class

class one: # A
    def m_one(self):
        salary=int(input("Enter the salary : "))
        try:
            if(salary<0):
                raise Exception
            else:
                print(salary)
        except Exception as e:
            print("Exception : Negative value ",e)

class two: # B
    def m_two(self):
        n=int(input("Enter the value for n : "))
        p=int(input("Enter the value for p :"))
        try:
            if(n<=0 or p<=0):
                raise Exception()
            else :
                c=pow(n,p)
                print(c)
        except Exception as e:
            print("Exception ! : Either N or P should not be Negative or Zero",e)
        else:
            print("Calculated : " ,c)

class three: # C
    def m_three(self):
        money=int(input("Enter the value of money : "))
        try:
            if(money>3000):
                raise Exception()
            else:
                print("Money Deposited")
        except:
            print("Exception : You cannot deposite more than 3000")



class four: # D
    def m_four(self):
        age=int(input("Enter the age : "))
        try:
            if(age<=18):
                raise Exception()
            else:
                print("You are eligible for voting")
        except:
            print("Exception : You are not eligible for voting")
            
class five: # E
    def m_five(self):
      
        try:
            a=int(input("Enter the value for a : "))
            b=int(input("Enter a value for b : "))
            c=a/b
            print(c)      
        except Exception as e:
            print("Exception ! :  ",e)
        else:
            print("Executed")

#obj1=one()
#obj2=two()
#obj3=three()
#obj4=four()
#obj5=five()

#obj1.m_one()
#obj2.m_two()
#obj3.m_three()
#obj4.m_four()
#obj5.m_five()

