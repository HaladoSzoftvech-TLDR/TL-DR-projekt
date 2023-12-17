from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import os

model = T5ForConditionalGeneration(T5ForConditionalGeneration.from_pretrained("t5-small").config)
tokenizer = T5Tokenizer.from_pretrained("t5-small", model_max_length=1024)
model_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(model_dir, 'model.pt')
model.load_state_dict(torch.load(model_path))



def summarize(text):
    input_ids = tokenizer.encode("Summarize this:" + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(input_ids, max_length=200, min_length=40, length_penalty=2.0, num_beams=4,
                                 early_stopping=True)

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
