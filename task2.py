#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0

    def __init__(self,P=0,r=0,n=0):
        self.principal = P
        self.rate = r/100
        self.nPeriods = n
        #more input parameters needed

    def interest(self,t):
        return self.principal*(1+self.rate/self.nPeriods)**self.nPeriods*t - self.principal
    
    def amount(self,t):
        return self.principal*(1+self.rate/self.nPeriods)**self.nPeriods*t

a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

