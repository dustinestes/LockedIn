def exponential_growth(n, factor, days):
    result = [n]

    for _ in range(days):
        result.append(result[-1] * factor)

    return result