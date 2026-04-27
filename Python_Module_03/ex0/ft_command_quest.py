import sys


def print_args() -> None:
    for i in range(1, len(sys.argv)):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print_args()
    print(f"Total arguments: {len(sys.argv)}")
