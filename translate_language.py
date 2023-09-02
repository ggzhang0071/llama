import langid
#from fairseq_translation1 import translate
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def translator(text):
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

    #text = "从时间上看，中国空间站的建造比国际空间站晚20多年。"
    input_ids = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(input_ids=input_ids, max_length=128, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(translated_text)
    return translated_text

def detect_language(text):
    lang, confidence = langid.classify(text)
    return lang, confidence

def language_translator (text):
    lang,confidence = detect_language(text,)
    if lang == 'zh':
        text= translator(text)
    elif lang == 'en':
        pass
    else:
        # 判断是否为中英混说
        if any(c.isalpha() for c in text):
            return translator(text)
        else:
            raise ValueError("We only support Chinese to English translation now!!!")
    return text

if __name__=="__main__":
    text="this is a monster"
    text=language_translator(text)  # 输出中文
    print(text)


