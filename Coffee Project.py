class CoffeeMachine:
    def __init__(self):
        self.water_available = 400
        self.milk_available = 540
        self.beans_available = 120
        self.cups_available = 9
        self.money = 550
        self.water_top_up = 0
        self.milk_top_up = 0
        self.beans_top_up = 0
        self.cups_top_up = 0
        self.action = None
        self.coffee_option = None

    def input_action(self):
        print("Write action (buy, fill, take):")
        self.action = str(input())
        if self.action == "exit":
            quit()
        elif self.action == "buy":
            self.buy_action()
        elif self.action == "fill":
            self.fill_action()
        elif self.action == "take":
            self.take_action()
        elif self.action == "remaining":
            self.remaining_action()

    def buy_action(self):
        self.coffee_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if self.coffee_option == 'back':
            self.input_action()
        if self.coffee_option == '1':
            self.money += 4
            self.water_available -= 250
            self.beans_available -= 16
            self.cups_available -= 1
            if self.water_available < 0 or self.beans_available < 0 or self.cups_available < 0:
                print("There are not enough resources to make this coffee")
                self.money -= 4
                self.water_available += 250
                self.beans_available += 16
                self.cups_available += 1
                self.input_action()
            else:
                print("Making you a espresso")
            self.input_action()
        elif self.coffee_option == '2':
            self.money += 7
            self.water_available -= 350
            self.milk_available -= 75
            self.beans_available -= 20
            self.cups_available -= 1
            if self.water_available < 0 or self.beans_available < 0 or self.cups_available < 0:
                print("There are not enough resources to make this coffee")
                self.money -= 7
                self.water_available += 350
                self.milk_available += 75
                self.beans_available += 20
                self.cups_available += 1
                self.input_action()
            else:
                print("Making you a latte")
            self.input_action()
        elif self.coffee_option == '3':
            self.money += 6
            self.water_available -= 200
            self.milk_available -= 100
            self.beans_available -= 12
            self.cups_available -= 1
            if self.water_available < 0 or self.beans_available < 0 or self.cups_available < 0:
                print("There are not enough resources to make this coffee")
                self.money -= 6
                self.water_available += 200
                self.milk_available += 100
                self.beans_available += 12
                self.cups_available += 1  
                self.input_action()
            else:
                print("Making you a cappuccino")
            self.input_action()
        elif self.buy_input():
            self.input_action()
        else:
            self.input_action()
    
    def fill_action(self):
        self.water_top_up = int(input("Write how many ml of water do you want to add:"))
        self.water_available += self.water_top_up
        self.milk_top_up = int(input("Write how many ml of milk do you want to add:"))
        self.milk_available += self.milk_top_up
        self.beans_top_up = int(input("Write how many grams of coffee beans do you want to add:"))
        self.beans_available += self.beans_top_up
        self.cups_top_up = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups_available += self.cups_top_up
        print("Coffee Machine has been topped up")
        self.input_action()

    def take_action(self):
        print("I gave you $", self.money)
        self.money *= 0
        self.input_action()

    def remaining_action(self):
        print("The coffee machine has:")
        print(self.water_available, "of water")
        print(self.milk_available, "of milk")
        print(self.beans_available, "of coffee beans")
        print(self.cups_available, "of disposable cups")
        print(self.money, "of money")    
        self.input_action()

run = CoffeeMachine() 
run.input_action() 
