def num_possible_orders(num_posts):
    product = 1
    for n in range(2, num_posts + 1):
        product *= n
    return product