from groq import Groq
client = Groq(api_key="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")
models = client.models.list()
for m in models.data:
    print(m.id)
