import requests
from bs4 import BeautifulSoup

# URL of the news site
url='https://www.bbc.com/news'

# Send request
response=requests.get(url)
if response.status_code!=200:
    print("Failed to fetch the page!")
    exit()

# Parse HTML
soup=BeautifulSoup(response.content, 'html.parser')

# Extract headlines from h3/h2 tags
headlines=soup.find_all(['h3', 'h2'])

# Filter unique headlines
unique_headlines=[]
for tag in headlines:
    text=tag.get_text(strip=True)
    if text and text not in unique_headlines:
        unique_headlines.append(text)

# Save to .txt file
with open('headlines.txt','w',encoding='utf-8') as f:
    for i, line in enumerate(unique_headlines,start=1):
        f.write(f"{i}. {line}\n")

print(f"✅ {len(unique_headlines)} headlines saved to 'headlines.txt'")
