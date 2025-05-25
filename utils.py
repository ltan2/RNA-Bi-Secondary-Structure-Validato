def read_fasta(filename):
    sequence = ""
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            sequence += line.strip().upper()
    return sequence

def read_bpseq(filename):
    # returns a list of tuples. Each tuple is an edge between two nodes
    basepairs = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(",")
            # convert 1-based to 0-based index
            i = int(parts[0]) - 1 
            paired = int(parts[2]) - 1
            if paired > i:
                basepairs.append((i, paired))
    return basepairs

def dotbracket_to_bpseq(sequence, structure, filename):
    stack = []
    n = len(sequence)
    pairs = [0] * n  # paired position for each nucleotide, 0 if unpaired

    for i, char in enumerate(structure):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                raise ValueError("Dot bracket notation err")
            j = stack.pop()
            pairs[i] = j + 1
            pairs[j] = i + 1

    if stack:
        raise ValueError("Dot bracket notation err")
    
    with open(filename, 'w') as f:
        for i in range(n):
            f.write(f"{i+1} {sequence[i]} {pairs[i]}\n")


def parse_input(sequence, basepairs):
    for base in sequence:
        if base not in "AUCG":
            print("Invalid RNA sequence")
    
    for i, j in basepairs:
        if i < 0 or i > len(sequence) or j < 0 or j >= len(sequence):
            print("Invalid basepair")
