def isPalindrome(number):

    #Edge Case
    if number < 0:
        return False

    original = number  # Copy the original from number
    reversed_number = 0  # Initialize number to 0
    while number > 0:  # Iterate of the number while it is zero
        last_digit = number % 10  # Get the modulus of number
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10  # get the floor number after dividing by 10

    return  original == reversed_number  # Return true if the reversed number equals to original

print(isPalindrome(-1))
print(isPalindrome(121))