# Q. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
# 60 copies?
cover_price = 24.95
discount = 0.4  # 40% discount
num_books = 60

#Calculate wholesale price per book after discount
wholesale_price = cover_price * (1 - discount)


num_additional_copies = num_books - 1
shipping_cost_additional = num_additional_copies * 0.75

#Calculate total shipping cost (first copy + additional copies)
total_shipping = 3 + shipping_cost_additional

#Calculate total wholesale cost
total_cost = wholesale_price * num_books + total_shipping

#Print the total cost
print("The total wholesale cost for 60 copies is:", total_cost)

#output: The total cost for 60 copies is: 945.4499999999