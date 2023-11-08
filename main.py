name = input("What's your name?\n")

balance = 0
withdraw_limit = 500
withdraw_limit_per_day = 3
extract = []


def wellcome() -> str:
    return f"""
    ************Wellcome to the DIO's Bank {name.title()}*************
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
    if 0 > amount > withdraw_limit:
        return "Amount incorrect"
    else:
        balance - amount
        result = f"Draw out R${amount}"
        extract.append(result)
        return result

