
START_POINT = 50
test_path = "test1.txt"
file_path = "input1.txt"
with open(test_path, 'r') as file:
    lines = file.readlines()

when_left_on_zero = []
current = START_POINT
for line in lines:
    direction = line[0]
    number = int(''.join(i for i in line if i.isdigit()))
    print(direction, number)
    if direction == 'R':
        if current 
        current = (current + number) % 100
    elif direction == 'L':
        current = (current - number) % 100 
    when_left_on_zero.append((line, current))

print(when_left_on_zero)
print("result is: ", len(when_left_on_zero))
