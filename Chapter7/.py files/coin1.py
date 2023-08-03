import numpy as np
import matplotlib.pyplot as plt
import random 

exprmt = int(1e5)
throws = 10
Htally = []

for i in range(exprmt):
    heads= 0
    for trial in range(throws):
        roll = random.randint(0, 1)
        if roll == 0: heads += 1
    Htally.append(heads)

bins = np.arange(throws+2)-0.5
prob, b1, b2 = plt.hist(Htally, bins= bins, 
                        density = True)
plt.xticks(range(11))
plt.xlabel('No. of heads in 10 throws')
plt.ylabel('Probability')
plt.grid('on')
plt.show()

print(f'Pr(5 heads)= {prob[5]}')
print(f'Pr(at least 5 heads)= {sum(prob[5:])}')
