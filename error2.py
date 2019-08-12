import logging

logging.basicConfig(filename="bbbbb.log", level=logging.ERROR)

data= {"1111":10000,"2222":20000 }


logging.debug(data)

class InvalidAccount(Exception):
    pass

class InsufficientFund(Exception):
    pass

def withdraw(accNo, amount):
    logging.info(" withdraw function -start")
    if accNo not in data:
        logging.debug( "Account Number is "+ accNo)
        raise InvalidAccount()

    if amount > data[accNo] :
        logging.debug("Amout is " + accNo)
        raise InsufficientFund()

    data[accNo] = data[accNo]- amount
    logging.info(" withdraw function -end")



def main ():
    try :
        accNo = input("Account Number ::")
        amount = int (input("amount"))
        withdraw(accNo,amount)
    except InvalidAccount as e:
        logging.exception(e)
    except InsufficientFund  as e:
        logging.exception(e)
        print ()
    except ValueError  as e:
        logging.exception(e)
    except Exception as e :
        logging.exception(e)
    else :
        pass
    finally:
        pass

main()