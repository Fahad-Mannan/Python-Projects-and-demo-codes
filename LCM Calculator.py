''' Welcome to the Least Common Multiple calculator.
Just run the program and put as many values as you want.
This will Find the LCM of those values for you. '''


############## input Loop ################
print('*** Welcome to the LCM counter! Please Enter your values and I will count the LCM for you! ***')
print()
n = ''
num_lst = []
input_serial = 1
while n == '':
    Input = int(input(f'enter value {input_serial}: '))
    if Input <= 0:
        print('Please enter positive integer only')
    else:
        num_lst.append(Input)
        input_serial = input_serial + 1
    n = input('for next value press "enter" or press any key to stop: ')

print('your values are: ', num_lst)


############## LCM Loop ###############

product_of_num_list = 1
for i in range(len(num_lst)):
    product_of_num_list = product_of_num_list * num_lst[i]


# print(b)
breaking_point = 0
for i in range(1, product_of_num_list+1):
    if breaking_point == 1:
        break
    for j in num_lst:
        if i % j == 0:
            if j == num_lst[-1]:
                print('LCM: ', i)
                breaking_point = 1
                break
            continue
        else:
            break
