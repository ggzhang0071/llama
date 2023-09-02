# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional

import fire

from llama import Llama
from translate_language  import  language_translator, translate_multiline_string
import input_text
import os


def main(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    text=language_translator(input_text.sql_query) 

    dialogs = [
        [{"role": "user", "content": text}]
        ]
    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    bb=results[0]["generation"]['content']
    # 将变量 text 保存到 output.py 文件中
    print(bb)
    os.exit()


    output=translate_multiline_string(bb.to('cpu'))

    for dialog, result in zip(dialogs, results):
        for msg in dialog:
            print(f"{msg['role'].capitalize()}: {input_text.sql_query}\n")
        print(
            f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
            #f"> {result['generation']['role'].capitalize()}: {translate_multiline_string(result['generation']['content'])}"

        )
        print("\n==================================\n")


if __name__ == "__main__":
    fire.Fire(main)
