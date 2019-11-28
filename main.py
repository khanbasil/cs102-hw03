import sys
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    # TODO: Fill in the actual logic here!
    with open(input_file_path, "r") as f:
        for line in f:
            integers = line.split(",")
            catalog = []
            for c in integers:
                catalog.append(float(c))
            print(f"{mean(catalog)}")




if __name__ == "__main__":
    main()
