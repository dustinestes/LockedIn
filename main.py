def get_avg_brand_followers(all_handles, brand_name):
    total_handles = 0
    len_handles_list = len(all_handles)

    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                total_handles += 1
        
    return total_handles / len_handles_list
