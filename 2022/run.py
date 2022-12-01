import argparse
import pathlib
import importlib

def main() -> int:
    parser = argparse.ArgumentParser("Advent of Code 2022 Runner")
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int)
    parser.add_argument("filename", type=str, nargs="?")
    args = parser.parse_args()

    print(args.day)

    module = f"day{args.day}.part{args.part}"
    if args.filename:
        inputPath = pathlib.Path(args.filename)
    else:
        inputPath = pathlib.Path(f"day{args.day}") / "input.txt"

    try:
        runner = importlib.import_module(module)
        runner.run(inputPath)
    except:
        print(module, "not found")
        return 1


main()
