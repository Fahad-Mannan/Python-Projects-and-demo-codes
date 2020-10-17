'''Welcome to the "Greatest Common Factor" counter!
Just run the program and put as many values as you want.
This will Find the GCF of those values for you.'''


##################### Input Loop #####################
print('Welcome to the GCF counter! Please Enter your values and I will count the GCF for you!')

n = ''
input_serial = 1
num_lst = []
while n == '':
    Input = int(input(f'Please enter value {input_serial}: '))
    if Input >= 0:
        num_lst.append(Input)
        input_serial = input_serial + 1
    else:
        print('Please enter positive integer only')

    n = input('For next value press "enter" or press any key to stop: ')


print('Your values are: ', num_lst)

#################### GCF Calculating portion ####################


min_of_num_list = min(num_lst)

# print(min_of_num_list)

break_point = 0

for i in range(min_of_num_list, 0, -1):
    if break_point == 1:
        break
    for j in num_lst:
        if j % i == 0:
            if j == num_lst[-1]:
                print('GCF: ', i)
                break_point = 1
                break
            continue
        else:
            break

###########################################
