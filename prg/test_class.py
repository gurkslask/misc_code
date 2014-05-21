#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      alexander.svensson
#
# Created:     02-08-2013
# Copyright:   (c) alexander.svensson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)




def main():
    "This would create first object of Employee class"
    emp1 = Employee("Zara", 2000)
    "This would create second object of Employee class"
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp1.displayCount()





if __name__ == '__main__':
    main()
