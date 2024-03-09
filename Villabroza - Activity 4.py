class Employee:
    def __init__(self, name, gender, birthdate, position, rate, dayswork):
        # Initializes the Employee object with provided attributes
        self.__name = name
        self.__gender = gender
        self.__birthdate = birthdate
        self.__position = position
        self.__rate = rate
        self.__dayswork = dayswork
        
    # Getters for each attribute
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_birthdate(self):
        return self.__birthdate

    def get_position(self):
        return self.__position

    def get_rate(self):
        return self.__rate

    def get_dayswork(self):
        return self.__dayswork
    
    # Setters for each attribute
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate
       

    def set_position(self, position):
        self.__position = position

    def set_rate(self, rate):
        self.__rate = rate

    def set_dayswork(self, dayswork):
        self.__dayswork = dayswork
    
    # Calculates gross salary
    def get_gross(self):
        gross = self.__dayswork * self.__rate
        return gross

    # Calculates SSS deduction based on gross salary
    def get_sss(self):
        gross = self.get_gross()
        if gross < 10000:
            sss = 0
        elif 10000 <= gross <= 20000:
            sss = 1000
        else:
            sss = 1500
        return sss

    # Calculates tax deduction based on gross salary
    def get_tax(self):
        gross = self.get_gross()
        if gross < 10000:
            tax = 0
        elif 10000 <= gross < 20000:
            tax = 0.10 * gross
        elif 20000 <= gross <= 30000:
            tax = 0.20 * gross 
        else:
            tax = 0.25 * gross
        return tax

    # Calculates net salary after deductions
    def get_net_salary(self):
        gross = self.get_gross()
        sss = self.get_sss()
        tax = self.get_tax()
        net = gross - sss - tax
        return net
    
    # Prints employee details including salary information
    def get_employee_details(self):
        print()
        print("Employee Details: ")
        print()
        print("Name:", self.get_name())
        print("Gender:", self.get_gender())
        print("Birth Date:", self.get_birthdate())
        print("Position:", self.get_position())
        print()
        print("Salary Details: ")
        print()
        print("Gross Salary: P ", "{:,.2f}".format(self.get_gross()), sep='')
        print("SSS: P ", "{:,.2f}".format(self.get_sss()), sep='')
        print("Tax: P ", "{:,.2f}".format(self.get_tax()), sep='')
        print("Net Salary: P ", "{:,.2f}".format(self.get_net_salary()), sep='')

def main():
    # Takes input for employee details
    name = input("Enter Employee Name: ")
    gender = input("Enter Gender (M/F): ")
    birthdate = input("Enter Birth Date: ")
    position = input("Enter Position: ")
    rate = float(input("Enter Rate per day: "))
    dayswork = int(input("Enter Days Work: "))

    # Creates Employee object with provided details and displays employee details
    employee = Employee(name, gender, birthdate, position, rate, dayswork)
    employee.get_employee_details()

if __name__ == "__main__":
    main()