from termcolor import colored
import pyfiglet

def banner():
    # Create a fancy banner using pyfiglet
    ascii_banner = pyfiglet.figlet_format("Open Redirect Finder")
    
    # Display the banner with colors
    print(colored(ascii_banner, 'cyan'))
    
    # Additional information
    info = """
    **************************************************
    *                                                *
    *        OPEN REDIRECT BUG FINDING TOOL          *
    *                                                *
    **************************************************
    *  Author: Prabha                                *
    *  Version: 1.0                                  *
    *  Description: This tool helps in finding open  *
    *  redirect vulnerabilities in web applications. *
    *                                                *
    **************************************************
    """
    print(colored(info, 'yellow'))

if __name__ == "__main__":
    banner()
    # Your main script logic here
