"""
Do not open or run any file apart from this one.
"""

import sys, os
sys.path.append(os.getcwd())

while True:
    print('0. Exit\n1. Start Test\n2. Set questions manually')
    print('3. Set questions from file')
    Lin = input("Enter choice: ")
    if Lin == '0':
        print("Goodbye!!!")
        break
    elif Lin == '1':
        import start
        start.main()
        break
    elif Lin == '2':
        import generateQfileManually
        generateQfileManually.main()
        break
    elif Lin == '3':
        import generateQfileFromIpFile
        generateQfileFromIpFile.main()
        break
