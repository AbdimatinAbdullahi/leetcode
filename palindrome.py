def isPalindrome(number):

    #Edge Case
    if number < 0:
        return False

    original = number
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10

    return  original == reversed_number

print(isPalindrome(-1))
print(isPalindrome(121))