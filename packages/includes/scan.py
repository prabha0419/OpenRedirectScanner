import requests
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
    redirect_chain = [url]
    final_target = None

    while True:
        response = requests.head(url, allow_redirects=True)
        if response.status_code in (301, 302):
            url = response.headers['Location']
            redirect_chain.append(url)
        else:
            final_target = url
            break

    vulnerability_found = is_open_redirect(final_target)

    result = f"Potential open redirect vulnerability found at {redirect_chain[0]}.\n"
    result += f"The URL redirects to: {final_target}\n"
    if vulnerability_found:
        result += "The target page contains the vulnerability.\n"
    else:
        result += "The target page does not contain the vulnerability.\n"

    if len(redirect_chain) > 1:
        result += "Redirect chain:\n"
        for i, redirect_url in enumerate(redirect_chain):
            result += f"{response.history[i].status_code} - {redirect_url}\n"

    with open(output_file, 'w') as file:
        file.write(result)
    print(f"Scan result written to '{output_file}'.")

