from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
model_id = "MBZUAI/LaMini-T5-738M"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

task_pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_tasks(obligation_text: str):
    prompt = f"Extract the key compliance task(s) and deadline(s) from the following:\n\n{obligation_text}"
    response = task_pipe(prompt, max_length=512, do_sample=False)[0]['generated_text']
    return response
