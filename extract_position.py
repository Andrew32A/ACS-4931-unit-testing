def extract_position(line):
    if not line or 'debug' in line or 'error' in line:
        raise ValueError("Invalid line")
    
    if 'x:' not in line:
        raise ValueError("No position found in line")
    
    start_index = line.find('x:') + 2
    pos = line[start_index:].strip()
    return float(pos)

if __name__ == "__main__":
    try:
        result1 = extract_position('|error| numerical calculations could not converge.')
        print(result1)
    except ValueError as e:
        print(e)

    try:
        result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
        print(result2)
    except ValueError as e:
        print(e)
