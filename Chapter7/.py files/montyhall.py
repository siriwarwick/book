import matplotlib.pyplot as plt
from random import choice

sims = 1e5
Ndoors = 3

listsims = range(int(sims))
round1 = range(Ndoors)

staywin, switchwin = 0, 0
Pstay = []
Pswitch = []

for i in listsims:
    car = choice(round1)
    pick1 = choice(round1) 
    
    monty = [n for n in round1 
             if n!= car and n!= pick1]
    goat = choice(monty)

    round2 = [n for n in round1 
              if n!= pick1 and n!=goat]
    pick2 = choice(round2)

    if pick1==car: staywin += 1
    if pick2==car: switchwin +=1
    
    p1 = staywin/(i+1)
    p2 = switchwin/(i+1)
    Pstay.append(p1)
    Pswitch.append(p2)
    
plt.semilogx(listsims, Pstay, 'r', 
             listsims, Pswitch, 'b')
plt.text(5e3, 0.36, f'Pr(win if stay)={p1:.3}')
plt.text(5e3, 0.7,f'Pr(win if switch)={p2:.3}')
plt.xlim([10, sims])
plt.ylim([0,1])
plt.xlabel('Number of simulations')
plt.ylabel('Probability of winning')
plt.title('Monty Hall simulations with 3 doors')
plt.grid('on')
plt.show()
