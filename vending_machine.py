def calculate_change(paid, price):
    change = price - paid
    return change
snacks_price = 25
print("===== SNACKS VENDING MACHINE =====")
print(f"THIS SNACKS COST {snacks_price} Rs.")
print("ACCEPTABLE COINS :  1, 5, 10, 25\n")
total_coins_inserted = 0
inserted_coins = 0
while True:
    coin = int(input("INSERT A COIN (1, 5, 10, 25!) : "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25 :
        print("INVALED COINs INSERTED!, TRY AGAIN")
        continue
    total_coins_inserted += coin
    inserted_coins += 1
    print(f"INSERTED COIN {coin}.TOTAL SO FAR {total_coins_inserted}.")
    if total_coins_inserted > snacks_price:
        print("ENOUGH COINS INSERTED!\n")
        break
    change_due = calculate_change (total_coins_inserted, snacks_price)
    print("DISPENSING YOUR SNACKS...")
    if change_due == 0:
        pass
    else :
        print(f"HERE IS YOUR CHANGE : {change_due}\n")
        print("===== PURCHASE SUMMARY =====")
        print("SNACKS PRICE : ", snacks_price)
        print("COINS INSERTED : ", inserted_coins)
        print("TOTAL PAID : ", total_coins_inserted)
        print("CHANGE GIVEN : \n", change_due)
        print("===== THANKS FOR YOUR PURCHANSE =====")