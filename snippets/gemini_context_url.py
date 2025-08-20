import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = """
    Show me information about the types of statistical control charts and situations each one is recommended using the docs
    https://factorialmap.github.io/pdca/grafico-de-controle.html
    """,
    config = {"tools":[{"url_context":{}}]},
)

print(f"Response: {response.text}")
