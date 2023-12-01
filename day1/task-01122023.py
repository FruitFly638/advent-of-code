import re

number_dictionary = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
number_words ="one|two|three|four|five|six|seven|eight|nine"
numbers = []
regex = re.compile(f'(\d|{number_words})(?:.*)(\d|{number_words})|(\d|{number_words})')
with open("01122023.txt") as file:
    for line in file:
        trimmed = regex.search(line)
        if trimmed:
            trimmed = trimmed.group()

            first = trimmed[0]
            last = trimmed[-1]
            if not first.isdigit():
                first = re.compile(number_words).match(trimmed).group()
                first = number_dictionary[first]
            if not last.isdigit():
                last = re.compile(f"({number_words})$").search(trimmed).group()
                last = number_dictionary[last]
            number = int(f'{first}{last}')
            numbers.append(number)
      

sum = 0
for number in numbers:
    sum += number

print(sum)

#re.compile("one|two|three|four|five|six|seven|eight|nine")