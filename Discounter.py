def price_maker(price): 
 if price == 0:
    return 'What a wonderful world'
 if price > 0 and price <= 20:
    price = price - (price * (20/100))
    return price
 elif price > 20 and price <= 50:
    price = price - (price * (40/100))
    return price
 elif price > 50 :
    price = price - (price * (60/100))
    return price

prices = input('please enter your prices seperated by commas : ').split(",")

new_prices = []
for n in prices:
    new_prices.append(price_maker(float(n)))


    
print(new_prices)


chaos = ["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []
for n in chaos:
    if 'old' in n :
         order.append(price_maker(float(n.split(':')[1])))
    elif 'new'in n :
        order.append(float(n.split(':')[1]))
print(order)

