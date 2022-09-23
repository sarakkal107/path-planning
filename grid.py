import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def read_input():
    f = open("input.txt", "r")
    contents = f.readlines()
    start = list(map(int, contents[0].strip().split(" ")))
    end = list(map(int, contents[1].strip().split(" ")))
    size = list(map(int, contents[2].strip().split(" ")))

    data = np.full([size[1], size[0]], np.nan)
    i = 3

    while i < len(contents):
        temp = list(map(int, contents[i].strip().split(" ")))
        if (temp[2] == 1):
            data[temp[1]-1][temp[0]-1] = 1
        i += 1
    generate_grid(size[1], size[0], data, start, end)


def generate_grid(x, y, data, start, end):
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    my_cmap = matplotlib.colors.ListedColormap(['grey'])
    my_cmap.set_bad(color='w', alpha=0)
    for x in range(x+1):
        ax.axhline(x, lw=2, color='k', zorder=5)
    for y in range(y+1):
        ax.axvline(y, lw=2, color='k', zorder=5)

    ax.imshow(data, interpolation='none', cmap=my_cmap,
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
    ax.scatter(end[0]-1, x-end[1]+1, s=50, zorder=50, label="End")
    ax.legend()
    plt.axis('off')
    plt.show()
