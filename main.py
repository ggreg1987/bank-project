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
    global balance
    if amounts > withdraw_limit or amounts < 0 or withdraw_limit_per_day == 0:
        return "Amount incorrect or limit per day"
    else:
        withdraw_limit_per_day -= 1
        balance -= amounts
        result = f"Draw out R${amounts}"
        extracts.append(result)
        return result


def deposit(amounts) -> str:
    global balance
    global extracts
    if amounts > 0:
        balance += amounts
        result = f"deposited R${amounts}"
        extracts.append(result)
        return result
    else:
        return "Amount incorrect"


def extract():
    for ex in extracts:
        print(ex)


####################################################################################################
def main():
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

main()