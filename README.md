# password-manager
Here's a detailed overview of the Python Password Manager:

This password manager application provides secure storage for your account credentials using a simple yet effective encryption system. At its core, it utilizes a character-shifting algorithm (shift cipher) to encrypt passwords before storing them in a local text file. The system is protected by a 4-digit master PIN that must be entered to access sensitive operations like viewing or deleting stored passwords. 

The program features a console-based menu interface with five main functions: adding new account passwords (automatically encrypted), viewing stored passwords (decrypted only after PIN verification), listing all saved accounts, deleting existing entries, and saving changes before exit. All data persists between sessions by writing to a "passwords.txt" file in the same directory, with passwords always stored in their encrypted form.

Key technical aspects include the use of basic file I/O operations for data storage, ASCII value manipulation for the encryption/decryption process, and careful input validation for the PIN system. The implementation deliberately avoids external dependencies, using only Python's built-in functions to ensure maximum compatibility across different systems. While the encryption method is relatively simple, it provides a basic level of security for personal use, and the entire program runs as a standalone script without requiring installation of additional libraries or frameworks.
