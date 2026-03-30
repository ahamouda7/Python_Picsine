if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print()

        file = None
        file = open("new_discovery.txt", "w")
        print(f"Initializing new storage unit: {file.name}")
        print("Storage unit created successfully...")
        print()

        print("Inscribing preservation data...")
        data = (
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n"
        )
        file.write(data)
        print(data)
        print()

        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except Exception as e:
        print(f"ERROR: {e}")

    finally:
        if file:
            file.close()
