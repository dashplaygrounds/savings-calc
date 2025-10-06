import json
import os
from rich.progress import Progress

SAVINGS_FILE = "savings.json"
CURRENCY = "₱"  # "$"


def load_savings():
    if not os.path.exists(SAVINGS_FILE):
        return [{"actual": 0, "target": 1000, "project": "Default"}]
    with open(SAVINGS_FILE, "r") as f:
        data = json.load(f)
        if isinstance(data, list) and data:
            return data
        elif isinstance(data, dict):
            # If file contains a single dict, wrap it in a list
            return [data]
        else:
            return [{"actual": 0, "target": 1000, "project": "Default"}]


def show_progress():
    print("\nShowing savings progress:")
    data = load_savings()
    if isinstance(data, list):
        for entry in data:
            actual = entry.get("actual", 0)
            target = entry.get("target", 1000)
            project = entry.get("project", "Unnamed")
            code = entry.get("code", "N/A")
            percent = min(actual / target * 100, 100) if target else 0
            with Progress() as progress:
                print(
                    f"\t* {project} ({code}): {CURRENCY}{actual:.2f} / {CURRENCY}{target:.2f} ({percent:.2f}%)"
                )
                task = progress.add_task(f"\t[green]{project} Progress", total=target)
                progress.update(task, completed=actual)
        return


def main():
    print("Savings-calc app")
    while True:
        print("\nMenu:")
        print("1. Show progress\n2. Exit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            show_progress()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
