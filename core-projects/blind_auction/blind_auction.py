import art
auction={}
cont = 'y'
print(art.logo)
while cont != 'n' and cont != 'N':
    name = input("Bidder name: ")
    amount = int(input("Bidder amount: "))
    auction[name] = amount
    cont = input("Are there any other bidders [Y|N]? ")

bid = 0
bidder = ""
for name in auction:
    if auction[name]>bid:
        bidder = name
        bid = auction[name]

print(f"\nThe highest bidder is {bidder} with {bid} Euro.")
