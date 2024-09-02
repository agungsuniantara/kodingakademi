import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)

dealer = []
player = []

def deal_initial_cards():
    global dealer
    global player
    dealer = [draw_card(), draw_card()]
    player = [draw_card(), draw_card()]

def draw_card():
    return cards.pop()

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            value += 10
        elif card == "A":
            num_aces += 1
            value += 11
        else:
            value += int(card)

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def player_turn():
    while True:
        print(f"Your hand: {player}")
        choice = input("Do you want to hit or stand? ").lower()

        if choice == 'hit':
            player.append(draw_card())
            player_value = calculate_hand_value(player)

            if player_value > 21:
                print("Bust! You went over 21. You lose.")
                return 'bust'
        elif choice == 'stand':
            return 'stand'
        else:
            print("Invalid choice. Please enter 'hit' or 'stand.'")

def main():
    print("Welcome to Blackjack!")

    deal_initial_cards()
    player_result = player_turn()

    if player_result != 'bust':
        # Implement dealer's turn and determine the winner
        pass

if __name__ == "__main__":
    main()
