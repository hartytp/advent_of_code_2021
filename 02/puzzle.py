with open('data.txt') as file:
    data = file.read().splitlines()
# data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

data = ';'.join(data)
data = (data.replace('forward', 'position +=')
            .replace('down', 'depth +=')
            .replace('up', 'depth -='))

depth = 0
position = 0
exec(data)
print(f"Day 2: position {position}, depth {depth}, product {position*depth}")
