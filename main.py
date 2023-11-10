import main

balance = 0
withdraw_limit = 500
withdraw_limit_per_day = 3
extracts = []


def wellcome() -> str:
    return """
    ************Wellcome to the DIO's Bank*************
    """


def menu() -> str:
    return """
    ######Choose an Option######
    
    [1] - Withdraw
    [2] - Deposit
    [3] - Extract
    [4] - Exit
    """


def withdraw(amounts) -> str:
    global withdraw_limit
    global withdraw_limit_per_day
    if withdraw_limit < amounts < 0 < withdraw_limit_per_day:
        return "Amount incorrect"
    else:
        withdraw_limit_per_day -= 1
        balance -= amount
        result = f"Draw out R${amounts}"
        extracts.append(result)
        return result


def deposit(amounts) -> str:
    global balance
    if amount > 0:
        balance += amount
        result = f"deposited R${amounts}"
        extracts.append(result)
        return result
    else:
        return "Amount incorrect"


def extract():
    for ex in extracts:
        print(ex)


####################################################################################################
print(wellcome())
print(menu())
number = 0

while number != 4:
    number = int(input())

    if number == 1:
        amount = int(input("How much you will withdraw?\n"))
        print(withdraw(amount))

    elif number == 2:
        amount = int(input("How much you will deposit?\n"))
        print(deposit(amount))

    elif number == 3:
        extract()

    elif number == 4:
        print("Thanks you to use DIO's Bank!!")
        break

    else:
        print("Incorrect Option")

    print(menu())
