import sys
import os
import mysql.connector as m
import games as g
score = 0
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
    global score
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
        score = 0  # Reset score for the player
    else:
        print("Invalid username or password. Please try again.")
        login()
    return user[0]  # Return USER_ID for further use
        
        
def adminmenu():
    print("Hello admin")
    print("1. View all users")
    print("2. View all scores")
    print("3. View all games")
    print("4. Suspend a user")
    print("5. Logout")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("You have selected option 1")
        cur.execute("SELECT * FROM user")
        users = cur.fetchall()
        if users:
            print("All Users:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Mobile: {user[3]}, Role: {user[5]}")
        else:
            print("No users found.")
        adminmenu()
    elif choice == '2':
        print("You have selected option 2")
        cur.execute("SELECT * FROM score")
        scores = cur.fetchall()
        if scores:
            print("All Scores:")
            for score in scores:
                print(f"User ID: {score[0]}, Game ID: {score[1]}, Score: {score[2]}, Time Stamp: {score[3]}")
        else:
            print("No scores found.")
        adminmenu()
    elif choice == '3':
        print("You have selected option 3")
        print("Available Games:")
        print("1. Battleship")
        print("2. Periodic table quiz")
        print("3. RPG Battle Arena")
        print("4. BlackJack")
        adminmenu()
    elif choice == '4':
        print("You have selected option 4")
        user_id = input("Enter the USER_ID of the user to suspend: ")
        cur.execute("delete from user where USER_ID = %s", (user_id,))
        cur.execute("delete from score where USER_ID = %s", (user_id,))
        con.commit()
        print(f"User with ID {user_id} has been suspended.")
        adminmenu()
    elif choice == '5':
        print("You have selected option 3")
        print("Logging out...")
        welcome_screen()
        mainmenu()
    else:
        print("Invalid choice, please try again.")
        adminmenu()
    
username = login()   

def playermenu():
    global username
    print("Welcome to the Player Menu!")
    print("1. Play Games")
    print("2. View Scores")
    print("3. Logout")
    choice = input("enter Your option")
    if choice == '1':
        print("You have selected option 1")
        print("which game do you want to play")
        print("1. Battleship")
        print("2. Periodic table quiz")
        print("3. RPG Battle Arena")
        print("4. BlackJack")
        choice2 = input("Enter your choice: ")
        if choice2 == '1':
            g.battleship()
            playermenu()
        elif choice2 == '2':
            g.periodic_table_quiz(username)
            playermenu()
        elif choice2 == '3':
            g.rpg()
            playermenu()
        elif choice2 == '4':
            g.blackjack()
            playermenu()
        else:
            print("Invalid choice, please try again.")
            playermenu()
    if choice == '2':
        print("You have selected option 2")
        cur.execute("SELECT * FROM score WHERE USER_ID = %s", (username,))
        scores = cur.fetchall()
        if scores:
            print("Your Scores:")
            for score in scores:
                print(f"Game ID: {score[2]}, Score: {score[3]}, Time Stamp: {score[4]}")
        else:
            print("No scores found.")
        playermenu()
    if choice == '3':
        print("You have selected option 3")
        print("Logging out...")
        welcome_screen()
        mainmenu()