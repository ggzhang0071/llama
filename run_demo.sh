torchrun --nproc_per_node 2 example_chat_completion.py \
    --input_text "本月交易用户数，写个hive sql" \
    --ckpt_dir llama-2-13b-chat/ \
    --tokenizer_path tokenizer.model \
    --max_seq_len 4096 --max_batch_size 6 

    



