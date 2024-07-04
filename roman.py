def roman_to_integer(s):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0  # Initializing total to zero
    i = 0  # Used to track the loop

    while i < len(s):  # using example as s = "CMIX"
        if i + 1 < len(s) and roman_values[s[i + 1]] > roman_values[s[i]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]  # Subtracting the values
            i = i + 2
        else:
            total += roman_values[s[i]]
            i = i + 1

    print(total)

s = "CMIX"
roman_to_integer(s)


