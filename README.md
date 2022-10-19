# Any Angle Path Planning

# To run A* algorithm, use the command-line argument: 
# The small.txt file can be replaced with an other input file
# Our hand-written test files are in the file non_generated_grids and our generated test files are in the folder experiment
# Use "aStar" to run A* and "thetaStar" to run Theta*

python3 main.py non_generated_grids/small.txt aStar

python3 main.py non_generated_grids/small.txt thetaStar

python3 main.py experiment/test1.txt aStar

python3 main.py experiment/test1.txt thetaStar

# to generate tests

python3 main.py generateTest aStar filePath
python3 main.py generateTest thetaStar filePath

# to run experiments
# This experiment generates a bar graph of the average A* runtimes and the average Theta* runtimes
python3 run_experiments_aStarVsTheta.py

# This experiment generates a bar graph of the changes to optimize the runtime in our A* script.
python3 run_experiments_runtimes.py

# This experiment generates a bar graph of the difference in runtimes of the memory-focused script and the efficiency-focused one
python3 run_experiments_runtimes_runtimes.py
