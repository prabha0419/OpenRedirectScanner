import re
from urllib.parse import urlparse, parse_qs

def is_open_redirect(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    for param, values in query_params.items():
        for value in values:
            if is_external_url(value):
                return True
    return False

def is_external_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)

def cvescan(url, output_file):
    if is_open_redirect(url):
        result = f"Potential open redirect vulnerability found at {url}."
    else:
        result = f"No vulnerability found at {url}."
    
    with open(output_file, 'w') as file:
        file.write(result)
    print(f"Scan result written to '{output_file}'.")

