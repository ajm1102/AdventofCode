f = open("Day2Input.txt", "r")
content = f.read().split(',')

for i in content:
    command = i.split()
lst2 = []
c = 0
a = 0
b = 1
depth = 0
distance = 0
aim = 0
underwater = False

while c < len(command):
    if aim != 0:
        underwater = True
    if command[a] == "forward":
        distance = distance + int(command[b])
        print(underwater)
        if underwater:
            depth = depth + (int(command[b]) * aim)
    elif command[a] == "down":
        aim = aim + int(command[b])
    elif command[a] == "up":
        aim = aim - int(command[b])


    a = a + 2
    b = b + 2
    c = c + 2
answer = depth * distance

print(answer)