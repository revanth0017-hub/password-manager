# Password Manager (No external modules needed)
class PasswordManager:
    def __init__(self):
        self.accounts = {}  # Using regular dictionary instead of defaultdict
        self.master_pin = None
        self.filename = "passwords.txt"
        
    def _encrypt(self, password, shift=3):
        """Simple encryption using character shifting"""
        encrypted = []
        for char in password:
            encrypted_char = chr((ord(char) + shift) % 256)
            encrypted.append(encrypted_char)
        return ''.join(encrypted)
    
    def _decrypt(self, encrypted, shift=3):
        """Decrypts the shifted characters"""
        decrypted = []
        for char in encrypted:
            decrypted_char = chr((ord(char) - shift) % 256)
            decrypted.append(decrypted_char)
        return ''.join(decrypted)
    
    def _normalize_pin(self, pin):
        """Ensure PIN is 4 digits"""
        return int(pin) % 10000
    
    def set_pin(self, pin):
        """Set the master PIN"""
        self.master_pin = self._normalize_pin(pin)
    
    def check_pin(self, entered_pin):
        """Verify if entered PIN matches master PIN"""
        return self._normalize_pin(entered_pin) == self.master_pin
    
    def load_accounts(self):
        """Load accounts from file if it exists"""
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split(maxsplit=1)
                        if len(parts) == 2:
                            account, encrypted = parts
                            self.accounts[account] = encrypted
        except FileNotFoundError:
            print("No password file found. Starting fresh.")
    
    def save_accounts(self):
        """Save all accounts to file"""
        with open(self.filename, 'w') as f:
            for account, encrypted in self.accounts.items():
                f.write(f"{account} {encrypted}\n")
        print("Passwords saved successfully.")
    
    def add_password(self, account, password):
        """Add new account password"""
        encrypted = self._encrypt(password)
        self.accounts[account] = encrypted
        print(f"Password added for {account}!")
    
    def get_password(self, account, pin):
        """Retrieve password if PIN is correct"""
        if not self.check_pin(pin):
            print("Wrong PIN! Access denied.")
            return
        
        if account in self.accounts:
            decrypted = self._decrypt(self.accounts[account])
            print(f"Password for {account}: {decrypted}")
        else:
            print(f"No account named {account} found.")
    
    def delete_account(self, account, pin):
        """Delete an account if PIN is correct"""
        if not self.check_pin(pin):
            print("Wrong PIN! Can't delete.")
            return
        
        if account in self.accounts:
            del self.accounts[account]
            print(f"Account {account} deleted.")
        else:
            print(f"Account {account} doesn't exist.")
    
    def show_accounts(self):
        """List all stored accounts"""
        if not self.accounts:
            print("No accounts stored yet.")
            return
        
        print("Your saved accounts:")
        for i, account in enumerate(self.accounts.keys(), 1):
            print(f"{i}. {account}")

def get_valid_pin():
    """Helper to get a valid 4-digit PIN"""
    while True:
        pin = input("Enter 4-digit PIN: ").strip()
        if pin.isdigit() and len(pin) == 4:
            return int(pin)
        print("Invalid PIN - must be 4 digits.")

def main():
    print("\n=== Password Manager ===")
    manager = PasswordManager()
    manager.load_accounts()
    
    # Set up PIN if first run
    if manager.master_pin is None:
        print("\nSet up your master PIN")
        manager.set_pin(get_valid_pin())
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add new password")
        print("2. View password")
        print("3. List accounts")
        print("4. Delete account")
        print("5. Save & Exit")
        
        try:
            choice = input("Your choice (1-5): ").strip()
            if not choice.isdigit():
                raise ValueError
            choice = int(choice)
        except ValueError:
            print("Please enter a number between 1 and 5")
            continue
        
        if choice == 1:
            account = input("Account name: ").strip()
            password = input("Password: ").strip()
            if account and password:
                manager.add_password(account, password)
            else:
                print("Account name and password cannot be empty!")
        
        elif choice == 2:
            account = input("Account name: ").strip()
            if account:
                pin = get_valid_pin()
                manager.get_password(account, pin)
            else:
                print("Please enter an account name")
        
        elif choice == 3:
            manager.show_accounts()
        
        elif choice == 4:
            account = input("Account to delete: ").strip()
            if account:
                pin = get_valid_pin()
                manager.delete_account(account, pin)
            else:
                print("Please enter an account name")
        
        elif choice == 5:
            manager.save_accounts()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 5")

if __name__ == "__main__":
    main()
