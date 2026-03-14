from cryptography.fernet import Fernet
key = b'MNsyuZAjMhzyr96LGK1ZscPG5VA_YHpT10k-YUe_2C0='
fer = Fernet(key)

master_password = input("enter the log in password: ")

if master_password != "jarvis 2.0":
    print("incorrect password access denied...")
    quit()

def view():
    with open("test.txt", 'r' ) as e:
        for lines in e.readlines():
            data = lines.rstrip()
            user, password = data.split("|")
            print("user:", user,  "password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("enter your account name: ")
    pwd = input("enter your password: ")
    with open("test.txt" , 'a') as e:
        e.write (name + "|"  + fer.encrypt(pwd.encode()).decode() + "\n")
        print ("saved to:"< e.name)


while True:
    mode = input("would you like to (view) or (add) press (q) to quit: ").lower()
    if mode == "view":
        view()
    if mode == "add":
        add()
    if mode == "q":
        print("exiting...")
        exit()