import gpt_2_simple as gpt2
import os
import sys

model_name = "124M"
file_name = sys.argv[1]
print(file_name)

if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/



sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=40,
              restore_from='fresh',
              run_name=f'run {file_name}',
              print_every=5,
              sample_every=10,
              save_every=20
              )

gpt2.generate(sess)


