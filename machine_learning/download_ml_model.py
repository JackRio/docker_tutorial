from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Enter your local directory you want to store the model in
save_path = "model_weights/"

# Specify the model you want to download from HF
hf_model = 'facebook/nllb-200-distilled-600M'

# Instantiate the model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(hf_model, return_dict=True, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(hf_model)

# Save the model and the tokenizer in the local directory specified earlier
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
