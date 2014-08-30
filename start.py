"""
The quiz must be started by calling the main() of this file.
"""

import login
import readqs
import helper
        
def main():
    """
    No doc string should ever be found under a main function.
    """
    print('''Note:
* Press '0' (zero) if you'd like to answer a question later.
* You will not be warned if an incorrect key is entered. Check twice.
* Do not give spaces or tabs when entering any input. Not even at the end or start. It will NOT be ignored as whitespace.
* Pressing the Enter key will be treated as end of input. It will NOT be ignored as whitespace.
* Consider ':' (colon) as a prompt to enter input.
* Ctrl + c terminates the program.
#################################################################
''')
    while True:
        Lno = input("\nNew session (N) or Continue old session (C)?: ")
        if Lno == 'N' or Lno == 'n':
            Lno = True
            break
        elif Lno == 'C' or Lno == 'c':
            Lno = False
            break
        else:
            print('Invalid input\n')
            
##    Lusn -> this file will (or already does) contain the remaining questions and the scores
##    Lfile -> In case its a new session, all questions will be read from the original file, old sess -> Lfile = Lusn
##    Lkey -> 1. Use as password, but why? 2. Encrypt the damn thing... :)
    
    Lusn, Lfile, Lkey = login.main(Lno)
    helper.main(readqs.main(Lfile), Lkey, Lusn, Lno)        

main()
