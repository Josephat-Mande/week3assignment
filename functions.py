def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        # Apply the discount
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        # No discount applied
        return price

# prompt the user for input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)
    print(f"Final price after discount: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values for price and discount percentage.")

