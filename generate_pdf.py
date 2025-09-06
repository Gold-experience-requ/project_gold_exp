from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Blue gradient header
        self.set_fill_color(0, 102, 204)
        self.rect(0, 0, 210, 20, 'F')
        self.set_y(6)
        self.set_font("DejaVu", "B", 18)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, "Arcade Zone Project Documentation", ln=True, align="C")
        self.ln(5)
        self.set_text_color(0, 0, 0)

    def chapter_title(self, title):
        # Green bar for section title
        self.set_fill_color(34, 139, 34)
        self.set_text_color(255, 255, 255)
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, title, ln=True, align="L", fill=True)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def code_block(self, code):
        # Light purple background for code
        self.set_font("DejaVu", "", 9)
        self.set_fill_color(230, 230, 250)
        self.set_text_color(128, 0, 128)
        self.multi_cell(0, 5, code, fill=True)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def output_block(self, text):
        # Light yellow background for outputs
        self.set_font("DejaVu", "", 11)
        self.set_fill_color(255, 255, 204)
        self.set_text_color(0, 102, 0)
        self.multi_cell(0, 7, text, fill=True)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def table_block(self, table, col_widths=None, header_color=(0, 102, 204), row_color=(245, 245, 245)):
        # Calculate column widths if not provided
        if not col_widths:
            page_width = self.w - 2 * self.l_margin
            col_count = len(table[0])
            col_widths = [page_width / col_count] * col_count

        # Center table
        start_x = self.l_margin
        self.set_x(start_x)

        # Header
        self.set_font("DejaVu", "B", 10)
        self.set_fill_color(*header_color)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(table[0]):
            self.cell(col_widths[i], 8, header, border=1, align="C", fill=True)
        self.ln()
        self.set_font("DejaVu", "", 10)
        self.set_text_color(0, 0, 0)
        # Rows
        for idx, row in enumerate(table[1:]):
            self.set_x(start_x)
            self.set_fill_color(*(row_color if idx % 2 == 0 else (255, 255, 255)))
            for i, item in enumerate(row):
                self.cell(col_widths[i], 8, str(item), border=1, align="C", fill=True)
            self.ln()
        self.ln(2)

pdf = PDF()
pdf.add_font("DejaVu", "", "DejaVuSansMono.ttf", uni=True)
pdf.add_font("DejaVu", "B", "DejaVuSansMono.ttf", uni=True)
pdf.set_auto_page_break(auto=True, margin=15)

# --- COVER PAGE ---
pdf.add_page()
pdf.set_fill_color(0, 102, 204)
pdf.rect(0, 0, 210, 297, 'F')

pdf.image("apeejay_logo.png", x=pdf.w/2-50, y=35, w=100)

pdf.set_y(140)
pdf.set_font("DejaVu", "B", 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 20, "Apeejay School Saket", ln=True, align="C")

pdf.set_font("DejaVu", "B", 20)
pdf.cell(0, 15, "Arcade Zone Project Documentation", ln=True, align="C")

pdf.set_font("DejaVu", "", 14)
pdf.cell(0, 12, "A Python-based Arcade Management System", ln=True, align="C")

# Footer with names and session (move up so it's always visible)
pdf.set_y(230)
pdf.set_font("DejaVu", "B", 14)
pdf.cell(0, 10, "Prepared by:", ln=True, align="C")
pdf.set_font("DejaVu", "", 13)
pdf.cell(0, 8, "AYUSH RANJAN", ln=True, align="C")
pdf.cell(0, 8, "AYUSHMAAN GUPTA", ln=True, align="C")
pdf.set_font("DejaVu", "", 12)
pdf.cell(0, 8, "Session: 2025-26", ln=True, align="C")

# --- INDEX PAGE ---
pdf.add_page()
pdf.chapter_title("Index")
pdf.set_font("DejaVu", "", 12)
pdf.set_text_color(0, 0, 128)

# Use a table for index so it doesn't move out of page
index_items = [
    ("Introduction", "3"),
    ("Main Application File", "4"),
    ("Functions and Menus", "5"),
    ("Game Logic", "6"),
    ("Database Connection", "7"),
    ("Sample Outputs and Data", "8"),
    ("View All Users (Sample Data)", "9"),
    ("View All Scores (Sample Data)", "10"),
    ("View All Games", "11"),
    ("Player Menu Output", "12"),
    ("Sample Game Outputs", "13")
]
col_width = 120
page_width = pdf.w - 2 * pdf.l_margin
pdf.set_x(pdf.l_margin)
pdf.set_fill_color(230, 230, 250)
pdf.set_font("DejaVu", "B", 12)
pdf.cell(col_width, 8, "Section", border=1, align="L", fill=True)
pdf.cell(page_width-col_width, 8, "Page", border=1, align="C", fill=True)
pdf.ln()
pdf.set_font("DejaVu", "", 12)
for section, page in index_items:
    pdf.set_x(pdf.l_margin)
    pdf.cell(col_width, 8, section, border=1, align="L")
    pdf.cell(page_width-col_width, 8, page, border=1, align="C")
    pdf.ln()
pdf.set_text_color(0, 0, 0)
# --- Continue with rest of your PDF generation ---
# Introduction
pdf.add_page()
pdf.chapter_title("Introduction")
pdf.output_block(
    "Arcade Zone is a terminal-based arcade management system built in Python. "
    "It allows users to register, login, play classic games, and view their scores. "
    "Admins can manage users and view all scores. The project demonstrates database "
    "integration, menu-driven interfaces, and game logic.\n\n"
    "This documentation includes all source code, sample outputs, and data tables for reference."
)

# Add code from files
files = [
    ("mainframe_1.py", "Main Application File"),
    ("functions.py", "Functions and Menus"),
    ("games.py", "Game Logic"),
    ("db.py", "Database Connection"),
]

for fname, title in files:
    pdf.add_page()
    pdf.chapter_title(f"{title} ({fname})")
    with open(fname, "r", encoding="utf-8") as f:
        code = f.read()
    pdf.code_block(code)

# Sample Outputs
pdf.add_page()
pdf.chapter_title("Sample Outputs and Data")

pdf.output_block("Main Menu Output:\n"
                 "========================================\n"
                 "MAIN MENU\n"
                 "1. Login\n"
                 "2. Register\n"
                 "3. Exit\n"
                 "========================================\n")

pdf.output_block("Registration Output (Sample):\n"
                 "REGISTRATION\n"
                 "Enter your username (min 3 chars): johndoe\n"
                 "Enter your email: johndoe@example.com\n"
                 "Enter your mobile number (10 digits): 9876543210\n"
                 "Enter your password: ****\n"
                 "Re-enter your password: ****\n"
                 "Registration successful!\n")

pdf.output_block("Admin Menu Output:\n"
                 "ADMIN MENU\n"
                 "1. View all users\n"
                 "2. View all scores\n"
                 "3. View all games\n"
                 "4. Suspend a user\n"
                 "5. Logout\n")

# Table: View All Users (More Sample Data)
pdf.chapter_title("View All Users (Sample Data)")
user_table = [
    ["ID", "Name", "Email", "Mobile", "Password", "Role"],
    ["1", "admin", "arcadeworld@arcade.com", "9999999999", "admin@arc", "admin"],
    ["2", "johndoe", "johndoe@example.com", "9876543210", "pass1234", "player"],
    ["3", "alice", "alice@arcade.com", "9123456789", "alicepass", "player"],
    ["4", "bob", "bob@arcade.com", "9988776655", "bobpass", "player"],
    ["5", "eve", "eve@arcade.com", "9001122334", "evepass", "player"]
]
pdf.table_block(user_table, col_widths=[15, 30, 55, 30, 30, 25])

# Table: View All Scores (More Sample Data)
pdf.chapter_title("View All Scores (Sample Data)")
score_table = [
    ["UserID", "Game", "Score", "Time"],
    ["2", "battleship", "5", "2025-09-06 12:34:56"],
    ["2", "guess number", "10", "2025-09-06 12:40:12"],
    ["3", "rock paper scissors", "7", "2025-09-06 13:10:22"],
    ["4", "rpg", "20", "2025-09-06 13:15:45"],
    ["5", "blackjack", "5", "2025-09-06 13:20:10"],
    ["3", "battleship", "8", "2025-09-06 13:25:33"],
    ["4", "guess number", "12", "2025-09-06 13:30:01"],
    ["5", "rpg", "18", "2025-09-06 13:35:27"]
]
pdf.table_block(score_table, col_widths=[25, 55, 25, 55], header_color=(128, 0, 128), row_color=(230, 230, 250))

# Table: View All Games (Sample Data)
pdf.chapter_title("View All Games")
games_table = [
    ["Game ID", "Game Name", "Description"],
    ["1", "Battleship", "Guess the ship's location on a grid."],
    ["2", "Guess Number", "Guess a randomly generated number."],
    ["3", "Rock Paper Scissors", "Classic hand game against computer."],
    ["4", "RPG Battle Arena", "Fight monsters and use potions."],
    ["5", "BlackJack", "Card game against dealer."]
]
pdf.table_block(games_table, col_widths=[25, 45, 110], header_color=(0, 153, 153), row_color=(224, 255, 255))

pdf.output_block("Player Menu Output:\n"
                 "PLAYER MENU\n"
                 "1. Play Games\n"
                 "2. View Scores\n"
                 "3. Logout\n")

pdf.output_block("Sample Game Output (Battleship):\n"
                 "BATTLESHIP\n"
                 "Guess the ship's location (0-9)!\n"
                 "Attempts left 5. Enter your guess: 3\n"
                 "Miss!\n"
                 "Attempts left 4. Enter your guess: 7\n"
                 "Hit! You sunk the battleship!\n"
                 "Score saved! Your score: 5\n")

pdf.output_block("Sample Game Output (Guess the Number):\n"
                 "GUESS THE NUMBER\n"
                 "Guess the number between 1 and 100!\n"
                 "Attempts left 7. Enter your guess: 50\n"
                 "Too low!\n"
                 "Attempts left 6. Enter your guess: 75\n"
                 "Too high!\n"
                 "Attempts left 5. Enter your guess: 63\n"
                 "Congratulations! You guessed the number!\n"
                 "Score saved! Your score: 10\n")

pdf.output_block("Sample Game Output (Rock Paper Scissors):\n"
                 "ROCK PAPER SCISSORS\n"
                 "Round 1 of 5\n"
                 "Choose rock, paper, or scissors: rock\n"
                 "Computer chose: scissors\n"
                 "You win this round!\n"
                 "...\n"
                 "Game Over! Your score: 7\n"
                 "Score saved!\n")

pdf.output_block("Sample Game Output (RPG Battle Arena):\n"
                 "RPG BATTLE ARENA\n"
                 "A wild Goblin appears! Prepare for battle!\n"
                 "Your HP: 30 | Monster HP: 25 | Potions: 3\n"
                 "Choose your action:\n1. Attack\n2. Heal\n3. Run\n"
                 "Enter 1, 2, or 3: 1\n"
                 "You attack the monster for 6 damage!\n"
                 "The monster attacks you for 4 damage!\n"
                 "...\n"
                 "Congratulations! You defeated the monster!\n"
                 "Score saved! Your score: 20\n")

pdf.output_block("Sample Game Output (BlackJack):\n"
                 "BLACKJACK\n"
                 "Your cards: [10, 7] (Total: 17)\n"
                 "Dealer's first card: 9\n"
                 "Type 'hit' to get another card, or 'stand' to hold: stand\n"
                 "Dealer's cards: [9, 8] (Total: 17)\n"
                 "It's a draw!\n"
                 "Score saved! Your score: 5\n")

pdf.output("arcade_zone_documentation.pdf")
print("PDF generated: arcade_zone_documentation.pdf")