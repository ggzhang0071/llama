#
torchrun --nproc_per_node 2 --node_rank 0  chat_completion.py --ckpt_dir llama-2-13b-chat/ --tokenizer_path tokenizer.model --max_seq_len 4096 --max_batch_size 6 

python3 final_display.py



