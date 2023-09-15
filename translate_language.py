import langid
#from fairseq_translation1 import translate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelWithLMHead,pipeline
import torch
import re

def detect_program_language(text):
    # SQL keywords
    sql_keywords = ["SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "DROP", "CREATE", "ALTER", "JOIN"]
    # Shell commands
    shell_commands = ["echo", "ls", "cd", "mkdir", "rm", "chmod", "chown", "sudo", "apt-get", "yum"]
    # Python keywords
    python_keywords = ["def", "class", "import", "print", "for", "while", "if", "else", "elif", "return", "lambda"]
    # Check for SQL
    if any(keyword in text.upper() for keyword in sql_keywords):
        return "SQL"
    # Check for Shell
    if any(command in text for command in shell_commands):
        return "Shell"
    # Check for Python
    if any(keyword in text for keyword in python_keywords):
        return "Python"
    # If none of the above, return plain text
    return "plain text"


def translate_en_to_zh(text):
    device = torch.device("cpu")
    mode_name = 'liam168/trans-opus-mt-en-zh'
    model = AutoModelForSeq2SeqLM.from_pretrained(mode_name).to(device)
    tokenizer = AutoTokenizer.from_pretrained(mode_name)
    translation = pipeline("translation_zh_to_en", model=model, tokenizer=tokenizer)
    outputs=translation(text, max_length=400)
    return outputs[0]["translation_text"]

def translator_zh_to_en(text):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids=input_ids, max_length=128, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

def detect_language(text):
    lang, confidence = langid.classify(text)
    return lang, confidence

def language_translator (text):
    lang = detect_language(text)
    if lang == 'zh':
        text= translator_zh_to_en(text)
    elif lang == 'en':
        pass
    else:
        # 判断是否为中英混说
        if any(c.isalpha() for c in text):
            return translator_zh_to_en(text)
        else:
            raise ValueError("We only support Chinese to English translation now!!!")
    return text
    


def translate_multiline_string(s):
    lines = s.split('\n')
    translated_lines = []
    counter=0
    
    for line in lines:
        if line.strip()=="":
            translated_lines.append(line)
        else:
            if "```" in line:
                counter+=1
            if counter%2==0:
                if line.startswith("*"):
                    print(line)
                    segments = re.split(r"(\* `.*?`)", line)
                    for i, segment in enumerate(segments):
                        if segment=="":
                            del segments[i]
                            continue
                        if not segment.startswith("* `") and not segment.endswith("`"):
                            segments[i] = translate_en_to_zh(segment)
                    translated_lines.append(''.join(segments))
                else:
                    translated_lines.append(translate_en_to_zh(line))
            else:
                translated_lines.append(line)

            """language = detect_program_language(line)
            if language in ["SQL", "Python","Shell"]:
                translated_lines.append(line)  
            else:
                if line=="sql":
                    translated_lines.append(line)  
                else:
                    translated_lines.append(translate_en_to_zh(line))
                #print(line)
                words_in_text = line.split()
                if len(words_in_text) > 1:
                    translated_lines.append(translate_en_to_zh(line))
                else:
                    translated_lines.append(line)  
                """
    return '\n'.join(translated_lines)


if __name__=="__main__":
    """text="this is a monster"
    text=language_translator(text)  # 输出中文
    print(text)
    
    import  output
    text=output.sql_query
    print(translate_multiline_string(text))
    """

    input_text="who are you"
    text=language_translator(input_text) 
    





   