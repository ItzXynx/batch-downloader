import sys
import urllib.request
import os

# download multiple urls at once
# reads from a txt file, one url per line

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python main.py urls.txt [output_dir]")
        sys.exit()
    
    urls_file = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    os.makedirs(output, exist_ok=True)
    
    with open(urls_file) as f:
        urls = [l.strip() for l in f if l.strip()]
    
    print(f"downloading {len(urls)} files...")
    for url in urls:
        filename = url.split("/")[-1] or "file"
        path = os.path.join(output, filename)
        try:
            urllib.request.urlretrieve(url, path)
            print(f"ok: {filename}")
        except Exception as e:
            print(f"fail: {url} - {e}")
    
    print("done")
