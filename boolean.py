"""This program converts a base-10 number between 1 and 99
to a written out form of the number in English"""

print("enter a number between 1 and 99")

num = int(input())

tens = num // 10
ones = num % 10

if tens == 9:
    tens_word = 'ninety'
elif tens == 8:
    tens_word = 'eighty'
# more code goes here
if ones == 9:
    ones_word = 'nine'
elif ones == 8:
    ones_word = 'eight'
# more code goes here
if tens == 0:
    output = ones_word
else:
    output = tens_word + '-' + ones_word

print(output)
