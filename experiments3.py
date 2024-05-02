import random
import sys
import numpy as np
import csv
file_name = sys.argv[1]

n_samp = 15

def sample_entries(input):
    with open(input, 'r') as file:
        entries = file.read().splitlines()

    filtered = [entry for entry in entries if ((1 <= len(entry)) and (len(entry) <= 35)) and not (entry.endswith("<FLAG>") or entry.endswith("=="))]
    # if len(filtered) >= n_samp:
    #     sampled_entries = random.sample(filtered, n_samp)
    #     with open(output, 'w') as output_file:
    #         for entry in sampled_entries:
    #             output_file.write(entry + '\n')

    if len(filtered) >= n_samp:
        return random.sample(filtered, n_samp)
    return []


#for colors: 10, 35, 59
#for romance_movies: 15, 37, 59

g = np.geomspace(10, 59, 5).astype(int)

# for i in g:
#     #Early epoch, middle epoch, late epoch
#     input = f'samples/run {file_name} FOR_ANALYSIS/PROCESSED-samples-{i}'
#     output = f'samples/run {file_name} FOR_ANALYSIS/RSAMPLE_samples-{i}'
#     sampled_list = sample_entries(input, output)

columns = {}

for i in g:  # Early epoch, middle epoch, late epoch
    input_file = f'samples/run {file_name} FOR_ANALYSIS/PROCESSED-samples-{i}'
    sampled_entries = sample_entries(input_file)
    if sampled_entries:
        columns[f'Epoch_{i}'] = sampled_entries

max_len = max(len(col) for col in columns.values())
for key in columns:
    columns[key] += [''] * (max_len - len(columns[key]))

with open(f'samples/run {file_name} FOR_ANALYSIS/RSAMPLE.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns.keys()) 
    for row in zip(*columns.values()):
        writer.writerow(row)

