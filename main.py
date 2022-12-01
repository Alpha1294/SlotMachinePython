
import random


MIN_BET = 10
MAX_BET = 100
MAX_LINES = 3

ROWS = 3
COLLS = 3

symbol_value = {
    "A": 3,
    "B": 6,
    "C": 9,
    "D": 12}

symbol_count = {
    "A": 8,
    "B": 6,
    "C": 5,
    "D": 4}


def deposit():
    while True:
        cash = input(
            "Insert the ammount of money you will have to play with  ")
        if cash.isdigit():
            cash = int(cash)
            if cash > 0:
                break
            else:
                print("Number must be positive")
        else:
            print("You must insert a number")
    return cash


def number_of_lines():
    while True:
        num_lines = input(
            "Number on lines to bet on ,must be between 1 and 3 \n")
        if num_lines.isdigit():
            num_lines = int(num_lines)
            if num_lines > 0 and num_lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and 3")
        else:
            print("You must insert a number")
    return num_lines


def get_bet():
    while True:
        bet = input("How much do you want to bet on each line?")
        if bet.isdigit():
            bet = int(bet)
            if bet > MIN_BET and bet < MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("The bet must be a number")
    return bet


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # -items() gives you both the key and the value asociated with a dictionary
    for symbol, symbol_count in symbols.items():
        # if the symbol count is 3 ,we add that symbol 3 times in the all_symbols list
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # " : " is to copy the list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def spin(cash):
    num_lines = number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * num_lines

        if total_bet > cash:
            print(f"You dont have enough money,your current balance is " + cash)
        else:
            break

    print("This is your money")
    print(f"You bet on " + str(num_lines) + " lines")

    slots = get_slot_machine_spin(COLLS, ROWS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(
        slots, num_lines, bet, symbol_value)
    print(f"You won {winnings}$.")
    # splat or unpack operator , pass every single line of this winning lines list to this print function
    print(f"You won on lines :", *winning_lines)

    return winnings - total_bet


def main():
    cash = deposit()
    while True:
        print(f"Current balance is ${cash}")
        answer = input("Press enter to spin or q to quit")
        if answer == "q":
            break
        cash += spin(cash)

    print(f"you left with ${cash}")


main()
