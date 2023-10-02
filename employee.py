"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary, hours, rate,contracts, contractsRate, bonusCommision):
        self.name = name
        self.mPay = monthlySalary
        self.hours = hours
        self.rate = rate
        self.contracts = contracts 
        self.cRate = contractsRate
        self.bCommision = bonusCommision

    def get_pay(self):
        return self.mPay + (self.hours*self.rate) + (self.contracts*self.cRate) + self.bCommision
        
    def __str__(self):
        statement = self.name
        monthlyStatement = " works on a monthly salary of "+ str(self.mPay)
        contractStatement = " works on a contract of " + str(self.hours) + " hours at " + str(self.rate) + "/hour"
        commisionStatement = " and recieves a commision for " + str(self.contracts) +  "contract(s) at " + str(self.cRate) + "/contract. "
        bonusCommisionStatement = " and recieves a bonus commision of " + str(self.bCommision) + "."
        totalPayStatement = " Their total pay is "  +str(self.get_pay())

        if self.mPay != 0:
            statement += monthlyStatement
        if self.hours != 0:
            statement += contractStatement
        if self.contracts != 0:
            statement += commisionStatement
        if self.bCommision != 0:
            statement += bonusCommisionStatement
        statement += totalPayStatement
        return statement
        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,0,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,100,25,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,0,4,200,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,150,25,3,220,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,0,0,0,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,120,30,0,0,600)
