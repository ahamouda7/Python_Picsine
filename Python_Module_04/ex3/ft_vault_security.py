if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()

    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r+") as file:
            print("Vault connection established with failsafe protocols")
            print()

            print("SECURE EXTRACTION:")
            print(file.read())
            print()

            print("SECURE PRESERVATION:")
            new_data = (
                "[CLASSIFIED] New security protocols archived\n"
                "Vault automatically sealed upon completion"
                )
            file.write("\n" + new_data)
            print(new_data)
            print()

        print("All vault operations completed with maximum security.")

    except Exception as e:
        print(f"Error: {e}")
