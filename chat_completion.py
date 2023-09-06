# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional

import fire

from llama import Llama
from translate_language  import  language_translator
import  pickle, os 
import input_text

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
    #input_text: str = 'default'
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    text=input_text.query_text
    #print(text, "this is a test")
    text=language_translator(text) 
    dialogs = [
        [{"role": "user", "content": text}]
        ]
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,)

    file_path = 'dialogs_results.pkl'
    with open(file_path, 'wb') as file:
        pickle.dump((input_text.query_text, dialogs, results), file)

if __name__ == "__main__":
    fire.Fire(main)
