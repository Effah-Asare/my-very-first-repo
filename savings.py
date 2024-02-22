amount_saved = 0

while amount_saved <= 100:
    money_made = int(input("How much did you make today: "))
    amount_to_save = money_made * 0.4
    if money_made < 20:
        print(f"Your earnings for today is not sufficient. We were able to save {amount_saved} for now. However, Let us pause on savings for now")
        break
    amount_saved += amount_to_save
print(f"We have managed to save up to {amount_saved}")


