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
    [0] - Exit
    """


def withdraw(amount) -> str:
    if main.withdraw_limit < amount < 0 < main.withdraw_limit_per_day:
        return "Amount incorrect"
    else:
        main.withdraw_limit_per_day -= 1
        main.balance -= amount
        result = f"Draw out R${amount}"
        extracts.append(result)
        return result


def deposit(amount) -> str:
    if amount > 0:
        main.balance += amount
        result = f"deposited R${amount}"
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
number = int(input())

while number != 0:

    match number:
        case 1:
            amount = int(input("How much you will withdraw?\n"))
            print(withdraw(amount))
            break

        case 2:
            amount = int(input("How much you will deposit?\n"))
            print(deposit(amount))
            break

        case 3:
            extract()
            break

        case 0:
            print("Thank you for use DIO's Bank!!")
            number = 0

        case _:
            print("Option incorrect")
            break
