import pickle
from translate_language  import  translate_multiline_string
import argparse

import gradio as  gr



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument('--port', default=5000, type=int, help='port number')
    parser.add_argument('--input_text', type=str)
    args = parser.parse_args()
    # 从文件加载变量
    with open('dialogs_results.pkl', 'rb') as file:
        dialogs, results = pickle.load(file)


    for dialog, result in zip(dialogs, results):
        for msg in dialog:
            print(f"{msg['role'].capitalize()}: {args.input_text}\n")
        print(
                #f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
                f"> {result['generation']['role'].capitalize()}: {translate_multiline_string(result['generation']['content'])}"
            )
        print("\n==================================\n")

 # gradio 用于网页展示
  demo = gr.Interface(fn=greet,
        inputs=gr.Textbox(lines=3, placeholder="Enter your question here"),
        outputs=gr.Textbox(lines=3))
  demo.launch()