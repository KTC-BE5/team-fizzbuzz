print('it works')
for i in range(1,101):
    if(i%3 == 0):
        print('Fizz')
    if (i%5) == 0:
        print("buzz")
    if i % 15 == 0:
        print('fizzbuzz')
    else:
        print(i)
