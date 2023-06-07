# Example that appends logs to a log file

 

import logging

 

# set the level of loggin to : DEBUG is lowest level; INFO general; WARNING potential problem; ERROR failure; CRITICAL fatal error.

 

# appends log to a logging file

logging.basicConfig(filename='logging_example_log.txt',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.disable()

 

logging.info(f'Logging module is working')

logging.debug('Start of program')

 

def factorial(n):

    logging.debug(f'Start of factorial({n})')

   

    total = 1

    if type(n) not in [int, float]:

        raise TypeError('factorial can only work with integer or float')

    try:

        for i in range(1,n+1):

            total *= i

            logging.debug(f'i is {str(i)}, total is {str(total)}')

    except:

        logging.debug(f'something went wrong')

       

    logging.debug(f'End of factorial({n})')

    return total

 

   

#print(f'factorial({5}) = {factorial(5)}')

logging.debug('End of program')

 