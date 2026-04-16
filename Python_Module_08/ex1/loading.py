import sys
import importlib.util

def check_dependencies():
    packages = ["pandas", "numpy", "matplotlib"]
    all_good = True

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            print(f"[MISSING] {pkg} is not installed.")
            all_good = False
        else:
            module = importlib.import_module(pkg)
            print(f"[OK] {pkg} ({module.__version__})")

    return all_good

def run_matrix_analysis():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    matrix_data = np.random.rand(1000)
    df = pd.DataFrame(matrix_data, columns=['Matrix_Signal'])

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Matrix_Signal'], color='green', linewidth=0.5)
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Signal Strength")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

def main():
    if check_dependencies():
        run_matrix_analysis()
    else:
        print("\nERROR: Missing required programs.")
        print("To load your weapons, run:")
        print("pip install -r requirements.txt")
        print("OR")
        print("poetry install")

if __name__ == "__main__":
    main()