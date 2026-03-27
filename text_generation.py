from transformers import pipeline

text_generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_text(theme):
    prompt = f"Write a creative description about {theme}. "
    result = text_generator(
        prompt,
        max_length=150,
        num_return_sequences=1
    )
    return result[0]["generated_text"]
