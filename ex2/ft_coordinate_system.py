#!/usr/bin/env python3
import math


class CoordinateError(Exception):
    def __init__(self, *arg: str) -> None:
        default_message = "Invalid syntax"
        if arg:
            super().__init__(*arg)
        else:
            super().__init__(default_message)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            number: list[float] = []
            coordinates = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
            separated = coordinates.split(",")
            if len(separated) != 3:
                raise CoordinateError
            for parameter in separated:
                try:
                    number = number + [float(parameter)]
                except ValueError as e:
                    raise CoordinateError(
                        f"Error on parameter '{parameter}': {e}")
            return (number[0], number[1], number[2])
        except CoordinateError as e:
            print(e)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get first set of coordinates")
    first_coordinate = get_player_pos()
    x, y, z = first_coordinate
    print("Got a first tuple: (", x, ", ", y, ", ", z, ")", sep="")
    print("It includes: X=", x, ", Y=", y, ", Z=", z, sep="")
    distance_center = round(
        math.sqrt(sum([x ** 2, y ** 2, z ** 2])), 4)

    print("Distance to center:", distance_center)

    print("\nGet second set of coordinates")
    second_coordinate = get_player_pos()

    x2, y2, z2 = second_coordinate
    distance = round(
        math.sqrt(sum([
            (x2 - x) ** 2,
            (y2 - y) ** 2,
            (z2 - z) ** 2
        ])), 4)
    print("Distance between the 2 sets of coordinates:", distance)


if __name__ == "__main__":
    main()
