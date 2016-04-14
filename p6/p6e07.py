class Lunch:
    def __init__(self):
        self.cst = Customer()
        self.empl = Employee()

    def order(self, foodName='Sushi'):
        print('Please make an order.')
        self.cst.placeOrder(self.empl, foodName)
    def result(self):
        print('How is your food?')
        self.cst.printFood()


class Customer:
    def __init__(self):
        self.food = None
    def placeOrder(self, employee, foodName):
        print('I\'ll have %s.' % foodName)
        self.food = employee.takeOrder(foodName)
        print('Thank your for the %s.' % self.food.fdname)
    def printFood(self):
        print('The %s is fine, thanks.' % self.food.fdname) 

class Employee:
    def takeOrder(self, foodName):
        print('I\'ll bring your %s in a minute.' % foodName)
        return Food(foodName)
        print('Here is your %s.' % food.fdname)

class Food:
    def __init__(self, name):
        self.fdname = name

if __name__ == '__main__':
    lu = Lunch()

    lu.order()
    lu.result()

    lu.order('Tempura')
    lu.result()
