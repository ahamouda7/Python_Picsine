import importlib.util


def check_dependencies() -> bool:
    packages = ["pandas", "numpy", "matplotlib"]
    all_good = True

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            print(f"[KO] {pkg} is not installed.")
            all_good = False
        else:
            module = importlib.import_module(pkg)
            print(f"[OK] {pkg} ({module.__version__})")

    return all_good


def run_matrix_analysis() -> None:
    try:
        import numpy
        import pandas
        import matplotlib.pyplot as matplot
    except ImportError:
        print("[ERROR] A package didn't install")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    matrix_data = numpy.random.rand(1000)
    pandas_df = pandas.DataFrame(matrix_data)

    print("Generating visualization...")

    matplot.figure(figsize=(10, 6))
    matplot.plot(pandas_df.index, pandas_df, color='green', linewidth=0.5)
    matplot.title("Matrix Signal Analysis")
    matplot.xlabel("Data Points")
    matplot.ylabel("Signal Strength")

    matplot.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def compare_package_managers() -> None:
    print("\n" + "=" * 62)
    print(" MATRIX ARCHITECTURE: PIP vs POETRY")
    print("=" * 62)

    print("[pip]: The Drone Installer")
    print("  -> Installs requested packages (requirements.txt)")
    print("     without checking if they perfectly match each other.")
    print("  -> Can break projects by installing new versions)")
    print("     of hidden dependencies.")

    print("[poetry]: The Architect")
    print("  -> Smarter than pip. Checks if all packages and the Python")
    print("     version are suitable together before start to download.")
    print("  -> Uses a 'poetry.lock' file: a 100% mathematically")
    print("     identical snapshot of your system.")
    print("=" * 62)


def main() -> None:
    if check_dependencies():
        run_matrix_analysis()
    else:
        print("\n[ERROR]: Missing required programs.")

        print(" Hint: To load your all packages, run:")
        print("=" * 39)
        print("$ pip install -r requirements.txt")
        print("=" * 35)
        print(" or:")
        print("=" * 18)
        print("$ poetry install")
        print("=" * 18)

    compare_package_managers()


if __name__ == "__main__":
    main()
