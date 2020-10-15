''' Here you will get any prime number by just putting it's position.
 For example: If your input is 1, you will get 2
              If your input is 2, you will get 3
              If your input is 3, you will get 5, and so on.

 This will also show how many seconds your machine took to calculate it. Put some big Numbers and Have fun! '''


import time

print('*** Welcome to Prime fetcher! I will fetch the prime number for you. Just tell me the position!***')
print()
x = int(input('Enter position of the prime: '))
start = time.time()
if x == 0 or x < 0:
    print('please enter an positive integer')

if x == 1:
    print(2)


n = 1
i = 3
while x > n:
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            if j == i-1:
                n = n + 1
        if n == x:
            print(i)
            end = time.time()

    i = i + 1
print('It required %.10f' % (end - start), 'sec for me to finish the task')

