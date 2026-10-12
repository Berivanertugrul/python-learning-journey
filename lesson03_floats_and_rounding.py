
 #float

temperature = 35.5
product_price = 1999.99
print(temperature)


#Decimal precision 

print(0.1+0.2)    #0.30000000000000004

# Round (yuvarlama)

result = 0.1 + 0.2
print(result)

rounded_result = round(result , 2)   #0.3
print(rounded_result)

## Calculate VAT (20%) based on the given price

price = float (input ("Please enter the price: "))
print(price)

percent = 20

price_with_vat = price + price*percent/100
print(price_with_vat)