"""
hello.py - A simple greeting module with enhanced functionality.
"""

def hello(name: str = "World") -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def greet_multiple(names: list[str]) -> list[str]:
    """Return greeting messages for a list of names."""
    return [hello(name) for name in names]


def main() -> None:
    """Main entry point for the script."""
    print(hello())
    print(hello("Python Developer"))

    team = ["Alice", "Bob", "Charlie"]
    for greeting in greet_multiple(team):
        print(greeting)


if __name__ == "__main__":
    main()
