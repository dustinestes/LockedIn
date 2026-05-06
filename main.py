def merge_sort(nums: list):
    length = len(nums)
    middle = length // 2

    if length < 2:
        return nums

    a, b = nums[:middle], nums[middle:]
    print(f"a: {a}")
    print(f"b: {b}")
    c, d = merge_sort(a), merge_sort(b)

    return merge(c, d)


def merge(first, second):
    result = []

    i = 0
    j = 0

    for f in range(i, len(first)):
        for s in range(j, len(second)):
            if first[f] <= second[s]:
                result.append(first[f])
                i += 1
                break
            else:
                result.append(second[s])
                j += 1

    if i < len(first):
        result = result + first[i::]
    if j < len(second):
        result = result + second[j::]

    return result
