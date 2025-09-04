import mysql.connector as m
import random
import os
import db

con = db.con
cur = db.cur

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def battleship(user_id):
    clear_screen()
    print("="*60)
    print("BATTLESHIP".center(60))
    print("="*60)
    ship = random.randint(0, 9)
    attempts = 5
    score = 0
    print("Guess the ship's location (0-9)!")

    while attempts > 0:
        try:
            guess = int(input(f"Attempts left {attempts}. Enter your guess: "))
            if guess < 0 or guess > 9:
                print("Please enter a number between 0 and 9.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 0-9.")
            continue
        if guess == ship:
            print("Hit! You sunk the battleship!")
            score += 5
            break
        else:
            print("Miss!")
            attempts -= 1
    else:
        print("Game over! The ship was at position", ship)
    cur.execute(
        "INSERT INTO score (USER_ID, GAME_ID, SCORE_VALUE) VALUES (%s, %s, %s)",
        (user_id, 'battleship', score)
    )
    con.commit()
    print(f"Score saved! Your score: {score}")
    input("Press Enter to return to menu...")

def guess_number(user_id):
    clear_screen()
    print("="*60)
    print("GUESS THE NUMBER".center(60))
    print("="*60)
    number = random.randint(1, 100)
    attempts = 7
    score = 0
    print("Guess the number between 1 and 100!")

    while attempts > 0:
        try:
            guess = int(input(f"Attempts left {attempts}. Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1-100.")
            continue
        if guess == number:
            print("Congratulations! You guessed the number!")
            score = attempts * 2
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
    else:
        print(f"Game over! The number was {number}.")
    cur.execute(
        "INSERT INTO score (USER_ID, GAME_ID, SCORE_VALUE) VALUES (%s, %s, %s)",
        (user_id, 'guess number', score)
    )
    con.commit()
    print(f"Score saved! Your score: {score}")
    input("Press Enter to return to menu...")

def rock_paper_scissors(user_id):
    clear_screen()
    print("="*60)
    print("ROCK PAPER SCISSORS".center(60))
    print("="*60)
    choices = ['rock', 'paper', 'scissors']
    rounds = 5
    score = 0
    for i in range(rounds):
        print(f"Round {i+1} of {rounds}")
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")
        if user_choice == comp_choice:
            print("Draw!")
            score += 1
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            print("You win this round!")
            score += 2
        else:
            print("Computer wins this round!")
    print(f"Game Over! Your score: {score}")
    cur.execute(
        "INSERT INTO score (USER_ID, GAME_ID, SCORE_VALUE) VALUES (%s, %s, %s)",
        (user_id, 'rock paper scissors', score)
    )
    con.commit()
    print("Score saved!")
    input("Press Enter to return to menu...")

def rpg(user_id):
    clear_screen()
    print("="*60)
    print("RPG BATTLE ARENA".center(60))
    print("="*60)
    player_hp = 30
    monster_hp = 25
    potions = 3
    monsters = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie", "Vampire", "Werewolf", "Dragon", "Slime", "Giant Spider", "Witch", "Demon", "Ghost", "Minotaur", "Hydra", "Golem", "Lich", "Harpy", "Basilisk", "Kraken"]
    monsterpickup = random.choice(monsters)
    print(f"A wild {monsterpickup} appears! Prepare for battle!")
    score = 0
    while player_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {player_hp} | Monster HP: {monster_hp} | Potions: {potions}")
        print("Choose your action:\n1. Attack\n2. Heal\n3. Run")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            dmg = random.randint(4, 8)
            monster_hp -= dmg
            print(f"You attack the monster for {dmg} damage!")
        elif choice == "2":
            if potions > 0 and player_hp < 70:
                heal = random.randint(6, 12)
                player_hp += heal
                potions -= 1
                print(f"You drink a potion and heal for {heal} HP!")
            elif player_hp > 70:
                print("You are already at full health!")
            else:
                print("You have no potions left!")
        elif choice == "3":
            print("You try to run away...")
            if random.randint(0,5) < 3:
                print("You escaped safely!")
                break
            else:
                print("You failed to escape!")
        else:
            print("Invalid choice. Try again.")
            continue
        if monster_hp > 0:
            monster_dmg = random.randint(3, 7)
            player_hp -= monster_dmg
            print(f"The monster attacks you for {monster_dmg} damage!")
    if player_hp <= 0:
        print("\nYou have been defeated by the monster.")
        score -= 5
    elif monster_hp <= 0:
        print("\nCongratulations! You defeated the monster!")
        score += 20
    elif choice == "3" and player_hp > 0:
        print("\nYou survived by running away!")
    cur.execute(
        "INSERT INTO score (USER_ID, GAME_ID, SCORE_VALUE) VALUES (%s, %s, %s)",
        (user_id, 'RPG arena', score)
    )
    con.commit()
    print(f"Score saved! Your score: {score}")
    input("Press Enter to return to menu...")

def blackjack(user_id):
    clear_screen()
    print("="*60)
    print("BLACKJACK".center(60))
    print("="*60)
    def deal_card():
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        return random.choice(cards)
    def calculate_score(hand):
        score = sum(hand)
        aces = hand.count(11)
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score
    def show_hand(hand, owner="Your"):
        print(f"{owner} cards: {hand} (Total: {calculate_score(hand)})")
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    game_over = False
    score = 0
    while not game_over:
        show_hand(player_hand)
        print(f"Dealer's first card: {dealer_hand[0]}")
        if calculate_score(player_hand) == 21:
            print("Blackjack! You win!")
            score += 20
            game_over = True
            break
        elif calculate_score(player_hand) > 21:
            print("You went over 21. You lose!")
            score -= 10
            game_over = True
            break
        action = input("Type 'hit' to get another card, or 'stand' to hold: ").lower()
        if action == "hit":
            player_hand.append(deal_card())
        elif action == "stand":
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")
    if not game_over:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card())
        show_hand(dealer_hand, "Dealer's")
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21:
            print("Dealer went over 21. You win!")
            score += 20
        elif dealer_score == player_score:
            print("It's a draw!")
            score += 5
        elif player_score > dealer_score:
            print("You win!")
            score += 10
        else:
            print("Dealer wins!")
            score -= 10
    print("Game over. Thanks for playing!")       
    cur.execute(
        "INSERT INTO score (USER_ID, GAME_ID, SCORE_VALUE) VALUES (%s, %s, %s)",
        (user_id, 'blackjack', score)
    )
    con.commit()
    print(f"Score saved! Your score: {score}")
    input("Press Enter to return to menu...")


