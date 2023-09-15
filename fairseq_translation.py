from fairseq.models.transformer import TransformerModel

def load_fairseq_tm(path, device):
    # data_name_or_path和bpe_codes可以省略
    model = TransformerModel.from_pretrained(
        path,
        checkpoint_file='model.pt',
        data_name_or_path='.',
        bpe='subword_nmt',
        bpe_codes=path+"/bpecode"
    )
    model.cuda(device=device)
    return model

def translate(input_text):
    bt_model = load_fairseq_tm('./model/wmt16.en-de.joined-dict.transformer', 0)
    output = bt_model.translate(input_text)
    return  output

if __name__=="__main__":
    input_text='Hello world!'
    output=translate(input_text)
    print(output)
   