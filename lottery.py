import random

def generate_numbers(n):
    ran_num = []
    while len(ran_num) != n:    
        pick = random.randint(1,45)
        if pick not in ran_num:
            ran_num.append(pick)            
    return ran_num

# print(generate_numbers(7))

def draw_winning_numbers():
    winning_num = generate_numbers(7)
    return sorted(winning_num[:6]) + winning_num[6:]

# print(draw_winning_numbers())

def count_matching_numbers(num, win_num):
    count_match = 0
    for i in range(6):
        if num[i] in win_num:
            count_match += 1
    return count_match

# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

def check(num, win_num):
    count = count_matching_numbers(num, win_num[:6])
    bonus_count = count_matching_numbers(num, win_num[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]

# print(check(numbers_test, winning_numbers_test))
# numbers_test = [2, 4, 11, 14, 25, 40]
# winning_numbers_test = [2, 4, 10, 11, 14, 40, 25]

# print(check(numbers_test, winning_numbers_test))
