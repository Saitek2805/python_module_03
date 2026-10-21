#!/usr/bin/env python3
import sys


def main() -> None:
    counter = 1
    scores: list[int] = []
    total = len(sys.argv)
    print("=== Player Score Analytics ===")
    while counter < total:
        try:
            arg_int = int(sys.argv[counter])
            scores = scores + [arg_int]
        except ValueError:
            print("Invalid parameter: '", sys.argv[counter], "'", sep="")
        counter += 1
    if len(scores) > 0:
        print("Scores processed:", scores)
        print("Total players:", len(scores))
        print("Total score:", sum(scores))
        print("Average score:", (sum(scores) / len(scores)))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", (max(scores) - min(scores)))
    else:
        print("No scores provided. Usage:",
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
