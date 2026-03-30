import sys


if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
        print()

        ID = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")
        print()

        print(f"[STANDARD] Archive status from {ID}: {status}")
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr
            )
        print("[STANDARD] Data transmission complete")
        print()

        print("Three-channel communication test successful.")

    except Exception as e:
        print(f"ERROR: {e}")
