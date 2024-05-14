import random

requests = []
for i in range(1000):
    requests.append(random.randint(0, 4999))

with open('requests.txt', 'w') as file:
    for r in requests:
        file.write(str(r) + '\n')