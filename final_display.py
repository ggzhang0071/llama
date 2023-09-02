import pickle
import input_text
from translate_language  import  translate_multiline_string


# 从文件加载变量
with open('dialogs_results.pkl', 'rb') as file:
    dialogs, results = pickle.load(file)


for dialog, result in zip(dialogs, results):
    for msg in dialog:
        print(f"{msg['role'].capitalize()}: {input_text.sql_query}\n")
    print(
            #f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}"
            f"> {result['generation']['role'].capitalize()}: {translate_multiline_string(result['generation']['content'])}"

        )
    print("\n==================================\n")