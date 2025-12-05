# ТЕМА: Словники
# Завдання 1:
# Створіть додаток для управління користувачами, який має зберігати наступну
# інформацію:
# • логіни користувачів;
# • паролі користувачів.
# Для зберігання інформації використовуйте словник.
# Додаток має надавати таку функціональність:
# • додати нового користувача;
# • видалити користувача;
# • змінити пароль (приймається лише пароль, який відрізняється від
# попереднього);
# • перевірити паролі (відображається незахищені паролі);
# • отримати інформацію про пароль за логіном користувача;
# • *зберегти список користувачів у файл.
# ! незахищеним паролем вважається такий, що має менше 6-ти символів або лише
# букви

users_dict = {}
def add_user(users_dict, login, password):
    users_dict[login] = password
    print(f"User '{login}' added.")

def delete_user(users_dict, login):
    if login in users_dict:
        del users_dict[login] 
        print(f"User '{login}' deleted.")
    else:
        print(f"User '{login}' not found.")
        
def change_password(users_dict, login, password):
    if login in users_dict:
        if users_dict[login] != password:
            users_dict[login] = password
            print(f"Password for user '{login}' changed.")
        else:
            print("New password must be different from the old one.")
            
def check_passwords(users_dict):
    weak_passwords = [login for login, password in users_dict.items() if len(password) < 6 or password.isalpha()]
    print("Users with weak passwords:", weak_passwords) 

def get_password(users_dict, login):
    password = users_dict.get(login)
    if password:
        print(f"Password for user '{login}': {password}")
    else:
        print(f"User '{login}' not found.")

def get_all(users_dict):
    for login, password in users_dict.items():
        print(f"Login: {login}, Password: {password}")
        
def save_all(users_dict):
    dest = input("Enter filename to save users: ")
    with open(dest, 'w') as f:
        for login, password in users_dict.items():
            f.write(f"{login}:{password}\n")
def main():
    
    while True:
        print("\nMenu:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Check Passwords")
        print("5. Get Password by Login")
        print("6. Save All Users to File")
        print("7. Get All Users")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            login = input("Enter login: ")
            password = input("Enter password: ")
            add_user(users_dict, login, password)
        elif choice == '2':
            login = input("Enter login to delete: ")
            delete_user(users_dict, login)
        elif choice == '3':
            login = input("Enter login to change password: ")
            password = input("Enter new password: ")
            change_password(users_dict, login, password)
        elif choice == '4':
            check_passwords(users_dict)
        elif choice == '5':
            login = input("Enter login to get password: ")
            get_password(users_dict, login)
        elif choice == '6':
            save_all(users_dict)
        elif choice == '7':
            get_all(users_dict)
        elif choice == '8':
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()