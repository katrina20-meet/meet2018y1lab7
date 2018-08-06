
def add_numbers(start, end):
    
    c = 0
    for number in range(start, end+1):
        print(number)
        c = c + number
    return(c)



test1 = add_numbers(333, 777)
print(test1)

