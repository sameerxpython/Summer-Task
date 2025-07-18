import requests

url = "https://example.com/path/to/file.zip"
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open("file.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print("Download complete!")
else:
    print("Failed, status:", response.status_code)
