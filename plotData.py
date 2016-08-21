import numpy as np
import matplotlib.pyplot as plt
import csv

def readFile(fl):
	x = []
	y = []
	with open(fl, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)
			x.append(int(row[0]))
			y.append(int(row[1]))
	return np.array(x), np.array(y)


def plotScatter(x, y):
	heatmapMatrix = np.zeros((max(x)+1, max(y)+1))
	for i, j in zip(x, y):
		heatmapMatrix[i][j] += 1
	plt.imshow(heatmapMatrix)
	plt.savefig("plot.png")
	plt.show()


def main():
	x, y = readFile("data.csv")
	plotScatter(x, y)


if __name__ == "__main__":
	main()