class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, d_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.d_cups = d_cups
        self.money = money


class Espresso:
    def __init__(self, price, water, milk, coffee_beans, d_cups):
        self.price = price
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.d_cups = d_cups


class Latte:
    def __init__(self, price, water, milk, coffee_beans, d_cups):
        self.price = price
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.d_cups = d_cups


class Cappuccino:
    def __init__(self, price, water, milk, coffee_beans, d_cups):
        self.price = price
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.d_cups = d_cups


cm = CoffeeMachine(100, 100, 100, 10, 0)

e = Espresso(40, 20, 0, 20, 1)
l = Latte(50, 20, 40, 20, 1)
c = Cappuccino(60, 20, 30, 20, 1)


while True:
    command = input(
        "\nEnter command: buy / remaining / take / fill / exit: "
    ).lower()

    if command == "buy":

        user_choice = int(
            input("Choose: 1.Espresso 2.Latte 3.Cappuccino: ")
        )

        if user_choice == 1:
            selected_coffee = e
        elif user_choice == 2:
            selected_coffee = l
        elif user_choice == 3:
            selected_coffee = c
        else:
            print("Choose correct number")
            continue

        # Check resources
        if cm.water < selected_coffee.water:
            print("Not enough water")

        elif cm.milk < selected_coffee.milk:
            print("Not enough milk")

        elif cm.coffee_beans < selected_coffee.coffee_beans:
            print("Not enough coffee beans")

        elif cm.d_cups < selected_coffee.d_cups:
            print("Not enough cups")

        else:
            print("Enough resources")

            # Payment
            pay = int(input("Enter the payment amount: "))

            if pay < selected_coffee.price:
                print("Payment is insufficient")
            else:
                change = pay - selected_coffee.price

                cm.money = cm.money + selected_coffee.price

                cm.milk = cm.milk - selected_coffee.milk
                cm.d_cups = cm.d_cups - selected_coffee.d_cups
                cm.water = cm.water - selected_coffee.water
                cm.coffee_beans = (
                    cm.coffee_beans - selected_coffee.coffee_beans
                )

                print("Change:", change)

                if user_choice == 1:
                    print("Espresso is ready")
                elif user_choice == 2:
                    print("Latte is ready")
                elif user_choice == 3:
                    print("Cappuccino is ready")


    elif command == "remaining":

        print("Water:", cm.water)
        print("Milk:", cm.milk)
        print("Coffee beans:", cm.coffee_beans)
        print("Cups:", cm.d_cups)
        print("Money:", cm.money)


    elif command == "take":

        print("Money taken:", cm.money)
        cm.money = 0


    elif command == "fill":

        water = int(input("Add water: "))
        milk = int(input("Add milk: "))
        coffee_beans = int(input("Add coffee beans: "))
        cups = int(input("Add cups: "))

        cm.water += water
        cm.milk += milk
        cm.coffee_beans += coffee_beans
        cm.d_cups += cups

        print("Machine filled successfully")


    elif command == "exit":

        print("Machine turned off.")
        break


    else:

        print("Invalid command")