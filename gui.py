import grid
from classes.Vertex import Vertex
import optimizedMemorySearchAlgos
import searchAlgos
import matplotlib.pyplot as plt
import matplotlib


class App():

    def __init__(self, inputOrTest, typeOfAlgo,inputFileOrTestPath):

        adjacents = {}
        if (inputOrTest):
            start, goal, size, data, visualizeData = grid.read_input(inputFileOrTestPath)
        else:
            start, goal, size, data, visualizeData = grid.generate_test(inputFileOrTestPath)
        
        x, y = size[1], size[0]
        if (typeOfAlgo == 'aStar'):
            title = "A* Algorithm"
        else:
            title = "Theta* Algorithm"

        goalVertex = searchAlgos.algosMain(start, goal, data, size,adjacents, typeOfAlgo)
        # adjacents = {}
        # goalVertex = initialSearchAlgos.algosMain(start, goal, data, size, adjacents, typeOfAlgo)
        if goalVertex == None:
            print("No path found")
            return None
        if (typeOfAlgo == 'aStar'):
            title = "A* Algorithm"
        else:
            title = "Theta* Algorithm"
        x, y = size[1], size[0]
        fig, ax = plt.subplots(1, 1, tight_layout=True)
        fig.suptitle(title, fontsize=20)
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
        ax.scatter(start[0]-1, x-start[1]+1, s=100,
                   zorder=50, label="Start", clip_on=False)
        ax.scatter(goal[0]-1, x-goal[1]+1, s=100,
                   zorder=50, label="Goal", clip_on=False)
        ax.legend()
        plt.axis('off')

        current = goalVertex
        print("Path from Goal to Start")
        #print(str(size[0]) + " : " + str(size[1]))
        while (current.coords != start):
            currentParent = current.parent
            currentCoords = current.coords
            parentCoords = currentParent.coords
            x1 = currentCoords[0]
            y1 = currentCoords[1]
            x2 = parentCoords[0]
            y2 = parentCoords[1]
            print([x1,y1])


            a = plt.plot([x1-1, x2-1], [size[1]-y1+1, size[1]-y2+1],
                         zorder=50, color='red', linewidth=3, linestyle='dashed', clip_on=False)
            current = currentParent
        print(start)
        plt.savefig("wrongThetaStar2.png")
        plt.show()