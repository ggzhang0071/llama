import gradio as gr
from translate_language import detect_language
from typing import Optional
import fire
from llama import Llama
from translate_language  import language_translator, translate_multiline_string
import  pickle, os 
import input_text

class chatbot():
    def __init__(self,
        ckpt_dir: str="llama-2-13b-chat/",
        tokenizer_path: str="tokenizer.model",
        max_seq_len: int = 512,
        max_batch_size: int = 8,
        #input_text: str = 'default'
    ):
        self.model = Llama.build(
            ckpt_dir=ckpt_dir,
            tokenizer_path=tokenizer_path,
            max_seq_len=max_seq_len,
            max_batch_size=max_batch_size,
        )

    def chat(self, input_text,       
            temperature: float = 0.6,
            max_gen_len: Optional[int] = 4096,
            top_p: float = 0.9,
            ):
        if self.model is None:
            raise ValueError("Model not loaded")
        if input_text == "你是谁" or input_text == "你是谁？":
            return("我是 datagpt，是您的数据分析小助手!!!")

        elif (input_text == "who are you") or  (input_text =="who are you?"):
            return("I am datagpt, your data analysis assistant!!!")

        """if  len(input_text.split()) < 2:  # 如果输入为空或只有空格
            return("请输入至少两个单词或字符。")
        """
        lang = detect_language(input_text)
        if lang == 'zh':
            input_text = input_text.replace(" ", "")
        elif lang == 'en':
            pass
        text=language_translator(input_text) 
        dialogs = [
                [{"role": "user", "content": text}]
                ]
        print(self.model)
        results = self.model.chat_completion(
                dialogs,  # type: ignore
                max_gen_len=max_gen_len,
                temperature=temperature,
                top_p=top_p,)
        print("here2")
        for _, result in zip(dialogs, results):
            return(result['generation']['content'])
            """if lang == 'zh':
                return(translate_multiline_string(result['generation']['content']))
            elif lang == 'en':
                return(result['generation']['content'])"""

        """file_path = 'dialogs_results.pkl'
        with open(file_path, 'wb') as file:  
            pickle.dump((input_text.query_text, dialogs, results), file)

    # 准备要写入.py文件的内容
    content = f"query_text = \"{input_text}\""
    # 将内容保存到input_text.py文件中
    with open('input_text.py', 'w', encoding='utf-8') as f:
        f.write(content)
    import subprocess
    bash_command = f'bash run_demo.sh'
    result = subprocess.run(bash_command, shell=True, stdout=subprocess.PIPE)
    output_text = result.stdout.decode('utf-8')
    print("here", type(output_text))
    return output_text.splitlines()[-1]"""


if __name__ == "__main__":
    model=chatbot()
    iface = gr.Interface(
        fn=model.chat,
        inputs=gr.Textbox(lines=10, placeholder="Enter your question here"),
        outputs=gr.Textbox(lines=10)
        #live=True
        )
    iface.launch()
