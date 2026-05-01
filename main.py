def decayed_followers(initial_followers, fraction_lost_daily, days):
    total = initial_followers
    for n in range(days):
        total -= total * fraction_lost_daily

    return total
