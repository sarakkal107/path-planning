# Any Angle Path Planning

# To run A* and Theta* algorithms, use the command-line argument: 
# The small.txt file can be replaced with an other input file
# Our hand-written test files are in the file non_generated_grids and our generated test files are in the folder experiment
# Use "aStar" to run A* and "thetaStar" to run Theta*
The searchAlgorithms.py script is our implementation of the Theta* and A*. As we print the H, F, and G values to the console in our implementation, we used scripts that had the same functions but did not print the values to the console. This was in order to test the runtimes of trying to find the goal vertex, and the time needed to print would have messed with the results and depicted the runtimes as being closer than they should have been.

python3 main.py non_generated_grids/small.txt aStar

python3 main.py non_generated_grids/small.txt thetaStar

python3 main.py experiment/test1.txt aStar

python3 main.py experiment/test1.txt thetaStar

# to generate test grids

python3 main.py generateTest aStar filePath
python3 main.py generateTest thetaStar filePath

# to run experiments
This experiment generates a bar graph of the average A* runtimes and the average Theta* runtimes:

python3 run_experiments_aStarVsTheta.py

This experiment generates a bar graph of the changes to optimize the runtime in our A* script:

python3 run_experiments_runtimes.py aStar
python3 run_experiments_runtimes.py thetaStar

This experiment generates a bar graph of the difference in runtimes of the memory-focused script and the efficiency-focused one:

python3 run_experiments_runtimes_runtimes.py aStar
python3 run_experiments_runtimes_runtimes.py thetaStar

# This script generates a visibility graph of the input file and finds the true shortest path:
The small.txt file can be replaced with an other input file:

python3 visibilityGraph.py non_generated_grids/small.txt 

