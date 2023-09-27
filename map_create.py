map = []

while True:
    a = input()
    if a == 'gg':
        break
    maps_line = []
    for i in a:
        maps_line.append(i)
    map.append(maps_line)

print(map)
