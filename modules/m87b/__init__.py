import os

from transformers import AutoModelForCausalLM, AutoTokenizer


def setup():
    model_id = "mistralai/Mixtral-8x7B-v0.1"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    print(os.environ['HF_HOME'])
    print(os.environ['TRANSFORMERS_CACHE'])
    print(os.environ['HF_DATASETS_CACHE'])

    print(".")
    # TODO This is where the error occurs
    model = AutoModelForCausalLM.from_pretrained(model_id)
    print(".")
    text = "Hello my name is"
    print(".")
    inputs = tokenizer(text, return_tensors="pt")
    print(".")
    outputs = model.generate(**inputs, max_new_tokens=20)
    print(".")
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    print(".")
