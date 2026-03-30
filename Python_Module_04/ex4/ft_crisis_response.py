def access_archive(file_name: str, alert_type: str) -> None:
    try:
        print(f"{alert_type}: Attempting access to '{file_name}'...")
        with open(file_name):
            print(
                "SUCCESS: Archive recovered - Knowledge preserved for humanity"
                )
            print("STATUS: Normal operations resumed")
            print()

    except Exception as e:
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, system stable")
        print()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    access_archive("lost_archive.txt", "CRISIS ALERT")
    access_archive("classified_vault.txt", "CRISIS ALERT")
    access_archive("standard_archive.txt", "ROUTINE ACCESS")

    print("All crisis scenarios handled successfully. Archives secure.")
