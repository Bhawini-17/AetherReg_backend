import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["aetherreg"]
circulars_collection = db["circulars"]

# RBI circulars page
url = "https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx"
print("🔎 Fetching RBI circulars page...")
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# PDF links
pdf_links = []
for link in soup.find_all("a", href=True):
    href = link["href"]
    if href.lower().endswith(".pdf"):
        full_url = "https://www.rbi.org.in" + href if href.startswith("/") else href
        title = link.get_text(strip=True)
        if not title:
            title = "Untitled Circular"
        pdf_links.append({"title": title, "url": full_url})

unique_links = {c["url"]: c for c in pdf_links}.values()
print(f"Found {len(unique_links)} unique circulars.\n")


inserted_count = 0
for circular in unique_links:
    if not circulars_collection.find_one({"url": circular["url"]}):  
        circulars_collection.insert_one(circular)
        inserted_count += 1
    print(f"🔹 {circular['title']}\n   📎 {circular['url']}\n")

print(f"{inserted_count} new circular(s) saved to MongoDB.")
