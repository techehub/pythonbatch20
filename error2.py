import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)

data= {"1111":10000,"2222":20000 }


logging.debug(data)

class InvalidAccount(Exception):
    pass

class InsufficientFund(Exception):
    pass

def withdraw(accNo, amount):
    logging.info("111111")
    if accNo not in data:
        logging.debug("111111")
        raise InvalidAccount()

    if amount > data[accNo] :
        logging.debug("22222")
        raise InsufficientFund()

    data[accNo] = data[accNo]- amount


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