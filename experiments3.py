import random
import sys
file_name = sys.argv[1]

n_samp = 10

def sample_entries(input, output):
    with open(input, 'r') as file:
        entries = file.read().splitlines()

    filtered = [entry for entry in entries if len(entry) <= 60]
    if len(filtered) >= n_samp:
        sampled_entries = random.sample(filtered, n_samp)
        with open(output, 'w') as output_file:
            for entry in sampled_entries:
                output_file.write(entry + '\n')


#for colors: 10, 35, 59
#for romance_movies: 15, 37, 59

for i in [15, 37, 59]:
    #Early epoch, middle epoch, late epoch
    input = f'samples/run {file_name} FOR_ANALYSIS/PROCESSED-samples-{i}'
    output = f'samples/run {file_name} FOR_ANALYSIS/RSAMPLE_samples-{i}'
    sampled_list = sample_entries(input, output)

