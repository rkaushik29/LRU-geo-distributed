# Calculates whether line segments described by seg1 and seg2 params overlap on x-axis.
# Input: seg1 - Tuple[int, int], seg2 - Tuple[int, int]
# Return: Boolean
# Time : O(1) ; Space : O(1)
def line_overlap(seg1, seg2):
    # unpack line segments into start and end points
    s1, e1 = seg1
    s2, e2 = seg2

    # overlap condition
    if (s1 <= e2 and e1 >= s2) or (s2 <= e1 and e2 >= s1):
        return True
    else:
        return False
    
# Runs `line_overlap` after reading input file and writes results to output file.
# Input: input - File, output - File
def io_run(input_file, output_file):
    # using `with` so files are closed automatically
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        for line in input_file:
            if line[0] == "#" or line[0] == "\n":
                continue
            # gets all 4 integers as strings
            segments = line.strip().split()
            if len(segments) == 4:
                # converts digits to integers
                seg1 = int(segments[0]), int(segments[1])
                seg2 = int(segments[2]), int(segments[3])
                # write output
                if line_overlap(seg1, seg2):
                    output_file.write("Segments: (" + segments[0] + "," + segments[1] + ") and (" + segments[2] + "," + segments[3] + ") overlap.\n")
                else:
                    output_file.write("Segments: (" + segments[0] + "," + segments[1] + ") and (" + segments[2] + "," + segments[3] + ") do not overlap.\n")


if __name__=="__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    io_run(input_file=input_file, output_file=output_file)
