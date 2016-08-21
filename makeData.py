import csv
from scipy import stats

def main():
	with open("data.csv", "w") as fo:
		writer = csv.writer(fo)
		for i in range(100000):
			x = stats.poisson.rvs(100)
			y = stats.poisson.rvs(200)
			writer.writerow([x, y])


if __name__ == "__main__":
	main()