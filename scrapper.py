import re

# Define a regular expression pattern to match URLs
url_pattern = r'https?://[^\s]+'

# Open the text file for reading
with open('scraped_Dorks.txt', 'r') as file:
    # Read the content of the file
    file_content = file.read()

    # Use re.sub to replace URLs containing "accounts.google.com" and everything from the first ? or & (whichever comes first) with an empty string
    modified_content = re.sub(url_pattern, lambda x: '' if 'accounts.google.com' in x.group() else re.sub(r'[?&].*', '', x.group()), file_content)

# Write the modified content back to the file
with open('scrapped.txt', 'w') as file:
    file.write(modified_content)
