bidders = {}
bid_amounts = []
print("Welcome to the secret auction program!")
while True:
  bidder_name = input("What is your name? ")
  bidder_bid = int(input("What is your bid? "))
  bidders[bidder_name] = bidder_bid
  bid_amounts.append(bidder_bid)
  another_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if another_bidder == 'no':
    bid_amounts.sort(reverse = True)
    for k in bidders.keys():
      if bidders[k] == bid_amounts[0]:
        print(f'The winner is {k} with a bid of {bid_amounts[0]}')
        break
    break
  else:
    clear()
