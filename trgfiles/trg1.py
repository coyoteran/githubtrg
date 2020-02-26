# This variable contains an integer
quantity = 14
# This variable contains a float
unit_price = 26.99
# This variable contains the result of multiplying the two
extended_price = quantity * unit_price
purchase_price = round(extended_price,2)
oct_price = oct(extended_price)
# This shows the price
print(extended_price)
print(purchase_price)
print(oct_price)