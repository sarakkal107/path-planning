# Any Angle Path Planning

# To run A* algorithm, use the command-line argument: 
# The small.txt file can be replaced with an other input file
# Use "aStar" to run A* and "thetaStar" to run Theta*

python3 main.py small.txt aStar

python3 main.py small.txt thetaStar

# to generate tests

python3 main.py generateTest aStar filePath
python3 main.py generateTest thetaStar filePath