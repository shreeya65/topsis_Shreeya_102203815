import sys
import pandas as pd
import numpy as np

def validate_inputs(input_file, weights, impacts):
    # Check if the file exists
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{input_file}' not found.")

    # Check if input file has at least three columns
    if len(df.columns) < 3:
        raise ValueError("Error: Input file must contain at least three columns.")

    # Check if 2nd to last columns are numeric
    if not all([np.issubdtype(df.iloc[:, 1:].dtypes[i], np.number) for i in range(len(df.columns) - 1)]):
        raise ValueError("Error: All columns from the 2nd to last must contain numeric values.")

    # Check if weights and impacts have the correct length
    num_criteria = len(df.columns) - 1
    weights_list = [float(w) for w in weights.split(",")]
    impacts_list = impacts.split(",")

    if len(weights_list) != num_criteria or len(impacts_list) != num_criteria:
        raise ValueError("Error: Number of weights and impacts must match the number of criteria.")

    # Check if impacts are valid (+ or -)
    if not all(impact in ["+", "-"] for impact in impacts_list):
        raise ValueError("Error: Impacts must be '+' or '-'.")

    return df, weights_list, impacts_list

def topsis(df, weights, impacts):
    # Normalize the decision matrix
    normalized_df = df.iloc[:, 1:].copy()
    for column in normalized_df.columns:
        column_norm = np.sqrt(sum(normalized_df[column]**2))
        normalized_df[column] = normalized_df[column] / column_norm

    # Apply weights
    weighted_df = normalized_df * weights

    # Determine ideal best and worst
    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == "+":
            ideal_best.append(weighted_df.iloc[:, i].max())
            ideal_worst.append(weighted_df.iloc[:, i].min())
        else:
            ideal_best.append(weighted_df.iloc[:, i].min())
            ideal_worst.append(weighted_df.iloc[:, i].max())

    # Calculate the distances to ideal best and worst
    distances_best = np.sqrt(((weighted_df - ideal_best)**2).sum(axis=1))
    distances_worst = np.sqrt(((weighted_df - ideal_worst)**2).sum(axis=1))

    # Calculate the TOPSIS score
    topsis_score = distances_worst / (distances_best + distances_worst)

    # Add score and rank to the DataFrame
    df["Topsis Score"] = topsis_score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    return df

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    result_file = sys.argv[4]

    try:
        # Validate inputs and load data
        df, weights_list, impacts_list = validate_inputs(input_file, weights, impacts)

        # Perform TOPSIS
        result_df = topsis(df, weights_list, impacts_list)

        # Save the result to the output file
        result_df.to_csv(result_file, index=False)
        print(f"Results saved to '{result_file}'")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
