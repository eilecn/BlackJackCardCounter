import random
import time

count = 0
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['♣', '♦', '♥', '♠']

deck = []

for i in range(len(numbers)):
    for j in range(len(suits)):
        deck.append(str(numbers[i] + ' of ' + suits[j]))

NumberOfCards = ''
while NumberOfCards.isdigit() is False:
    NumberOfCards = input("Number of cards to count (1-52): \n")
NumberOfCards = int(NumberOfCards)

SecondsBetweenCards = ''
while isinstance(SecondsBetweenCards, float) is False:
    SecondsBetweenCards = float(input("Number of seconds between cards: \n"))

print('\n' * 20)
for i in range(int(NumberOfCards)):
    card = random.choice(deck)
    deck.remove(card)
    if card[0] in ['2', '3', '4', '5', '6']:
        count += 1
    elif card[0] in ['1', 'J', 'Q', 'K']:
        count -= 1

    print(card)
    time.sleep(SecondsBetweenCards)
    print('\n' * 20)

UserGuess = input("Your final count: \n")

if int(UserGuess) is count:
    print("Good Job! The number was " + str(count) + ".")
else:
    print("You lose, the final count was " + str(UserGuess) + ".")

