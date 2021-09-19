icecream_flavors = ['vanilla', 'chocolate', 'mint chocolate', 'chocolate chip', 'cookie dough']
fruits = ['apple', 'banana', 'fig', 'mango', 'orange']
flavor_index = 0
print('The combination are:')
while flavor_index < len(icecream_flavors):
    fruit_index = 0
    flavor = icecream_flavors[flavor_index]
    flavor_index += 1
    if flavor == 'mint chocolate':
        continue
    while fruit_index < len(fruits):
        fruit = fruits[fruit_index]
        fruit_index += 1
        if fruit == 'banana':
            continue
        print(f"{flavor} - {fruit}")

print("Good bye!")