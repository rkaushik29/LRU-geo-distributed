# Calculates whether line segments described by seg1 and seg2 params overlap on x-axis.
# Input: seg1 - Tuple[int, int], seg2 - Tuple[int, int]
# Return: Boolean
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
def io_run(input, output):
    # using `with` so files are closed automatically
    with open(input, 'r') as input, open(output, 'w') as output:
        for line in input:
            # gets all 4 integers as strings
            segments = line.strip().split()
            if len(segments) == 4:
                # converts digits to integers
                seg1 = int(segments[0]), int(segments[1])
                seg2 = int(segments[2]), int(segments[3])
                # write output
                if line_overlap(seg1, seg2):
                    output.write("Segments: (" + segments[0] + "," + segments[1] + ") and (" + segments[2] + "," + segments[3] + ") overlap.\n")
                else:
                    output.write("Segments: (" + segments[0] + "," + segments[1] + ") and (" + segments[2] + "," + segments[3] + ") do not overlap.\n")


if __name__=="__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    io_run(input=input_file, output=output_file)
    