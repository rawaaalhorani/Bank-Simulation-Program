### Bank Simulation Program Project ###
username="admin"
password="123456"
attempts= 3
while attempts > 0 :
    user=input("Enter username: ")
    pas=input("Enter password: ")
    if user == username and pas == password :
        print("Access")
        break
    else:
        attempts-=1 
        print("wrong username or password")   
if attempts == 0 :
    print("Locked")
    exit()

balance = float(input("Enter your balance: "))

while True:

    print("\n--- Bank Menu ---") 
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful.")
            print("Your new balance is:", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Your new balance is:", balance)
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == 4:
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice.")