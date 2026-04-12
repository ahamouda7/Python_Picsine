import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    try:
        print(f"Testing create_earth: {alchemy.create_earth()}")
    except Exception as e:
        print(f"🔴 AttributeError: {e}")
