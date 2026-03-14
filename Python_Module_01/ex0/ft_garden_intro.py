class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("rose", 25, 30)

if __name__ == "__main__":
    rose.name = rose.name.capitalize()
    print("=== Welcome to My Garden ===")
    print(f"Plant: {rose.name}")
    print(f"Height: {rose.height}cm")
    print(f"Age: {rose.age} days\n")
    print("=== End of Program ===")

# (Shebang #!) line: "#!/usr/bin/env python3"
# Makes our file executable
# Needs only to change its mode (chmod +x file.py)
# Then you can run it with ./file.py
