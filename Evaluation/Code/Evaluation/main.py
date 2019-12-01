from evaluationManager import *
from config import execution_mode

if __name__ == '__main__':

    if execution_mode == 1:
        run()
    elif execution_mode == 2:
        debug()
    else:
        print("Unspported execution mode")
