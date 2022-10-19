
import gui
import sys

# gui.start_gui()

# grid.generate_grid(3, 4)
typeInput = True
inputFile = sys.argv[1]
if inputFile == "generateTest":
    typeInput = False
    filePath = sys.argv[3]
else:
    filePath = inputFile

typeOfAlgo = sys.argv[2]

gui.App(typeInput, typeOfAlgo, filePath)





