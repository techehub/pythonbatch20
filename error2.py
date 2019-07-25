data= {"1111":10000,"2222":20000 }

class InvalidAccount(Exception):
    pass

class InsufficientFund(Exception):
    pass

def withdraw(accNo, amount):
    if accNo not in data:
        raise InvalidAccount()
    if amount > data[accNo] :
        raise InsufficientFund()

    data[accNo] = data[accNo]- amount


def main ():
    try :
        accNo = input("Account Number ::")
        amount = int (input("amount"))
        withdraw(accNo,amount)

    except InvalidAccount:
        print ()

    except InsufficientFund:
        print ()

    except ValueError:
        print ()

    except Exception:
        print ()

main()