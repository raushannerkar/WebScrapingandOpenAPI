from anthropic import Anthropic
from secret import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)

def summarize_repo(name, description, language):
    prompt = f"""
    I have a GitHub project named "{name}".
    
    Description: {description}
    Language(s): {language}
    
    Please:
    1. Summarize what the project does
    2. Explain what kind of user might benefit from it
    3. Mention the core technologies used
    """

    response = client.messages.create(
        model="claude-3-haiku-20240307",  
        max_tokens=500,
        temperature=0.5,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text  
