def letter_combinations(digits):
    if not digits:
        return []
    
    result = [""]

    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")
        
        new_result = []
        print(f"letters: {digit} = {digit_to_letters[digit]}")
        for combo in result:
            for letter in digit_to_letters[digit]:
                new_result.append(combo + letter)

        result = new_result

    return result








# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
