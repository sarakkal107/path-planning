from re import search
import gui
import sys
import grid
import optimizedMemorySearchAlgos
import nonOptimizedRuntimeSearchAlgos
import searchAlgos
import time
import statistics
import matplotlib.pyplot as plt
import matplotlib

# gui.start_gui()

# grid.generate_grid(3, 4)


file = open('testPathFile.txt', 'r')
lines = file.readlines()
opt_runtimes_list = []
non_opt_runtimes_list = []
average_opt_tests = []
average_non_opt_tests = []
adjacents = {}
adjacents2 = {}

algoType = sys.argv[1]


for count in range(0,10):
    for line in lines:
        filePath = line.strip()
        startTime = time.time()
        start, goal, size, data, visualizeData = grid.read_input(filePath)
        goalVertex = searchAlgos.algosMain(start, goal, data, size, adjacents, algoType)
        runTime = time.time() - startTime
        opt_runtimes_list.append(runTime)


    for line in lines:
        filePath = line.strip()
        startTime = time.time()
        start, goal, size, data, visualizeData = grid.read_input(filePath)
        goalVertex = nonOptimizedRuntimeSearchAlgos.algosMain(start, goal, data, size, adjacents, algoType)
        runTime = time.time() - startTime
        non_opt_runtimes_list.append(runTime)

    print("\n")
    print(opt_runtimes_list)
    average_runtimes = statistics.mean(opt_runtimes_list)
    average_opt_tests.append(average_runtimes)
    print("\n")

    print("\n")
    print(non_opt_runtimes_list)
    average_runtimes = statistics.mean(non_opt_runtimes_list)
    average_non_opt_tests.append(average_runtimes)
    print("\n")


print("\n")
print(average_opt_tests)
average_opt_results = (statistics.mean(average_opt_tests))
print(average_opt_results)
print("\n")

print("\n")
print(average_non_opt_tests)
average_non_opt_results = (statistics.mean(average_non_opt_tests))
print(average_non_opt_results)
print("\n")

equations = ['Runtimes with Optimization','Runtimes without Optimization']
times = [average_opt_results,average_non_opt_results]

fig = plt.figure()
 
# creating the bar plot
plt.bar(equations,times, color ='blue', width = 0.4)
 
plt.xlabel(algoType + " Algorithms")
plt.ylabel("Average Runtime")
plt.title("Difference in Runtimes")
plt.savefig("RuntimeAnalysis" + algoType + ".png")
plt.show()

