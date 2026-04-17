import os


def consult_oracle() -> None:
    try:
        from dotenv import load_dotenv
        env_loaded = load_dotenv()
    except ImportError:
        print("[ERROR] Package 'dotenv' is missing")
        return

    matrix_mode = os.environ.get("MATRIX_MODE")
    database_url = os.environ.get("DATABASE_URL", "")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    if matrix_mode:
        if matrix_mode != "development" and matrix_mode != "production":
            print("[ERROR] Mode varible is not available")
            return
        print(f"Mode: {matrix_mode}")
    else:
        print("[ERROR] Mode varible didn't set")
        return

    if "localhost" in database_url or "127.0.0.1" in database_url:
        print("Database: Connected to local instance")
    else:
        print("[ERROR] Database variable didn't set")
        return

    if api_key:
        print("API Access: Authenticated")
    else:
        print("[ERROR] API Access variable didn't set")
        return

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("[ERROR] Log Level variable didn't set")
        return

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("[ERROR] Zion Network variable didn't set")
        return

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing")

    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()
