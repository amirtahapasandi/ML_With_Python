user_item = int(input("What's the price of your item? "))
discount_percent = int(input("What is the discount percentage of your product? "))

discounted_product_price = (((user_item * discount_percent) // 100) - user_item)
print(f"The price of your product with a discount: {discounted_product_price * -1}")
