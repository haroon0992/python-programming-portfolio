#  Vending Machine Program

products = {
    1: ("Cola", 2.50),
    2: ("snickers", 2.00),
    3: ("oreo", 1.25),
    4: ("Water", 1.00)
}

def display_menu():
    print("\n====== VENDING MACHINE ======")
    for num, item in products.items():
        print(f"{num}. {item[0]} - ${item[1]:.2f}")
    print("5. Exit")

while True:
    display_menu()

    try:
        option = int(input("Select a product number: "))
    except ValueError:
        print(" Please enter numbers only.")
        continue

    if option == 5:
        print("Thank you for using the vending machine!")
        break

    if option not in products:
        print(" Invalid product selection.")
        continue

    product_name, product_price = products[option]
    print(f"\nYou selected: {product_name}")
    print(f"Price: ${product_price:.2f}")

    total_paid = 0.0

    while total_paid < product_price:
        try:
            money = float(input("Insert money: $"))
            if money <= 0:
                print(" Insert a positive amount.")
                continue

            total_paid += money
            print(f"Total inserted: ${total_paid:.2f}")

            if total_paid < product_price:
                print(" Insufficient funds, please insert more money")

        except ValueError:
            print("Invalid input. Numbers only.")

    change = total_paid - product_price
    print(f"\nDispensing {product_name}")

    if change > 0:
        print(f"Returning change: ${change:.2f}")

    print("Please collect your item.\n")
