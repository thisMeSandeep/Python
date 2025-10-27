"""Dictionary comprehension"""

prices={
    "Apple":100,
    "Banana":40,
    "Oranges":60,
}

prices_in_usd = { product:str(price/80)+'$'  for product,price in prices.items() }
print(prices_in_usd)