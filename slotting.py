import random

def spinrow():
    symbols = ['🏆', '☠️', '🥳', '🍾', '💵']
    return [random.choice(symbols) for _ in range(3)]

def printrow(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def getpayout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥳':
            return bet * 3
        elif row[0] == '💵':
            return bet * 6
        elif row[0] == '🍾':
            return bet * 2
        elif row[0] == '☠️':
            return bet
        elif row[0] == '🏆':
            return bet * 4
    return 0

def main():
    balance = 100
    print("********************")
    print("Welcome to Coin Slot!")
    print("Symbols: 🏆 ☠️ 🥳 🍾 💵")
    print("********************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet
        print("Spinning...\n")
        row = spinrow()
        printrow(row)
        payout = getpayout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("lmfao loser aahhh")

        balance += payout
        playagain = input("Do you want to spin again? Type 'Y' to continue: ").strip().upper()
        if playagain != 'Y':
            break

    print("Thanks for playing. Bye!")

if __name__ == '__main__':
    main()