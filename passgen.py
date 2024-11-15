import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase +string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password



if __name__ == '__main__':
    num_passwords = int(input('Enter number of passwords to generate: \n'))
    
    pass_length = int(input('Enter desired password length: \n'))
    if pass_length < 3:
        raise ValueError('Password must be longer than three characters. \n')

    include_symbols = input('Would you like to include symbols? Y/N?')
    if include_symbols.lower() == 'y':
        symbols = True
    elif include_symbols.lower() == 'n':
        symbols = False
    else:
        raise ValueError('Must be Y/N value.')
    
    include_upper = input('Would you like to include upper case characters? Y/N?')
    if include_upper.lower() == 'y':
        uppercase = True
    elif include_upper.lower() == 'n':
        uppercase = False
    else:
        raise ValueError('Must be Y/N value.')
        



    for i in range(1, num_passwords +1):
        while True:
            new_pass: str = generate_password(pass_length, symbols, uppercase)

            # Ensure the password meets all criteria
            if uppercase and not contains_upper(new_pass):
                continue  # Regenerate if uppercase condition is not met
            if symbols and not contains_symbols(new_pass):
                continue  # Regenerate if symbols condition is not met
        # If password is valid, break out of the loop
            specs: str = f'Uppercase: {contains_upper(new_pass)}, Symbols: {contains_symbols(new_pass)}'
            print(f'{i} -> {new_pass} ({specs})')
            break  # Exit while loop when valid password is generated


    
    