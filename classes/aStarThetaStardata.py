import ast
import matplotlib.pyplot as plt
import matplotlib
import statistics



thetaPaths = [9,10,3,3,6,5,4,3,7,4,3,6,4,3,5,3,8,3,4,3,6,5,3,6,4,3,4,5,5,3,6,6,4,5,3,5,3,5,3,6,5,5,6,4,4,4,3,11,6,4]

aStarPaths = [46,53,62,56,24,31,27,55,37,63,25,32,25,57,41,35,58,38,63,26,61,88,20,23,53,42,17,43,81,39,37,96,17,87,31,60,59,24,24,57,39,30,44,22,39,29,26,91,70,25]
x = []
for count in range (1,51):
    x.append(str(count))

fig = plt.figure()
 
# creating the bar plot
plt.plot(thetaPaths)
plt.xlabel("Grid Number")
plt.ylabel("Number of Vertices in Path")
plt.title("Theta* Algorithm")
plt.grid(True)
plt.savefig("ThetaPaths.png")
plt.show()
plt.close()

plt.plot(aStarPaths)
plt.xlabel("Grid Number")
plt.ylabel("Number of Vertices in Path")
plt.title("A* Algorithm")
plt.grid(True)
plt.savefig("APaths.png")
plt.show()

thetaStar_results = (statistics.mean(thetaPaths))
aStar_results = (statistics.mean(aStarPaths))
print(thetaStar_results)
print(aStar_results)
results = [aStar_results,thetaStar_results]
names = ['Average A* Path Length','Average Theta* Path Length']
plt.bar(names,results, color ='blue', width = 0.4)
plt.xlabel("A* vs Theta*")
plt.ylabel("Average Path Size")
plt.title("Difference in Path Sizes")
plt.savefig("averageThetaStarAstar.png")
plt.show()