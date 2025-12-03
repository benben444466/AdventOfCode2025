file_path = "input1.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

START_POINT = 50

when_left_on_zero = []
current = START_POINT
for line in lines:
    direction = line[0]
    number = int(''.join(i for i in line if i.isdigit()))

    if direction == 'R':
        current = (current + number) % 99 
    elif direction == 'L':
        current = (current - number) % 99
    if current == 0:
        when_left_on_zero.append(line) 

print("result is: ", len(when_left_on_zero))




    