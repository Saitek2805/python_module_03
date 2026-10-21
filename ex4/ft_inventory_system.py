#!/usr/bin/env python3
import sys


class InventoryError(Exception):
    def __init__(self, *arg: str) -> None:
        default_message = "Inventory Error"
        if arg:
            super().__init__(*arg)
        else:
            super().__init__(default_message)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for argument in sys.argv[1:]:
        try:
            temp = argument.split(":")
            if len(temp) == 2:
                if temp[0] == "" or temp[1] == "":
                    raise InventoryError(
                        f"Error - Invalid parameter '{argument}'")
                elif temp[0] in inventory:
                    raise InventoryError(
                        f"Redundant item '{temp[0]}' - discarding")
                else:
                    quantity = int(temp[1])
                    inventory[temp[0]] = quantity
            else:
                raise InventoryError(f"Error - Invalid parameter '{argument}'")
        except InventoryError as e:
            print(e)
        except ValueError as e:
            print(f"Quantity error for '{temp[0]}':", e)

    print("Got inventory:", inventory)

    items = list(inventory.keys())
    print("Item list:", items)

    total = sum(inventory.values())
    print("Total quantity of the", len(items), "items", total)

    most_abundant = items[0]
    least_abundant = items[0]
    for item in inventory:
        quantity = inventory[item]
        if quantity > inventory[most_abundant]:
            most_abundant = item
        if quantity < inventory[least_abundant]:
            least_abundant = item
        percentage = round(quantity / total * 100, 1)
        print("Item ", item, " represents ", percentage, "%", sep="")

    highest = inventory[most_abundant]
    print("Item most abundant:", most_abundant, "with quantity", highest)

    lowest = inventory[least_abundant]
    print("Item least abundant:", least_abundant, "with quantity", lowest)

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)


if __name__ == "__main__":
    main()
