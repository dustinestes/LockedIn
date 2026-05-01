def get_follower_prediction(follower_count, influencer_type, num_months):
    count = 0
    match influencer_type:
        case "fitness":
            count = follower_count * (4 ** num_months)
        case "cosmetic":
            count = follower_count * (3 ** num_months)
        case _:
            count = follower_count * (2 ** num_months)
    
    return count