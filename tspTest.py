import random, numpy, math, copy, matplotlib.pyplot as plt
#cities = [random.sample(range(100), 2) for x in range(15)]
cities = [(1,1),(1,2),(1,3),(1,5),(10,20),(32,50),(12,20),(10,25),(59,60),(20,80),(80,50),(70,20),(10,10),(15,20),(56,40)]
tour = random.sample(range(15),15)
for temperature in numpy.logspace(0,5,num=100000)[::-1]:
	[i,j] = sorted(random.sample(range(15),2))
	newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:]
	if math.exp( ( sum([ math.sqrt(sum([(cities[tour[(k+1) % 15]][d] - cities[tour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(cities[newTour[(k+1) % 15]][d] - cities[newTour[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
		tour = copy.copy(newTour)
plt.plot(zip(*[cities[tour[i % 15]] for i in range(16) ])[0],zip(*[cities[tour[i % 15]] for i in range(16) ])[1], 'xb-', )
plt.show()