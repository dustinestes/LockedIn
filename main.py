import math

def log_scale(data, base):
    new_list = []
    for n in data:
        new_list.append(math.log(n, base))

    return new_list