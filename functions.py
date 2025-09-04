import sys
import os
import db
import games as g

con = db.con
cur = db.cur

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print("="*80)
    print(" █████╗ ██████╗  ██████╗  █████╗ ██████╗  ███████╗".center(80))
    print("██╔══██╗██╔══██╗██╔════╝ ██╔══██╗██╔═══██╗██╔════╝".center(80))
    print("███████║██████╔╝██║      ███████║██║   ██║█████╗  ".center(80))
    print("██╔══██║██╔══██╗██║      ██╔══██║██║   ██║██╔══╝  ".center(80))
    print("██║  ██║██║  ██║╚██████╔╝██║  ██║██████╔╝ ███████╗".center(80))
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ═════╝  ╚══════╝".center(80))
    print("="*80)

def welcome_screen():
    clear_screen()
    print_banner()
    print("\nWELCOME TO THE ARCADE ZONE!".center(80))
    print("GET READY FOR PIXELATED FUN!".center(80))
    print("\n> PRESS ENTER TO BEGIN <".center(80))
    print("="*80)
    input()
    clear_screen()

def mainmenu():
    while True:
        print_banner()
        print("MAIN MENU".center(80))
        print("1. Login".center(80))
        print("2. Register".center(80))
        print("3. Exit".center(80))
        print("="*80)
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Thank you for visiting Arcade Zone!")
            sys.exit()
        else:
            print("Invalid option, please try again.\n")

def register():
    clear_screen()
    print_banner()
    print("REGISTRATION".center(80))
    print("="*80)
    choice = input("Registration will cause you to share your information with us.\nEnter Y to proceed or N to cancel: ").strip().lower()
    if choice == 'y':
        while True:
            user_name = input("Enter your username (min 3 chars): ").strip()
            if len(user_name) < 3:
                print("Username must be at least 3 characters long.")
                continue
            cur.execute("SELECT * FROM user WHERE USER_NAME = %s", (user_name,))
            if cur.fetchone():
                print("Username already exists. Try another.")
                continue
            break
        while True:
            user_email = input("Enter your email: ").strip()
            if '@' not in user_email or '.' not in user_email:
                print("Invalid email format.")
                continue
            break
        while True:
            mobile = input("Enter your mobile number (10 digits): ").strip()
            if len(mobile) != 10 or not mobile.isdigit():
                print("Mobile number must be 10 digits.")
                continue
            break
        while True:
            password = input("Enter your password: ")
            repassword = input("Re-enter your password: ")
            if password != repassword:
                print("Passwords do not match.")
                continue
            break
        cur.execute(
            "INSERT INTO user (USER_NAME, USER_PASSWORD, USER_EMAIL, USER_MOBILE, ROLE) VALUES (%s, %s, %s, %s, %s)",
            (user_name, password, user_email, mobile, 'player')
        )
        con.commit()
        print("Registration successful!\n")
        input("Press Enter to continue...")
        welcome_screen()
    else:
        print("Registration cancelled.\n")
        input("Press Enter to return to main menu...")
        welcome_screen()

def login():
    clear_screen()
    print_banner()
    print("LOGIN".center(80))
    print("="*80)
    user_name = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    cur.execute("SELECT * FROM user WHERE USER_NAME = %s AND USER_PASSWORD = %s", (user_name, password))
    user = cur.fetchone()
    if user:
        print(f"\nWelcome {user[1]}!\n")
        if user[5] == 'admin':
            adminmenu()
        elif user[5] == 'player':
            playermenu(user[0])
        else:
            print("Unknown role. Contact admin.")
            mainmenu()
    else:
        print("Invalid username or password. Please try again.")
        input("Press Enter to retry...")
        login()

def adminmenu():
    while True:
        clear_screen()
        print_banner()
        print("ADMIN MENU".center(80))
        print("1. View all users".center(80))
        print("2. View all scores".center(80))
        print("3. View all games".center(80))
        print("4. Suspend a user".center(80))
        print("5. Logout".center(80))
        print("="*80)
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            cur.execute("SELECT * FROM user")
            users = cur.fetchall()
            print("\nAll Users:")
            print("-"*80)
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[3]}, Mobile: {user[4]}, Role: {user[5]}")
            print("-"*80)
            input("Press Enter to continue...")
        elif choice == '2':
            cur.execute("SELECT * FROM score")
            scores = cur.fetchall()
            print("\nAll Scores:")
            print("-"*80)
            for score in scores:
                print(f"User ID: {score[0]}, Game: {score[1]}, Score: {score[2]}, Time: {score[3]}")
            print("-"*80)
            input("Press Enter to continue...")
        elif choice == '3':
            print("\nAvailable Games:")
            print("- Battleship\n- Guess the Number\n- Rock Paper Scissors\n- RPG Battle Arena\n- BlackJack")
            input("Press Enter to continue...")
        elif choice == '4':
            user_id = input("Enter the USER_ID of the user to suspend: ").strip()
            confirm = input(f"Are you sure you want to suspend user {user_id}? (Y/N): ").strip().lower()
            if confirm == 'y':
                cur.execute("DELETE FROM user WHERE USER_ID = %s", (user_id,))
                cur.execute("DELETE FROM score WHERE USER_ID = %s", (user_id,))
                con.commit()
                print(f"User with ID {user_id} has been suspended.")
            else:
                print("Suspension cancelled.")
            input("Press Enter to continue...")
        elif choice == '5':
            print("Logging out...")
            welcome_screen()
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")

def playermenu(user_id):
    while True:
        clear_screen()
        print_banner()
        print("PLAYER MENU".center(80))
        print("1. Play Games".center(80))
        print("2. View Scores".center(80))
        print("3. Logout".center(80))
        print("="*80)
        choice = input("Enter your option (1-3): ").strip()
        if choice == '1':
            clear_screen()
            print_banner()
            print("Select a Game".center(80))
            print("1. Battleship".center(80))
            print("2. Guess the Number".center(80))
            print("3. Rock Paper Scissors".center(80))
            print("4. RPG Battle Arena".center(80))
            print("5. BlackJack".center(80))
            print("="*80)
            choice2 = input("Enter your choice (1-5): ").strip()
            if choice2 == '1':
                g.battleship(user_id)
            elif choice2 == '2':
                g.guess_number(user_id)
            elif choice2 == '3':
                g.rock_paper_scissors(user_id)
            elif choice2 == '4':
                g.rpg(user_id)
            elif choice2 == '5':
                g.blackjack(user_id)
            else:
                print("Invalid choice, please try again.")
                input("Press Enter to continue...")
        elif choice == '2':
            cur.execute("SELECT * FROM score WHERE USER_ID = %s", (user_id,))
            scores = cur.fetchall()
            print("\nYour Scores:")
            print("-"*80)
            for score in scores:
                print(f"Game: {score[1]}, Score: {score[2]}, Time: {score[3]}")
            print("-"*80)
            input("Press Enter to continue...")
        elif choice == '3':
            print("Logging out...")
            welcome_screen()
            break
        else:
            print("Invalid choice, please try again.")
            input("Press Enter to continue...")