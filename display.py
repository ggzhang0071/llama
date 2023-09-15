import gradio as gr
from translate_language import detect_language
import subprocess

def run_bash_command(input_text):
    if input_text == "你是谁" or input_text == "你是谁？":
        return("我是 datagpt，您的数据分析小助手!!!")
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
  
    # 准备要写入.py文件的内容
    content = f'query_text = """{input_text}"""'
    # 将内容保存到input_text.py文件中
    with open('input_text.py', 'w', encoding='utf-8') as f:
        f.write(content)
    bash_command = f'bash run_demo.sh'
    result = subprocess.run(bash_command, shell=True, stdout=subprocess.PIPE)
    output_text = result.stdout.decode('utf-8')
    lines = output_text.split('\n')
    desired_output = '\n'.join(lines[4:])
    #return output_text.splitlines()[-1]
    return desired_output


iface = gr.Interface(
    fn=run_bash_command,
    inputs=gr.Textbox(lines=30, placeholder="Enter your question here"),
    outputs=gr.Textbox(lines=40),
    live=True
)

if __name__ == "__main__":
    iface.launch()

