from units import urls, banner, chnet
from packages.includes import file, scan

def main():
    print("Open Redirect Scanner running")
    import argparse
    import webbrowser

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Enter URL")
    parser.add_argument("-i", "--input", help="Enter input file name")
    parser.add_argument("-o", "--output", help="Enter the output file name")
    parser.add_argument("-b", "--blog", action='store_true', help="Open the blog")
    args = parser.parse_args()

    if args.url:
        banner.banner()
        scan.cvescan(args.url, args.output)

    if args.input:
        banner.banner()
        file.reader(args.input, args.output)
    
    if args.blog:
        banner.banner()
        webbrowser.open(urls.Data.blog)

if __name__ == "__main__":
    if chnet.net():
        main()
    else:
        print("\nCheck internet connection")
