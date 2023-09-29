# Question A - Line Segment Overlap

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of. 

My execution examples are present in `input.txt` and `output.txt`. Please see below for input file formats in case you want to test further.

## Contents

- [Usage](#usage)
- [Input File](#input-file)
- [Output](#output)

## Usage

Developed on Python3. This is recommended to run the project.

You can use this library to compare two version strings by providing input in a text file. The results will be written to an output file.

To compare version strings, run the following command:
```
python3 version_compare.py input.txt output.txt
```
Replace input.txt with the name of your input file containing the line segments and output.txt with the desired output file name. *Place this in the same directory as the python program.*

## Input File
The input file should contain *one test case per line*, with each test case consisting of *two version strings separated by a ','*. These represent the versions to be compared. For example:
```
1.2,1.1
1.2.3.4,1.2.3  
```

## Output
The program will write the results of the version check to the specified output file. Each line in the output file will indicate the comparison of corresponding input versions.

Example:
```
Input: 1.2, 1.1
Result: 1.2 > 1.1
Input: 1.2.3.4, 1.2.3
Result: 1.2.3.4 > 1.2.3
```
