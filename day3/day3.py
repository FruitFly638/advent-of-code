import string

def number_finder(idx, idy):
    while True:
        if not list_lines[idx][idy-1] in string.digits:
            break
        idy = idy - 1
        
    number = int(list_lines[idx][idy])
    position = idy

    while True:
        if not list_lines[idx][idy+1] in string.digits:
            break
        idy = idy + 1
        number = number * 10 + int(list_lines[idx][idy])
    return [position, number]

list_lines = []
sum = 0
with open("input.txt") as file:
    for line in file:
        list_lines.append(line)
        #print(line, end = "")

# part 1
for idx, line in enumerate(list_lines):
    in_number = False
    valid_number = False
    number_length = 0
    location = 0
    number = 0
    for idy, char in enumerate(line):
        if(char in string.digits):
            if(not in_number):
                location = idy
                in_number = True
            number = number * 10 + int(char)
            number_length = number_length + 1
            
        if(not char in string.digits and in_number):
            #print(f"Number found: {number} at Location [{idx}][{location}], Length: {number_length}")
            in_number = False
            
            if idx-1 >= 0:
                for i in range(location-1, location + number_length +1):
                    try:
                        if(list_lines[idx-1][i] in string.punctuation and not list_lines[idx-1][i] == "."):
                            valid_number = True
                    except:
                        pass
            if idx+1 < len(list_lines):
                for i in range(location-1, location + number_length + 1):
                    #print(f"{list_lines[idx+1][i]} at location {i}")
                    try:
                        if(list_lines[idx+1][i] in string.punctuation and not list_lines[idx+1][i] == "."):
                            valid_number = True
                    except:
                        pass

            if(location - 1 >= 0):
                if (list_lines[idx][location-1] in string.punctuation and not list_lines[idx][location-1] == "."):
                    valid_number = True
            if(location+number_length < len(line)):
                #print(list_lines[idx][location+number_length])
                if (list_lines[idx][location+number_length] in string.punctuation and not list_lines[idx][location+number_length] == "."):
                   valid_number = True

            if(valid_number):
                sum = sum + number
                #print(f"Valid number: {number}")
            valid_number = False
            number = 0
            in_number = False
            number_length = 0

# part 2
gears_sum = 0
for idx, line in enumerate(list_lines):
    for idy, char in enumerate(line):
        if char == "*":
            numbers = []
            for i in range(idy - 1, idy + 2):
                if list_lines[idx + 1][i] in string.digits:
                    number = number_finder(idx + 1, i)
                    if number not in numbers:
                        numbers.append(number)
                if list_lines[idx - 1][i] in string.digits:
                    number = number_finder(idx - 1, i)
                    if number not in numbers:
                        numbers.append(number)
            if line[idy-1] in string.digits:
                number = number_finder(idx, idy - 1)
                if number not in numbers:
                    numbers.append(number)
            if line[idy+1] in string.digits:
                number = number_finder(idx, idy + 1)
                if number not in numbers:
                    numbers.append(number)
            if len(numbers) == 2:
                gears_sum = gears_sum + numbers[0][1]*numbers[1][1]

print(sum)
print(gears_sum)
