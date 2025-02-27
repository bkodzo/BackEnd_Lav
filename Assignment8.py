# Lavender Bank ATM System


INITIAL_BALANCE = 1000.00  # Starting balance of $1000
PIN = "1234"  # Default PIN

def display_welcome():
    print("\n" + "=" * 50)
    print(" Welcome to the Lavender Bank ATM System ")
    print("=" * 50)
    input("Press Enter to continue...")

def verify_pin():
    attempts = 3  #  3 attempts
    
    while attempts > 0:
        pin_input = input("\nPlease enter your 4-digit PIN: ")
        
        # Check if PIN is valid 
        if pin_input == PIN and len(pin_input) == 4 and pin_input.isdigit():
            print("\ PIN verified successfully!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. You have {attempts} attempts remaining.")
            else:
                print("Too many incorrect attempts. Your card has been blocked.")
    return False

def display_menu():
    
    print(" ATM MENU")
    
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")
    

def check_balance(balance):
    print(f"\n Your current balance is: ${balance:.2f}")

def deposit_money(balance, transactions):
    try:
        amount = float(input("\nEnter amount to deposit: $"))
        
        #  no neg deposits
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return balance
        
        # Update balance and transaction history
        balance += amount
        transactions.append(f"DEPOSIT: +${amount:.2f}")
        
        print(f" Successfully deposited: ${amount:.2f}")
        print(f" New balance: ${balance:.2f}")
        
    except ValueError:
        print(" Error: Please enter a valid number.")
    
    return balance

def withdraw_money(balance, transactions):
    try:
        amount = float(input("\nEnter amount to withdraw: $"))
        
        # no neg withdrawals
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return balance
        
        # Check for sufficient bal
        if amount > balance:
            print("Error: Insufficient funds. Transaction cancelled.")
            return balance
        
        # Update bal and transaction history
        balance -= amount
        transactions.append(f"WITHDRAWAL: -${amount:.2f}")
        
        print(f" Successfully withdrawn: ${amount:.2f}")
        print(f"New balance: ${balance:.2f}")
        
    except ValueError:
        print("Error: Please enter a valid number.")
    
    return balance

def view_transactions(transactions):
    if not transactions:
        print("\n No transactions to display.")
        return
    
   
    print(" TRANSACTION HISTORY")
    
    
    for i, transaction in enumerate(transactions, 1):
        print(f"{i}. {transaction}")
    
    

def main():
    # Initialize system
    balance = INITIAL_BALANCE
    transactions = []
    
    # Display welcome message
    display_welcome()
    
    # Verify PIN before proceeding
    if not verify_pin():
        print("\nSystem access denied. Please try again later.")
        return
    
    # Main ATM FUnctions 
    while True:
        display_menu()
        
        choice = input("\nEnter your action (1-5): ")
        
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance, transactions)
        elif choice == "3":
            balance = withdraw_money(balance, transactions)
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            print("\nThank you for using the Lavender Bank ATM System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM system
if __name__ == "__main__":
    main() 