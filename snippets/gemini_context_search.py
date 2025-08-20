import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = """ 
    Explan to me the equation for calculating the **effect size** in standar deviation and whether there are different approachese for situations where the distribution of data in the treatment group is skewed using those docs:
    - Website: https://en.wikipedia.org/wiki/Effect_size
    - Paper: https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf
    - Equation screenshot: https://www.statisticshowto.com/wp-content/uploads/2016/10/small-samples-formula.png
    
    Provide a summary approach based on all three sources and search for recent publications.
    """,
    config = {"tools": [
        {"url_context":{}},
        {"google_search":{}},
    ]},
)

print(f"Response: {response.text}")
