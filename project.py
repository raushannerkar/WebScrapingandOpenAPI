import requests
from bs4 import BeautifulSoup

username = "raushannerkar"
url = f"https://github.com/{username}?tab=repositories"

headers = {
    "User-Agent": "Mozilla/5.0"
}

open_ai_dict = {}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

repo_tags = soup.find_all("h3", class_="wb-break-all")

repos = []

for tag in repo_tags:
    a_tag = tag.find("a")
    repo_name = a_tag.text.strip()
    repo_url = "https://github.com" + a_tag["href"]
    repos.append((repo_name, repo_url))

for name, link in repos:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    about_us = soup.find("article", class_="markdown-body entry-content container-lg")
    if about_us:
        full_text = about_us.text.strip()

        lines = [line.strip() for line in full_text.splitlines() if line.strip()]
        cleaned_lines = []

        for line in lines:
            cleaned_lines.append(line)

        about_us_text = " ".join(cleaned_lines)

        if len(about_us_text) > 1000:
            about_us_text = about_us_text[:1000] + "..."
    else:
        about_us_text = "No description available"


    language_data = {}
    language_tags = soup.find_all("li", class_="d-inline")

    for li in language_tags:
        lang_span = li.find("span", class_="color-fg-default text-bold mr-1")
        percent_span = li.find_all("span")
        if lang_span and len(percent_span) > 1:
            language = lang_span.text.strip()
            percent = percent_span[1].text.strip()
            language_data[language] = percent

    open_ai_dict[name] = {
        "url": link,
        "description": about_us_text,
        "languages": language_data
    }

import json
print(json.dumps(open_ai_dict, indent=2))


def get_project_data():
    return open_ai_dict

