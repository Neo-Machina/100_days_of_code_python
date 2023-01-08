from art import logo

print(logo)

bidders = {}


def get_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    name = input("What is your name?: ")
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid
    other_bidders = input(
        "Are there any other bidders? Type 'yes or 'no'.\n").lower()

    while other_bidders != "yes" and other_bidders != "no":
        other_bidders = input(
            "Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if other_bidders == 'no':
        get_highest_bid(bidding_record=bidders)
        break