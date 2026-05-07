def count_marketers(job_titles):
    count = 0

    for x in job_titles:
        if str.lower(x) == "marketer":
            count += 1

    return count