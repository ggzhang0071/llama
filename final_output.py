import pickle
from translate_language  import  translate_multiline_string, detect_language

with open('dialogs_results.pkl', 'rb') as file:
    input_text,dialogs, results = pickle.load(file)
lang,_ = detect_language(input_text)
for dialog, result in zip(dialogs, results):
    if lang == 'zh':
        print(translate_multiline_string(result['generation']['content']))
    elif lang == 'en':
        print(result['generation']['content'])
