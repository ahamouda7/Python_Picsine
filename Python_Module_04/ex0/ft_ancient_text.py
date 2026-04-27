if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()

        file = None
        file = open("ancient_fragment.txt")  # "r" is by default
        print(f"Accessing Storage Vault: {file.name}")
        print("Connection established...")
        print()

        print("RECOVERED DATA:")
        print(file.read())
        print()

        print("Data recovery complete. Storage unit disconnected.")

    except Exception as e:
        print(f"ERROR: {e}")

    finally:
        if file:
            file.close()
