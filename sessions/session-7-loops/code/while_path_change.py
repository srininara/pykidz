fruits = ['apple', 'apricot', 'banana', 'chickoo', 'fig', 'guava', 'mango', 'orange']
while fruits:
    fruit = fruits.pop()
    if fruit == 'chickoo':
        print(fruit, "! Yuck... I will skip this one")
        continue
    print("I love", fruit)

print("I am done!")