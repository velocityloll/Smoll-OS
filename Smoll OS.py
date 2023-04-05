import time

selusername = input("undefined @DESKTOP: Create a Username: ")
selpassword = input("undefined @DESKTOP: Create a Password: ")
loggedon = False
commands = ['exit', 'info', 'sudo']

username = input("Username: ")

if username == selusername:
    password = input("Password: ")
    if password == selpassword:
        print(selusername, "@DESKTOP: You have logged into the account: ", username)
        loggedon = True
    else:
        print("Incorrect Password!")
        password = input("Password: ")
        if password == selpassword:
            print(selusername, "@DESKTOP: You have logged into the account: ", username)
            loggedon = True
        else:
            print("Incorrect Password!")
            password = input("Password: ")
            if password == selpassword:
                print(selusername, "@DESKTOP: You have logged into the account: ", username)
                loggedon = True
            else:
                print("Too many attempts!")
else:
    print("Incorrect Username!")
    username = input("Username: ")
    if username == selusername:
        password = input("Password: ")
        if password == selpassword:
            print(selusername, "@DESKTOP: You have logged into the account: ", username)
            loggedon = True
        else:
            print("Incorrect Password!")
            password = input("Password: ")
            if password == selpassword:
                print(selusername, "@DESKTOP: You have logged into the account: ", username)
                loggedon = True
            else:
                print("Incorrect Password!")
                password = input("Password: ")
                if password == selpassword:
                    print(selusername, "@DESKTOP: You have logged into the account: ", username)
                    loggedon = True
                else:
                    print("Too many attempts!")
    else:
        print("Incorrect Username!")
        username = input("Username: ")
        if username == selusername:
            password = input("Password: ")
            if password == selpassword:
                print(selusername, "@DESKTOP: You have logged into the account: ", username)
                loggedon = True
            else:
                print("Incorrect Password!")
                password = input("Password: ")
                if password == selpassword:
                    print(selusername, "@DESKTOP: You have logged into the account: ", username)
                    loggedon = True
                else:
                    print("Incorrect Password!")
                    password = input("Password: ")
                    if password == selpassword:
                        print(selusername, "@DESKTOP: You have logged into the account: ", username)
                        loggedon = True
                    else:
                        print("Too many attempts!")
        else:
            print("Incorrect Username!")
            username = input("Username: ")
            if username == selusername:
                password = input("Password: ")
                if password == selpassword:
                    print(selusername, "@DESKTOP: You have logged into the account: ", username)
                    loggedon = True
                else:
                    print("Incorrect Password!")
                    password = input("Password: ")
                    if password == selpassword:
                        print(selusername, "@DESKTOP: You have logged into the account: ", username)
                        loggedon = True
                    else:
                        print("Incorrect Password!")
                        password = input("Password: ")
                        if password == selpassword:
                            print(selusername, "@DESKTOP: You have logged into the account: ", username)
                            loggedon = True
                        else:
                            print("Too many attempts!")

if loggedon == True:
    command = input(">>> ")
    if command == "exit":
        print(username, "@DESKTOP: Shutting down...")
        print("0% [**********]")
        time.sleep(0.1)
        print("10% [#*********]")
        time.sleep(0.1)
        print("20% [##********]")
        time.sleep(0.1)
        print("30% [###*******]")
        time.sleep(0.1)
        print("40% [####******]")
        time.sleep(0.1)
        print("50% [#####*****]")
        time.sleep(0.1)
        print("60% [######****]")
        time.sleep(0.1)
        print("70% [#######***]")
        time.sleep(0.1)
        print("80% [########**]")
        time.sleep(0.1)
        print("90% [#########*]")
        time.sleep(0.1)
        print("100% [##########]")
        time.sleep(0.1)
        print(username, "@DESKTOP: Shut down successful.")
        command = input(">>> ")
        if command == "exit":
            print(username, "@DESKTOP: Shutting down...")
            print("0% [**********]")
            time.sleep(0.1)
            print("10% [#*********]")
            time.sleep(0.1)
            print("20% [##********]")
            time.sleep(0.1)
            print("30% [###*******]")
            time.sleep(0.1)
            print("40% [####******]")
            time.sleep(0.1)
            print("50% [#####*****]")
            time.sleep(0.1)
            print("60% [######****]")
            time.sleep(0.1)
            print("70% [#######***]")
            time.sleep(0.1)
            print("80% [########**]")
            time.sleep(0.1)
            print("90% [#########*]")
            time.sleep(0.1)
            print("100% [##########]")
            time.sleep(0.1)
            print(username, "@DESKTOP: Shut down successful.")
            command = input(">>> ")
        else:
            if command == "help":
                print("All commands avaliable:")
                print(commands)
            else:
                if command == "sudo":
                    print(username, "@sudo: You do not have permission to use this command!")
        
    else:
        if command == "help":
            print("All commands avaliable:")
            print(commands)
            command = input(">>> ")
            if command == "exit":
                print(username, "@DESKTOP: Shutting down...")
                print("0% [**********]")
                time.sleep(0.1)
                print("10% [#*********]")
                time.sleep(0.1)
                print("20% [##********]")
                time.sleep(0.1)
                print("30% [###*******]")
                time.sleep(0.1)
                print("40% [####******]")
                time.sleep(0.1)
                print("50% [#####*****]")
                time.sleep(0.1)
                print("60% [######****]")
                time.sleep(0.1)
                print("70% [#######***]")
                time.sleep(0.1)
                print("80% [########**]")
                time.sleep(0.1)
                print("90% [#########*]")
                time.sleep(0.1)
                print("100% [##########]")
                time.sleep(0.1)
                print(username, "@DESKTOP: Shut down successful.")
                command = input(">>> ")
            else:
                if command == "help":
                    print("All commands avaliable:")
                    print(commands)
                else:
                    if command == "sudo":
                        print(username, "@sudo: You do not have permission to use this command!")
        else:
            if command == "sudo":
                print(username, "@sudo: You do not have permission to use this command!")
                command = input(">>> ")
                if command == "exit":
                    print(username, "@DESKTOP: Shutting down...")
                    print("0% [**********]")
                    time.sleep(0.1)
                    print("10% [#*********]")
                    time.sleep(0.1)
                    print("20% [##********]")
                    time.sleep(0.1)
                    print("30% [###*******]")
                    time.sleep(0.1)
                    print("40% [####******]")
                    time.sleep(0.1)
                    print("50% [#####*****]")
                    time.sleep(0.1)
                    print("60% [######****]")
                    time.sleep(0.1)
                    print("70% [#######***]")
                    time.sleep(0.1)
                    print("80% [########**]")
                    time.sleep(0.1)
                    print("90% [#########*]")
                    time.sleep(0.1)
                    print("100% [##########]")
                    time.sleep(0.1)
                    print(username, "@DESKTOP: Shut down successful.")
                    command = input(">>> ")
                else:
                    if command == "help":
                        print("All commands avaliable:")
                        print(commands)
                    else:
                        if command == "sudo":
                            print(username, "@sudo: You do not have permission to use this command!")