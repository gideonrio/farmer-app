from groq import Groq
client = Groq(api_key="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")
try:
    models = client.models.list()
    for m in models.data:
        print(f"MODEL: {m.id}")
except Exception as e:
    print(f"ERROR: {e}")
