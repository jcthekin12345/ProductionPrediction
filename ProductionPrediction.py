
while True:
    production = int(input("Current Production:"))
    production_increase = int(input("Sales increase: "))

    print(f"Increase Production to {production + production:,.2f}")
    if input() == "e":
        break
