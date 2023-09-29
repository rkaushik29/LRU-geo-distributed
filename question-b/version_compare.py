# Compares version strings given as input
# Input: v1 (String), v2 (Sting) representing version numbers
# Output: String that shows comparison of v1 and v2
def compare_versions(v1, v2):   
    # Split strings based on decimal points.
    split1 = v1.split(".")  
    split2 = v2.split(".")
    versions1 = []
    versions2 = []

    for v in split1:
        if v:
            versions1.append(int(v))
        else:
            versions1.append(0)

    for v in split2:
        if v:
            versions2.append(int(v))
        else:
            versions2.append(0)

    for i in range(max(len(versions1),len(versions2))):
        ver1 = versions1[i] if i < len(versions1) else 0
        ver2 = versions2[i] if i < len(versions2) else 0
        if ver1 > ver2:
            return f"{v1} > {v2}"
        elif ver1 < ver2:
            return f"{v1} < {v2}"
    return f"{v1} = {v2}"

# Runs `compare_versions` after reading input file and writes results to output file.
# Input: input - File, output - File
def io_run(input_file, output_file):
    # using `with` so files are closed automatically
    test_cases = []
    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split(',')
            if len(parts) == 2:
                test_cases.append((parts[0], parts[1]))
    
    results = []
    for v1, v2 in test_cases:
        result = compare_versions(v1, v2)
        results.append(f"Input: {v1}, {v2}\nResult: {result}\n")
    
    with open(output_file, 'w') as outfile:
        outfile.writelines(results)

if __name__=="__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    io_run(input_file=input_file, output_file=output_file)
