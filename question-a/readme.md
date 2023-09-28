# Question A - Line Segment Overlap

Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

## Contents

- [Usage](#usage)
- [Input File](#input-file)
- [Output](#output)
- [Examples](#examples)

## Usage

Developed on Python3. This is recommended to run the project.

You can use this library to check if two line segments overlap by providing input in a text file. The results will be written to an output file.

To check for overlaps, run the following command:
```
python3 line_overlap.py input.txt output.txt
```
Replace input.txt with the name of your input file containing the line segments and output.txt with the desired output file name.

## Input File
The input file should contain *one test case per line*, with each test case consisting of *four integers separated by spaces*. These integers represent the endpoints of two line segments on the x-axis. For example:
```
1 5 4 7
3 8 10 12
```
In Line 1, `(x1,x2)` is `(1,5)` and `(x3,x4)` is `(4,7)`.

## Output
The program will write the results of the overlap checks to the specified output file. Each line in the output file will indicate whether the corresponding line segments overlap or not.

Example:
```
Segments: (1,5) and (4,7) overlap.
Segments: (3,8) and (10,12) do not overlap.
```
