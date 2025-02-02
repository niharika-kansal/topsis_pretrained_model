
import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):
    # Load data from CSV
    data = pd.read_csv(input_file)

    # Validate data
    if len(weights) != (data.shape[1] - 1):
        raise ValueError("Number of weights does not match number of criteria.")
    if len(impacts) != (data.shape[1] - 1):
        raise ValueError("Number of impacts does not match number of criteria.")
    if not set(impacts).issubset({'+', '-'}):
        raise ValueError("Impacts must be '+' or '-'.")
    
    # Normalize data
    normalized_data = data.iloc[:, 1:].apply(
        lambda col: col / np.sqrt(sum(col**2)), axis=0
    )
    
    # Apply weights
    weighted_data = normalized_data * weights

    # Determine ideal best and worst
    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(weighted_data.iloc[:, i].max())
            ideal_worst.append(weighted_data.iloc[:, i].min())
        else:
            ideal_best.append(weighted_data.iloc[:, i].min())
            ideal_worst.append(weighted_data.iloc[:, i].max())

    # Calculate distances to ideal best and worst
    distance_to_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    distance_to_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))

    # Calculate TOPSIS score
    scores = distance_to_worst / (distance_to_best + distance_to_worst)

    # Rank models
    data['Topsis Score'] = scores
    data['Rank'] = scores.rank(ascending=False).astype(int)

    # Save output
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
