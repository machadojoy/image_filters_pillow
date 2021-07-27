#!/usr/bin/env python3
import argparse
from image_processor import ImageProcessor

def main():
    parser = argparse.ArgumentParser(description='Apply filters to an image')
    parser.add_argument('-i', '--inputfile', type=str, help='Path to the input file')
    parser.add_argument('-o', '--outputfile', type=str, help='Path to the output file')
    parser.add_argument('-f', '--filter', nargs='*')
    args = parser.parse_args()
    input_file = "input.jpg"
    if args.inputfile:
        input_file = args.inputfile
    output_file = "output.jpg"
    if args.outputfile:
        output_file = args.outputfile
    filters = []
    if args.filter:
        filters = args.filter

    ip = ImageProcessor(input_file, output_file, filters)
    ip.apply_filters()

if __name__ == "__main__":
    main()