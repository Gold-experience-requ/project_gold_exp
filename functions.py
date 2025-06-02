import sys
import os
import mysql.connector as m
import games as g

con=m.connect(
    host="localhost",
    user="root",
    password="swordsaint",
    database="arcade"
)
cur = con.cursor()
cur.execute("use arcade")



def welcome_screen():
    os.system("cls")
    print(" █████╗ ██████╗  ██████╗  █████╗ ██████╗  ███████╗".center(160))
    print("██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔═══██╗██╔════╝".center(160))
    print("███████║██████╔╝██║      ███████║██║   ██║█████╗  ".center(160))
    print("██╔══██║██╔══██╗██║      ██╔══██║██║   ██║██╔══╝  ".center(160))
    print("██║  ██║██║  ██║╚██████╔╝██║  ██║██████╔╝ ███████╗".center(160))
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ═════╝  ╚══════╝".center(160))
    print("\n")
    print("             WELCOME TO THE ARCADE ZONE!".center(160))
    print("          GET READY FOR PIXELATED FUN!".center(160))
    print("\n")
    print("           > PRESS ENTER TO BEGIN <".center(160))
    print("---------------------------------------------------------".center(160))
    input() # Waits for user to press Enter
    print("\n")

    

def mainmenu():
    print("what Do You Want To Do ?".center(160))
    print(">>> Login".center(160))
    print(">>> Register".center(160))
    print(">>> Exit".center(160))
    try:
        mainmenuinput = input("Enter the no. of your desired option  ")
        if mainmenuinput.lower() == "login":
            print("You have selected option 1")
            # Call the function for option 1
            login()
        elif mainmenuinput.lower() == "register":
            print("You have selected option 2")
            # Call the function for option 2
            register()
        elif mainmenuinput.lower() == "exit":
            print("You have selected option 3")
            sys.exit()
        else:
            print("Invalid option, please try again.")
            mainmenu()
    except ValueError:
        print("Invalid input, please enter a valid input.")
        mainmenu()
        
def register():
    choice = input("Registraion will cause you to share your information with use Enter Y to procedd  ")
    if choice == 'Y' or choice == 'y':
        print("Proceeding with registration...")
        user_name = input("Enter your username: ")
        if len(user_name) < 3:
            print("Username must be at least 3 characters long. Please try again.")
            register()
        user_email = input("Enter your email: ")
        if '@' not in user_email or '.' not in user_email:
            print("Invalid email format. Please try again.")
            register()
        mobile = input("Enter your mobile number: ")
        if len(mobile) != 10 or not mobile.isdigit():
            print("Mobile number must be 10 digits long. Please try again.")
            register()
        password = input("Enter your password: ")
        repassword = input("Re-enter your password: ")
        if password == repassword:
            print("Registration successful!")
            cur.execute(
                "INSERT INTO user (USER_NAME, USER_EMAIL, USER_MOBILE, USER_PASSWORD) VALUES (%s, %s, %s, %s)",
                (user_name, user_email, mobile, password)
            )
            con.commit()
            welcome_screen()
            mainmenu()
        else:
            print("Passwords do not match. Please try again.")
            register()
    else:
        print("Registration cancelled.")
        welcome_screen()
        mainmenu()


def login():
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    cur.execute("SELECT * FROM user WHERE USER_NAME = %s AND USER_PASSWORD = %s", (user_name, password))
    user = cur.fetchone()
    if user:
        print(f"Welcome {user[1]}!")
        # Proceed to the next step after successful login
    if user[5] == 'admin':
        adminmenu()
    elif user[5] == 'player':
        playermenu()
    else:
        print("Invalid username or password. Please try again.")
        login()
        
        
def adminmenu():
    x = "admin"
    print("x")
    
    
def playermenu():
    x = 1
    print("x")
