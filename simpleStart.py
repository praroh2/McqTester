"""
Do not open or run any file apart from this one.
"""

import sys, os
sys.path.append(os.getcwd())
## Do not delete these two lines of code.
## It is required to access help() easily. (For dev only)

if __name__ == "__main__":
    while True:
        print('0. Exit\n1. Start Test\n2. Set questions manually')
        print('3. Set questions from file')
        Lin = input("Enter choice: ")
        if Lin == '0':
            print("Goodbye!!!")
            break
        elif Lin == '1':
            import tester
            tester.main()
            break
        elif Lin == '2':
            import generateQfileManually
            generateQfileManually.main()
            break
        elif Lin == '3':
            import generateQfileFromIpFile
            generateQfileFromIpFile.main()
            break
