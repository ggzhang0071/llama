#! /bin/bash
torchrun --nproc_per_node 2 --node_rank 0   display.py \
--ckpt_dir llama-2-13b-chat/ --tokenizer_path tokenizer.model

#python3 final_output.py  --input_text $text



