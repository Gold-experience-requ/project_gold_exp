
# Simple Battleship Game
import random

ship = random.randint(0, 9)
attempts = 5
print("Guess the ship's location (0-9)!")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == ship:
        print("Hit! You sunk the battleship!")
        break
    else:
        print("Miss!")
        attempts -= 1
else:
    print("Game over! The ship was at position", ship)
    
#periodic table quiz# Simple Periodic Table Quiz
import random

# List of elements: (Symbol, Name, Atomic Number)
elements = [
    ("H", "Hydrogen", 1),
    ("He", "Helium", 2),
    ("Li", "Lithium", 3),
    ("Be", "Beryllium", 4),
    ("B", "Boron", 5),
    ("C", "Carbon", 6),
    ("N", "Nitrogen", 7),
    ("O", "Oxygen", 8),
    ("F", "Fluorine", 9),
    ("Ne", "Neon", 10),
    ("Na", "Sodium", 11),
    ("Mg", "Magnesium", 12),
    ("Al", "Aluminum", 13),
    ("Si", "Silicon", 14),
    ("P", "Phosphorus", 15),
    ("S", "Sulfur", 16),
    ("Cl", "Chlorine", 17),
    ("Ar", "Argon", 18),
    ("K", "Potassium", 19),
    ("Ca", "Calcium", 20)
    # You can add more elements if you want!
]

score = 0
questions = 5

print("Welcome to the Periodic Table Quiz!")
print("You will be asked about element names, symbols, and atomic numbers.\n")

for i in range(questions):
    element = random.choice(elements)
    q_type = random.choice(["symbol", "name", "number"])
    
    if q_type == "symbol":
        answer = input(f"Q{i+1}: What is the symbol for {element[1]}? ").strip()
        if answer.capitalize() == element[0]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {element[0]}.\n")
    elif q_type == "name":
        answer = input(f"Q{i+1}: What is the name of the element with symbol {element[0]}? ").strip()
        if answer.lower() == element[1].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {element[1]}.\n")
    else:  # number
        answer = input(f"Q{i+1}: What is the atomic number of {element[1]}? ").strip()
        if answer.isdigit() and int(answer) == element[2]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {element[2]}.\n")

print(f"Quiz Over! Your score: {score}/{questions}")
if score == questions:
    print("Excellent! You're a periodic table master!")
elif score >= questions // 2:
    print("Good job! Keep practicing to improve.")
else:
    print("Don't worry, you'll get better with practice!")
    
#maths quiz final answer and operation given and need to choose array of no.

#lucky draw
             
             
import random

print("Welcome to the RPG Battle Arena!")
player_hp = 30
monster_hp = 25
potions = 3

monsters = [
    "Goblin",
    "Orc",
    "Troll",
    "Skeleton",
    "Zombie",
    "Vampire",
    "Werewolf",
    "Dragon",
    "Slime",
    "Giant Spider",
    "Witch",
    "Demon",
    "Ghost",
    "Minotaur",
    "Hydra",
    "Golem",
    "Lich",
    "Harpy",
    "Basilisk",
    "Kraken"
]
monsterpickup = random.choice(monsters)
print(f"A wild {monsterpickup} appears! Prepare for battle!")
while player_hp > 0 and monster_hp > 0:
    print(f"\nYour HP: {player_hp} | Monster HP: {monster_hp} | Potions: {potions}")
    print("Choose your action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Run")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        dmg = random.randint(4, 8)
        monster_hp -= dmg
        print(f"You attack the monster for {dmg} damage!")
    elif choice == "2":
        if potions > 0 and player_hp < 70:
            print("You drink a potion to heal yourself.")
            heal = random.randint(6, 12)
            player_hp += heal
            potions -= 1
            print(f"You drink a potion and heal for {heal} HP!")
        elif player_hp > 70:
            print("You are already at full health!")
            continue
        else:
            print("You have no potions left!")
            continue
    elif choice == "3":
        print("You try to run away...")
        if random.randint(0,5) < 6:  # 60% chance to escape
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
elif monster_hp <= 0:
    print("\nCongratulations! You defeated the monster!")
elif choice == "3" and player_hp > 0:
    print("\nYou survived by running away!")  



#black jack
def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 for J/Q/K, 11 for Ace
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a hand. Handles Ace as 1 or 11."""
    score3 = sum(hand)
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score3 = sum(hand)
    return score

def show_hand(hand, owner="Your"):
    print(f"{owner} cards: {hand} (Total: {calculate_score(hand)})")

print("Welcome to Blackjack!\n")

player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

game_over = False

while not game_over:
    show_hand(player_hand)
    print(f"Dealer's first card: {dealer_hand[0]}")
    
    if calculate_score(player_hand) == 21:
        print("Blackjack! You win!")
        game_over = True
        break
    elif calculate_score(player_hand) > 21:
        print("You went over 21. You lose!")
        game_over = True
        break

    action = input("Type 'hit' to get another card, or 'stand' to hold: ").lower()
    if action == "hit":
        player_hand.append(deal_card())
    elif action == "stand":
        break
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")

# Dealer's turn
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

print("Game over. Thanks for playing!")                  