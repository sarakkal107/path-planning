import tk
import grid
from classes.Vertex import Vertex
import searchAlgos
import matplotlib.pyplot as plt
import matplotlib

def start_gui():
    window = tk.Tk()
    window.minsize(200, 200)
    window.title("Path Planning")
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    window.mainloop()

class App():

    def __init__(self, inputFile, typeOfAlgo):


        start, goal, size, data, visualizeData = grid.read_input(inputFile)

        adjacents = {}
        goalVertex = searchAlgos.algosMain(start, goal, data, size, adjacents, typeOfAlgo)
        print("finished Algo")
        if goalVertex == None:
            print("No path found")
            return
        
        x,y = size[1], size[0]
        fig, ax = plt.subplots(1, 1, tight_layout=True)
        my_cmap = matplotlib.colors.ListedColormap(['grey'])
        my_cmap.set_bad(color='w', alpha=0)
        for x in range(x+1):
            ax.axhline(x, lw=2, color='k', zorder=5)
        for y in range(y+1):
            ax.axvline(y, lw=2, color='k', zorder=5)

        ax.imshow(visualizeData, interpolation='none', cmap=my_cmap,
              extent=[0, y, 0, x], zorder=0)

        plt.locator_params(axis="x", nbins=x+1)
        plt.locator_params(axis="y", nbins=y+1)

        locs, labels = plt.xticks()
        labels = [int(item)+1 for item in locs]
        plt.xticks(locs, labels)

        locs, labels = plt.yticks()
        z = len(locs)
        labels = [z-int(item) for item in locs]
        plt.yticks(locs, labels)

        ax.xaxis.tick_top()
        ax.scatter(start[0]-1, x-start[1]+1, s=50, zorder=50, label="Start")
        ax.scatter(goal[0]-1, x-goal[1]+1, s=50, zorder=50, label="End")
        ax.legend()
        plt.axis('off')

        current = goalVertex
     
        while (current.coords != start):
            currentParent = current.parent
            currentCoords = current.coords
            parentCoords = currentParent.coords
            x1 = currentCoords[0]
            y1 = currentCoords[1]
            x2 = parentCoords[0]
            y2 = parentCoords[1]
       
            a = plt.plot([x1,size[0]-y1+1],[x2,size[0]-y2+1], zorder=100, color='red')
            current = currentParent

        plt.show()
        

    
