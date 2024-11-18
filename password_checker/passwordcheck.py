def check_password(password: str):

    if not password.strip(): #Checks if password is empty
        print('Password must not be blank.')
        return
    
    with open('passwords.txt','r') as file:
        common_passwords: list[str] = file.read().splitlines()     
        for i, common_password in enumerate(common_passwords, start=1):
            if password.lower() == common_password:
                print(f'{password}: ❌ (#{i}) in Common Password List')
                return
            
        print(f'{password}:')
        print('🟢 Not Found in Common Password List')

        if len(password) < 12:
            print(f'❌ Password is too short.')
        else:
            print('🟢 Password length is good.')

        if password.isalpha:
            print(f'❌ Add numbers or special characters')
        else:
            print(f'🟢 Password contains numbers or special characters.')
            

def main():   
    user_password = input('Enter a password: ')
    check_password(user_password)
    
    

if __name__ == '__main__':
    main()