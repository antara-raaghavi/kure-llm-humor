import sys
n_steps = 30
file_name = sys.argv[1]

for i in range(3, n_steps, 2):
    output_path = f'samples/run {file_name} 26Apr/samples-{i}'  
    clean_output_path =  f'samples/run {file_name} 26Apr/CLEAN-samples-{i}'  
    input_path = file_name
    final_output_path = f'samples/run {file_name} 26Apr/PROCESSED-samples-{i}'  
    seen = set()
    inputs = set()
    cleaned = []

    #get rid of duplicates
    with open(output_path, 'r', encoding='utf-8') as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line not in seen:
                seen.add(cleaned_line)
                cleaned.append(cleaned_line)
    with open(clean_output_path, 'w', encoding='utf-8') as f2:
        for line in cleaned:
            f2.write(line + '\n')

    #check + count stuff that's in the input file

    ctr = 0
    total = 0
    with open(input_path, 'r', encoding='utf-8') as f3:
        for line in f3:
            inputs.add(line.strip())  
    with open(final_output_path, 'w', encoding='utf-8') as f4:
        for line in cleaned:
            total += 1
            if line in inputs:
                ctr += 1
                f4.write(line + ' <FLAG>\n')  
            else:
                f4.write(line + '\n')
        f4.write("Percentage present in input file: " + str(ctr/total))
