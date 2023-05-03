# ex 2.3.3 - pigs
bricks_amount = input("Enter three digits (each digit for one pig): ")
total_bricks = sum(int(digit) for digit in bricks_amount)
num = 3
each_pig_bricks = total_bricks // num
lefted_bricks = total_bricks % num
flag = (total_bricks % 3 == 0)
print(total_bricks)
print(each_pig_bricks)
print(lefted_bricks)
print(flag)

#ex 3.2.1
print('"Shuffle, Shuffle, Shuffle", say it together!\nChange colors and directions,\nDon\'t back down and stop the player!\n\t\tDo you want to play Taki?\n\t\tPress y\\n')

#ex 3.3.3
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
decoded_message = encrypted_message[::-2].replace("X", "")
print(decoded_message) #I am Alexander the Prince

#ex 3.4.2
str = input("Please enter a string: ")
first_char = str[0]
new_str = first_char + str[1:].replace(first_char, 'e')
print(new_str)

#ex 3.4.3
str2 = input("Please enter a string: ")
half_size = len(str2) // 2
result = str2[:half_size].lower() + str2[half_size:].upper()
print(result)

#ex 4.2.2
word = input("Enter a word: ").replace(" ", "").lower()
if word == word[::-1]:
    print("OK")
else:
    print("NOT")

#ex 4.2.3
temp = input("Enter the temperature you would like to convert: ")
if temp[-1].lower() == 'c':
    # C to F
    c = float(temp[:-1])
    f = (c * 9 / 5) + 32
    print(f"{f}F")

elif temp[-1].lower() == 'f':
    # F to C
    f = float(temp[:-1])
    c = (f - 32) * 5 / 9
    print(f"{c}C")
else:
    print("Invalid input. Please enter a valid temperature followed by C or F.")

#ex 4.2.4
import calendar
date_str = input("Enter a date (dd/mm/yyyy): ")
day, month, year = map(int, date_str.split('/'))
weekday = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday]
print(weekday_name)

#ex 5.3.4
def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    if my_str.count(last_char) > 1:
        return True
    else:
        return False

#ex 5.3.5
def distance(num1, num2, num3):
    if abs(num2 - num1) <= 1 and abs(num3 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    elif abs(num2 - num3) <= 1 and abs(num1 - num2) >= 2 and abs(num1 - num3) >= 2:
        return True
    elif abs(num3 - num1) <= 1 and abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2:
        return True
    else:
        return False

#ex 5.3.6
def fix_age(age):
    if age >= 13 and age <= 19 and age != 15 and age != 16:
        return 0
    else:
        return age

def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c

#ex 5.3.7
def chocolate_maker(small, big, x):
    max_big_cubes = x // 5
    if big > max_big_cubes:
        big = max_big_cubes
    remaining_space = x - big * 5
    if small >= remaining_space:
        return True
    else:
        return False

#ex 5.4.1
def func(num1, num2):
    #This function takes in two numbers and returns their sum.
    return num1 + num2
# def main():
#     result = func(3, 4)
#     print(result)
#
# if __name__ == "__main__":
#     main()

#ex 6.1.2
def shift_left(my_list):
    return my_list[1:] + [my_list[0]]

#ex 6.2.3
def format_list(my_list):
    return ", ".join(my_list[::2][:-1]) + ", and " + my_list[-1]

#ex 6.2.4
def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

#ex 6.3.1
def are_lists_equal(list1, list2):
    return sorted(list1) == sorted(list2)

#ex 6.3.2
def longest(my_list):
    return max(my_list, key=len)

#ex 7.1.4
def squared_numbers(start, stop):
    result = []
    num = start
    while num <= stop:
        result.append(num**2)
        num += 1
    return result

#ex 7.2.1
def is_greater(my_list, n):
    return [x for x in my_list if x > n]

#ex 7.2.2
def numbers_letters_count(my_str):
    num_count = 0
    char_count = 0
    for char in my_str:
        if char.isdigit():
            num_count += 1
        elif char.isalpha() or char.isspace():
            char_count += 1
    return [num_count, char_count]

#ex 7.2.4
def seven_boom(end_number):
    result = []
    for i in range(end_number + 1):
        if i % 7 == 0 or '7' in str(i):
            result.append('BOOM')
        else:
            result.append(i)
    return result

#ex 7.2.5
def sequence_del(my_str):
    result = my_str[0]
    for i in range(1, len(my_str)):
        if my_str[i] != my_str[i-1]:
            result += my_str[i]
    return result

#ex 7.2.6
def print_products(products):
    print("List of products:")
    for product in products:
        print(product)

def print_num_products(products):
    print(f"Number of products: {len(products)}")

def is_product_in_list(products):
    product_name = input("Enter product name: ")
    if product_name in products:
        print(f"{product_name} is in the list")
    else:
        print(f"{product_name} is not in the list")

def count_product_occurrences(products):
    product_name = input("Enter product name: ")
    occurrences = products.count(product_name)
    print(f"{product_name} appears {occurrences} times")

def delete_product(products):
    product_name = input("Enter product name to delete: ")
    if product_name in products:
        products.remove(product_name)
        print(f"{product_name} has been removed from the list")
    else:
        print(f"{product_name} is not in the list")

def add_product(products):
    product_name = input("Enter product name to add: ")
    products.append(product_name)
    print(f"{product_name} has been added to the list")

def print_invalid_products(products):
    invalid_products = [product for product in products if len(product) < 3 or not product.isalpha()]
    if invalid_products:
        print("Invalid products:")
        for product in invalid_products:
            print(product)
    else:
        print("No invalid products")

def remove_duplicates(products):
    unique_products = list(set(products))
    print("List with duplicates removed:")
    for product in unique_products:
        print(product)

# def main():
#     products_string = input("Enter a comma-separated list of products: ")
#     products = products_string.split(",")
#     while True:
#         print("Menu:")
#         print("1. Print list of products")
#         print("2. Print number of products")
#         print("3. Is product in list?")
#         print("4. Count product occurrences")
#         print("5. Delete product")
#         print("6. Add product")
#         print("7. Print invalid products")
#         print("8. Remove duplicates")
#         print("9. Exit")
#
#         choice = input("Enter your choice (1-9): ")
#
#         if choice == "1":
#             print_products(products)
#         elif choice == "2":
#             print_num_products(products)
#         elif choice == "3":
#             is_product_in_list(products)
#         elif choice == "4":
#             count_product_occurrences(products)
#         elif choice == "5":
#             delete_product(products)
#         elif choice == "6":
#             add_product(products)
#         elif choice == "7":
#             print_invalid_products(products)
#         elif choice == "8":
#             remove_duplicates(products)
#         elif choice == "9":
#             break
#         else:
#             print("Invalid choice, try again")
#
# if __name__ == "__main__":
#     main()

#ex 7.2.7
def arrow(my_char, max_length):
    result = []
    for i in range(1, max_length + 1):
        line = my_char * i
        result.append(line)
        if i == max_length:
            for j in range(max_length - 1, 0, -1):
                line = my_char * j
                result.append(line)
    return '\n'.join(result)

#ex 8.2.1
data = ("self", "py", 1.543)
format_string = "Hello {}.{} learner, you have only {:.1f} units left before you master the course!"
print(format_string.format(data[0], data[1], data[2]))

#8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)

#ex 8.2.3
def mult_tuple(tuple1, tuple2):
    return tuple((x, y) for x in tuple1 for y in tuple2)

#ex 8.2.4
def sort_anagrams(list_of_strings):
    anagram_dict = {}
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())

#ex 8.3.2
mariah_carey = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

user_input = int(input("Enter a number between 1 and 7: "))

if user_input == 1:
    print(mariah_carey["last_name"])
elif user_input == 2:
    print(mariah_carey["birth_date"].split(".")[1])
elif user_input == 3:
    print(len(mariah_carey["hobbies"]))
elif user_input == 4:
    print(mariah_carey["hobbies"][-1])
elif user_input == 5:
    mariah_carey["hobbies"].append("Cooking")
    print(mariah_carey["hobbies"])
elif user_input == 6:
    birth_date_parts = mariah_carey["birth_date"].split(".")
    birth_date_tuple = (int(birth_date_parts[0]), int(birth_date_parts[1]), int(birth_date_parts[2]))
    print(birth_date_tuple)
elif user_input == 7:
    from datetime import datetime
    birth_date_string = mariah_carey["birth_date"]
    birth_date = datetime.strptime(birth_date_string, "%d.%m.%Y")
    age = (datetime.now() - birth_date).days // 365
    mariah_carey["age"] = age
    print(mariah_carey["age"])

#ex 8.3.3
def count_chars(my_str):
    char_counts = {}
    for char in my_str.replace(" ", ""):
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

#ex 8.3.4
def inverse_dict(my_dict):
    inverse = {}
    for key, value in my_dict.items():
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    for value in inverse.values():
        value.sort()
    return inverse

#ex 9.1.2
def sort_words(file_path):
    with open(file_path) as f:
        words = set(f.read().split())
        return sorted(words)

def reverse_lines(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
        for line in lines:
            print(line[::-1])

def last_lines(file_path, n):
    with open(file_path) as f:
        lines = f.read().splitlines()
        for line in lines[-n:]:
            print(line)

file_path = input("Enter a file path: ")
task = input("Enter a task: ")

if task == "sort":
    print(sort_words(file_path))

elif task == "rev":
    reverse_lines(file_path)

elif task == "last":
    n = int(input("Enter a number: "))
    last_lines(file_path, n)

#ex 9.2.2
def copy_file_content(source, destination):
    with open(source, 'r') as source_file, open(destination, 'w') as destination_file:
        destination_file.write(source_file.read())

#ex 9.2.3
def who_is_missing(file_name):
    with open(file_name) as f:
        sequence = set(map(int, f.read().split(',')))
    full_sequence = set(range(1, max(sequence) + 1))
    missing_number = sorted(full_sequence - sequence)[0]
    with open("found.txt", "w") as f:
        f.write(str(missing_number))
    return missing_number

#ex 9.3.1
def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        songs = f.readlines()

    # Find longest song
    longest_song_length = -1
    longest_song_name = ""
    for song in songs:
        song_details = song.strip().split(";")
        song_length = song_details[2]
        song_length_in_sec = int(song_length.split(":")[0])*60 + int(song_length.split(":")[1])
        if song_length_in_sec > longest_song_length:
            longest_song_length = song_length_in_sec
            longest_song_name = song_details[0]

    # Find number of songs in file
    num_songs = len(songs)

    # Find operation that appears the most number of times
    operation_count = {}
    for song in songs:
        song_details = song.strip().split(";")
        operation_name = song_details[1]
        if operation_name in operation_count:
            operation_count[operation_name] += 1
        else:
            operation_count[operation_name] = 1

    max_count = -1
    most_common_operation = ""
    for operation_name, count in operation_count.items():
        if count > max_count:
            max_count = count
            most_common_operation = operation_name

    return (longest_song_name, num_songs, most_common_operation)

#ex 9.3.2
def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    while len(lines) < 3:
        lines.append('\n')
    lines[2] = f"{new_song};Unknown;\n"
    with open(file_path, 'w') as f:
        f.writelines(lines)
    with open(file_path, 'r') as f:
        print(f.read())











