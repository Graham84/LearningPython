price = 100                                 # GBP, no VAT
final_price1 = price * 1.2
final_price2 = price + price / 5.0
final_price3 = price * (100 + 20) / 100.0
final_price4 = price + price * 0.2

# vat function
def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100

