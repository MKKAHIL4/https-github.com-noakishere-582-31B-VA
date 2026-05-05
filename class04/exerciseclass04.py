


# write a class  of employee
# class attributes is bonus = 0.25

# instance atrributes are:
# #name
# #sales count
# write a method that claculates their salary returns it 
#  condition if sales are over 10-> give bonus multiplier per sales
# bonus salary is 500

# do this in python beginner friendly way 

class Employee:\
    #class attribute
    base_salary = 500
    company_name = "whatever"
    bonus = 0.25
    
    def __init__(self, name, sales_count):
        #instance atrributes
        self.name = name
        self.sales_count = sales_count
        
    def calculate_salary(self):
        salary = self.base_salary
        base_salary = 500
        
        #condition if
        if self.sales_count > 10:
            bonus_amount = base_salary * Employee.bonus * self.sales_count
            total_salary = base_salary + bonus_amount
        else:
            total_salary = base_salary
        
        return total_salary
    
emp1= Employee("micheal", 5)
emp2 = Employee("sarah", 12)

print(emp1.name, emp1.calculate_salary())
print(emp2.name, emp2.calculate_salary())