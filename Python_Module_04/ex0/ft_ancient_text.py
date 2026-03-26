if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()

        file = None
        file = open("ancient_fragment.txt", "r")
        print(f"Accessing Storage Vault: {file.name}")
        print("Connection established...")
        print()

        print("RECOVERED DATA:")
        print(file.read())
        file.close()
        print()

        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("file doesn't have the premission to be read")
        if file:
            file.close()
