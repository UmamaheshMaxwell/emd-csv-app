import csv
import numpy as np
from scipy.spatial.distance import euclidean
from pyemd import emd


def read_csv(file_path, num_lines=1000):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for i, row in enumerate(reader):
            if i >= num_lines:
                break
            data.append(float(row[0]))
    return data


def calculate_emd(dataset1, dataset2):
    dataset1 = np.array(dataset1, dtype=np.float64)
    dataset2 = np.array(dataset2, dtype=np.float64)

    dataset1 /= np.sum(dataset1)
    dataset2 /= np.sum(dataset2)

    distance_matrix = np.zeros((len(dataset1), len(dataset2)))
    for i in range(len(dataset1)):
        for j in range(len(dataset2)):
            distance_matrix[i, j] = euclidean([i, 0], [j, 0])

    emd_value = emd(dataset1, dataset2, distance_matrix)
    return emd_value


csv_file1 = "gretel_1.csv"
csv_file2 = "gretel_2.csv"

dataset1 = read_csv(csv_file1)
dataset2 = read_csv(csv_file2)

emd_distance = calculate_emd(dataset1, dataset2)
print(f"Earth Mover's Distance: {emd_distance}")