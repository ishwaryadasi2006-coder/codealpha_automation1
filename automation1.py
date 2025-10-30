import os
import shutil
import re
import requests
from bs4 import BeautifulSoup

# --------------------------
# Task 1: Move all .jpg files
# --------------------------
def move_jpg_files(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(destination_folder, filename)
            shutil.move(src_path, dst_path)
            print(f"Moved: {filename}")

# --------------------------
# Task 2: Extract emails from a .txt file
# --------------------------
def extract_emails_from_file(input_file, output_file):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    with open(input_file, 'r') as file:
        text = file.read()
        emails = re.findall(email_pattern, text)
    
    with open(output_file, 'w') as out:
        for email in set(emails):  # Remove duplicates
            out.write(email + '\n')
    print(f"Extracted {len(set(emails))} email(s) to {output_file}")

# --------------------------
# Task 3: Scrape the title of a webpage
# --------------------------
def scrape_webpage_title(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip() if soup.title else "No Title Found"
    with open(output_file, 'w') as file:
        file.write(title)
    print(f"Saved webpage title to {output_file}")

# --------------------------
# Run All Tasks
# --------------------------
if __name__ == "__main__":
    # === Task 1 ===
    source_folder = "source_images"
    destination_folder = "moved_images"
    move_jpg_files(source_folder, destination_folder)

    # === Task 2 ===
    input_text_file = "emails_input.txt"
    output_email_file = "extracted_emails.txt"
    extract_emails_from_file(input_text_file, output_email_file)

    # === Task 3 ===
    fixed_url = "https://example.com"
    webpage_title_file = "webpage_title.txt"
    scrape_webpage_title(fixed_url, webpage_title_file)
