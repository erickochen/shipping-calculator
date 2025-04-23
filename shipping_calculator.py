# Simple shipping cost calculator
def calculate_shipping_cost(weight_grams):
    if weight_grams <= 500:
        return 4.95
    elif weight_grams <= 2000:
        return 6.95
    else:
        return 9.95

weight = float(input("Enter the weight of the package in grams: "))
cost = calculate_shipping_cost(weight)
print(f"Shipping cost: €{cost}")
