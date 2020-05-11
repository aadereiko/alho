class Thing:
    def __init__(self, c, w, price):
        self.c = c
        self.w = w
        self.price = price

    def __repr__(self):
        return f'{self.c} {self.w} {self.price}'

def insert_thing(things, thing):
    if not len(things):
        return 0

    for i in range(0, len(things)):
        if things[i].price < thing.price:
            return i

    return len(things)

amount, capacity = map(int, input().split())
things = []
for _ in range(0, amount):
    c, w = map(int, input().split())
    if not(c == 0 or w == 0):
        thing = Thing(c, w, c / w)
        index = insert_thing(things, thing)
        things[index:index] = [thing]

# filling bagpack with things
result = 0
for i in range(0, len(things)):
    if capacity <= 0 or not len(things):
        break

    if capacity >= things[i].w:
        capacity -= things[i].w
        result += things[i].c
    else:
        things_to_fill = things[i].price * capacity
        result += things_to_fill
        capacity = 0

print(f'{result:.3f}')
