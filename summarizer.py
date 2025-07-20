from openai import OpenAI
from secret import openai_api_key
from project import get_project_data

client = OpenAI(api_key=openai_api_key)

projects = get_project_data()

for name, info in projects.items():
    description = info["description"]
    languages = ", ".join(f"{lang} ({perc})" for lang, perc in info["languages"].items())
    
    prompt = f"""
You are an AI assistant. Summarize and explain this GitHub project.

Project Name: {name}
Languages Used: {languages}
Description: {description}

Provide a short summary of what this project does and its purpose.
"""

    print(f"\n--- Summary for {name} ---")
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You summarize GitHub projects."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    print(response.choices[0].message.content)
