#!/usr/bin/env python3
import sys


def main() -> None:
    counter = 1
    total = len(sys.argv)
    print("=== Command Quest ===")
    print("Program name:", sys.argv[counter - 1])
    if total > 1:
        print("Arguments received:", total - 1)
        while counter < total:
            print("Argument ", counter, ": ", sys.argv[counter], sep="")
            counter += 1
    else:
        print("No arguments provided!")
    print("Total arguments:", total, "\n")


if __name__ == "__main__":
    main()
