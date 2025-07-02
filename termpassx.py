# Tool Name: TermPassX - The Ultimate Termux Password Generator
# Author: Mahedi Hasan Rafsun
# Developer | Programmer | Cybersecurity Enthusiast
# Website: https://weblearnerprosite.blogspot.com/
# Email: developer.mahedihasanrafsun@gmail.com
# Copyright © 2025 Mahedi Hasan Rafsun. All Rights Reserved.
#
# Created by: mhrtuch240
# Created on: 2025-07-01 18:09:00 UTC
# Last modified: 2025-07-01 18:09:00 UTC

import string
import secrets
import math
import subprocess
import sys
import os
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

class PasswordHistory:
    def __init__(self):
        self.history_file = os.path.expanduser('~/.termpassx/password_history.txt')
        self.ensure_history_dir()

    def ensure_history_dir(self):
        directory = os.path.dirname(self.history_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(self.history_file):
            with open(self.history_file, 'w', encoding='utf-8') as f:
                f.write("# TermPassX Password History\n")
                f.write("# Format: [Date Time UTC] - Password - Strength - Entropy\n\n")

    def add_password(self, password, strength, entropy):
        current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.history_file, 'a', encoding='utf-8') as f:
            f.write(f"[{current_time} UTC] - {password} - {strength} - {entropy:.2f} bits\n")

    def get_history(self, limit=10):
        if not os.path.exists(self.history_file):
            return []
        
        with open(self.history_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Filter out comments and empty lines
            passwords = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
            return passwords[-limit:]  # Return last 'limit' entries

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.emojis = "😀😎🔒💪🚀⭐️🔑💻🎯"
        
    def generate_password(self, length, use_lower=True, use_upper=True, 
                         use_digits=True, use_symbols=True, use_emojis=False):
        # Initialize character set
        charset = ""
        if use_lower:
            charset += self.lowercase
        if use_upper:
            charset += self.uppercase
        if use_digits:
            charset += self.digits
        if use_symbols:
            charset += self.symbols
        if use_emojis:
            charset += self.emojis
            
        if not charset:
            return None
            
        while True:
            password = ''.join(secrets.choice(charset) for _ in range(length))
            
            # Validate password meets requirements
            if (not use_upper or any(c.isupper() for c in password)) and \
               (not use_symbols or any(c in self.symbols for c in password)) and \
               (not use_lower or any(c.islower() for c in password)) and \
               (not use_digits or any(c.isdigit() for c in password)):
                
                # Check for repeated characters
                char_count = {}
                for c in password:
                    if c in char_count:
                        char_count[c] += 1
                        if char_count[c] > 2:  # Allow max 2 repetitions
                            break
                    else:
                        char_count[c] = 1
                else:
                    return password

    def generate_multiple_passwords(self, count, length, use_lower=True, use_upper=True,
                                  use_digits=True, use_symbols=True, use_emojis=False):
        passwords = []
        for _ in range(count):
            password = self.generate_password(length, use_lower, use_upper,
                                           use_digits, use_symbols, use_emojis)
            if password:
                passwords.append(password)
        return passwords
                    
    def calculate_entropy(self, password):
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += len(self.lowercase)
        if any(c.isupper() for c in password):
            charset_size += len(self.uppercase)
        if any(c.isdigit() for c in password):
            charset_size += len(self.digits)
        if any(c in self.symbols for c in password):
            charset_size += len(self.symbols)
        if any(c in self.emojis for c in password):
            charset_size += len(self.emojis)
            
        entropy = math.log2(charset_size ** len(password))
        return entropy
        
    def get_password_strength(self, entropy):
        if entropy < 50:
            return f"{Fore.RED}Weak{Style.RESET_ALL}"
        elif entropy < 70:
            return f"{Fore.YELLOW}Medium{Style.RESET_ALL}"
        elif entropy < 90:
            return f"{Fore.GREEN}Strong{Style.RESET_ALL}"
        else:
            return f"{Fore.BLUE}Very Strong{Style.RESET_ALL}"

def copy_to_clipboard(text):
    try:
        subprocess.run(['termux-clipboard-set'], input=text.encode(), check=True)
        print(f"{Fore.GREEN}Password copied to clipboard!{Style.RESET_ALL}")
    except (subprocess.SubprocessError, FileNotFoundError):
        print(f"{Fore.YELLOW}Could not copy to clipboard. Termux:API might not be installed.{Style.RESET_ALL}")

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        print(f"{Fore.RED}Invalid input! Please enter one of: {', '.join(valid_options)}{Style.RESET_ALL}")

def generate_password_menu(generator, history):
    try:
        # Get number of passwords to generate
        while True:
            try:
                num_passwords = int(input(f"{Fore.GREEN}How many passwords to generate (1-10): {Style.RESET_ALL}"))
                if 1 <= num_passwords <= 10:
                    break
                print(f"{Fore.RED}Please enter a number between 1 and 10{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")

        # Get password length
        while True:
            try:
                length = int(input(f"{Fore.GREEN}Enter password length (8-128): {Style.RESET_ALL}"))
                if 8 <= length <= 128:
                    break
                print(f"{Fore.RED}Invalid length! Must be between 8 and 128.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number{Style.RESET_ALL}")

        # Get character set preferences
        print("\nSelect character sets (y/n for each):")
        use_lower = get_valid_input("Include lowercase letters? (y/n): ", ['y', 'n']) == 'y'
        use_upper = get_valid_input("Include uppercase letters? (y/n): ", ['y', 'n']) == 'y'
        use_digits = get_valid_input("Include numbers? (y/n): ", ['y', 'n']) == 'y'
        use_symbols = get_valid_input("Include symbols? (y/n): ", ['y', 'n']) == 'y'
        use_emojis = get_valid_input("Include emojis? (y/n): ", ['y', 'n']) == 'y'

        if not any([use_lower, use_upper, use_digits, use_symbols, use_emojis]):
            print(f"{Fore.RED}Error: At least one character set must be selected!{Style.RESET_ALL}")
            return

        # Generate passwords
        passwords = generator.generate_multiple_passwords(
            num_passwords, length, use_lower, use_upper, use_digits, use_symbols, use_emojis
        )

        # Display results
        print(f"\n{Fore.CYAN}Generated Passwords:{Style.RESET_ALL}")
        for i, password in enumerate(passwords, 1):
            entropy = generator.calculate_entropy(password)
            strength = generator.get_password_strength(entropy)
            clean_strength = strength.replace(Fore.RED, '').replace(Fore.YELLOW, '') \
                                   .replace(Fore.GREEN, '').replace(Fore.BLUE, '') \
                                   .replace(Style.RESET_ALL, '')
            
            print(f"\n{Fore.CYAN}Password #{i}:{Style.RESET_ALL}")
            print(f"Password: {password}")
            print(f"Strength: {strength}")
            print(f"Entropy: {entropy:.2f} bits")
            
            # Save to history
            history.add_password(password, clean_strength, entropy)

        # Copy to clipboard option
        if len(passwords) == 1:
            if get_valid_input("\nCopy to clipboard? (y/n): ", ['y', 'n']) == 'y':
                copy_to_clipboard(passwords[0])
        else:
            while True:
                copy_choice = input(f"\nEnter password number to copy (1-{len(passwords)}) or 'n' to skip: ").lower()
                if copy_choice == 'n':
                    break
                try:
                    idx = int(copy_choice)
                    if 1 <= idx <= len(passwords):
                        copy_to_clipboard(passwords[idx-1])
                        break
                    else:
                        print(f"{Fore.RED}Please enter a valid number between 1 and {len(passwords)}{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Invalid input! Please enter a number or 'n'{Style.RESET_ALL}")

    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter valid numbers.{Style.RESET_ALL}")

def main():
    generator = PasswordGenerator()
    history = PasswordHistory()
    
    while True:
        print(f"\n{Fore.CYAN}=== TermPassX - Password Generator ==={Style.RESET_ALL}")
        print("1. Generate Password(s)")
        print("2. Validate Password")
        print("3. View Password History")
        print("4. Exit")
        
        choice = input(f"\n{Fore.GREEN}Choose an option (1-4): {Style.RESET_ALL}")
        
        if choice == '1':
            generate_password_menu(generator, history)
                
        elif choice == '2':
            password = input(f"{Fore.GREEN}Enter password to validate: {Style.RESET_ALL}")
            entropy = generator.calculate_entropy(password)
            strength = generator.get_password_strength(entropy)
            
            print(f"\n{Fore.CYAN}Analysis Results:{Style.RESET_ALL}")
            print(f"Length: {len(password)} characters")
            print(f"Strength: {strength}")
            print(f"Entropy: {entropy:.2f} bits")
            print(f"Contains lowercase: {any(c.islower() for c in password)}")
            print(f"Contains uppercase: {any(c.isupper() for c in password)}")
            print(f"Contains numbers: {any(c.isdigit() for c in password)}")
            print(f"Contains symbols: {any(c in generator.symbols for c in password)}")
            print(f"Contains emojis: {any(c in generator.emojis for c in password)}")

        elif choice == '3':
            print(f"\n{Fore.CYAN}Password History (Last 10 entries):{Style.RESET_ALL}")
            history_entries = history.get_history()
            if not history_entries:
                print(f"{Fore.YELLOW}No password history found.{Style.RESET_ALL}")
            else:
                for entry in history_entries:
                    print(entry)

        elif choice == '4':
            print(f"\n{Fore.CYAN}Thanks for using TermPassX!{Style.RESET_ALL}")
            sys.exit(0)
            
        else:
            print(f"{Fore.RED}Invalid choice! Please select 1, 2, 3, or 4.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Program terminated by user.{Style.RESET_ALL}")
        sys.exit(0)