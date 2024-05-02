import gpt_2_simple as gpt2
import os
import sys
from datetime import datetime

model_name = "124M"
file_name = sys.argv[1]
print(file_name)

now = datetime.now()

if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

run = f'run {file_name} FOR_ANALYSIS'

n_steps = 60

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=n_steps,
              restore_from='fresh',
              run_name=run,
              print_every=5,
              sample_every=1,
              save_every=20
              )

print('done!')

# gpt2.generate(sess)


#postprocessing! 

# for i in range(2, n_steps):
#     output_path = f'~/samples/run {file_name} NEW/samples-{i}'  
#     clean_output_path =  f'~/samples/run {file_name} NEW/CLEAN-samples-{i}'  
#     input_path = file_name
#     final_output_path = f'~/samples/run {file_name} NEW/PROCESSED-samples-{i}'  
#     seen = set()
#     inputs = set()
#     cleaned = []

#     #get rid of duplicates
#     with open(output_path, 'r', encoding='utf-8') as f:
#         for line in f:
#             cleaned_line = line.strip()
#             if cleaned_line not in seen:
#                 seen.add(cleaned_line)
#                 cleaned.append(cleaned_line)
#     with open(clean_output_path, 'w', encoding='utf-8') as f2:
#         for line in cleaned:
#             f2.write(line + '\n')

#     #check + count stuff that's in the input file

#     ctr = 0
#     total = 0
#     with open(input_path, 'r', encoding='utf-8') as f3:
#         for line in f3:
#             inputs.add(line.strip())  
#     with open(final_output_path, 'w', encoding='utf-8') as f4:
#         for line in cleaned:
#             total += 1
#             if line in inputs:
#                 ctr += 1
#                 f4.write(line + ' <FLAG>\n')  
#             else:
#                 f4.write(line + '\n')
#         f4.write("Percentage present in input file: " + str(ctr/total))


