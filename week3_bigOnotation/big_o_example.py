lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]


for l in lst:
    print(l, end=" ")

tot = 0
num_elem = 0
for l in lst:
    tot += l
    num_elem += 1
    
print("\nmean: ", tot / num_elem)

for l in range(1000):
    for j in range(1000):
        for k in range(1000):
            for m in range(1000):
                print(l * j * k * m, end=" ")
                 