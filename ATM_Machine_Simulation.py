import time

# Credit/Debit card insertion process
print("Please insert your debit/credit card: ")
print("........................................")
time.sleep(5)
print("Card inserted successfully")
print("........................................")
print("Please wait... ")
print("........................................")
time.sleep(2)

# Variables
password = 1234  # Card PIN
pin = int(input("Enter Your debit/credit Card PIN: "))  # Get PIN from user
balance = 5000  # Pre loaded balance
transactions = []  # Record transaction history in the list

# Function to check if the PIN is valid (4 digits and numeric)
def is_valid_pin(pin):
    return len(pin) == 4 and pin.isdigit()

# All Functions
if pin == password:
    while True:
        print("""
              1 : Account balance inquiry
              2 : Cash Withdrawal
              3 : Cash deposit
              4 : Transaction history
              5 : Pin Change
              6 : Exit
              """)
        try:
            option = int(input("Select any one of the following (e.g., 1, 2, 3, 4, 5, 6): "))
        except ValueError:
            print("Please enter a valid option")
            continue

        # Balance inquiry process
        if option == 1:
            balance_inquiry_pin = int(input("Enter your debit/credit card PIN: "))
            if balance_inquiry_pin == password:
                print(f"Your account balance is {balance}")
            else:
                print("Please enter the correct PIN")

        # Amount withdrawal process
        elif option == 2:
            withdrawal_amount = int(input("Enter withdrawal amount: "))
            withdrawal_pin = int(input("Enter your debit/credit card PIN: "))
            if withdrawal_pin == password:
                if withdrawal_amount <= balance:
                    balance -= withdrawal_amount
                    transactions.append(f"Withdrawn: {withdrawal_amount}")
                    print("Please collect your cash and card")
                    time.sleep(3)
                    print(f"Your Account has debited {withdrawal_amount}")
                    check_balance = input("Enter 'B' for view current balance: ")
                    if check_balance == 'B' or check_balance == 'b':
                        print(f"Your Account Balance is {balance} After Withdrawal {withdrawal_amount}")
                    else:
                        print("Incorrect Choice!")
                else:
                    print("Insufficient Balance")
            else:
                print("Please enter the correct PIN")
            break

        # Amount deposit process
        elif option == 3:
            print("Please insert your cash in the cash tray")
            time.sleep(3)
            print("Please wait.. Your cash is calculating")
            time.sleep(5)
            deposit_amount = int(input("Enter Amount For Deposit (max 20000): "))
            if deposit_amount <= 20000:
                deposit_pin = int(input("Enter your debit/credit card PIN: "))
                if deposit_pin == password:
                    balance += deposit_amount
                    transactions.append(f"Deposited: {deposit_amount}")
                    print(f"{deposit_amount} is credited in your account")
                    print(f"Your Current Balance is {balance}")
                else:
                    print("Please enter the correct PIN")
            else:
                print("Deposit limit exceeded. Maximum deposit is 20000.")

        # Check transaction history
        elif option == 4:
            print("Transaction History:")
            for transaction in transactions:
                print(transaction)

        # Credit/Debit card pin change process
        elif option == 5:
            old_pin = int(input("Enter the old PIN: "))
            if old_pin == password:
                new_pin = input("Enter New PIN: ")
                confirm_pin = input("Confirm New PIN: ")
                if new_pin == confirm_pin:
                    if is_valid_pin(new_pin):
                        if int(new_pin) == password:
                            print("Previous password and new password should not be the same!")
                        else:
                            password = int(new_pin)
                            print("PIN Changed Successfully")
                    else:
                        print("PIN must be 4 digits and numeric")
                else:
                    print("New PIN and confirm PIN do not match")
            else:
                print("Incorrect old PIN")

        # Break the process
        elif option == 6:
            print("Please collect your card")
            break
else:
    print("Please enter the correct PIN")