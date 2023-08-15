messsage = 'Hello, this is vishw joshi here. I am current studying in A D Patel institute of technology'

count = {}

for character in messsage:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)