#Task-1
import pandas as pd
import numpy as np

def generate_car_matrix(task1):
    df = pd.read_csv(taxk1)
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    np.fill_diagonal(car_matrix.values, 0)
    return car_matrix

# Example usage
taxk1 = 'dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)
