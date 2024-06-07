Open Redirect Bug Finder Tool :

This tool scans URLs for potential open redirect vulnerabilities. It is structured into multiple files for better modularity and maintainability.

Project Structure :

openred/
│
├── main.py # Entry point of the application
├── packages/
│ └── includes/
│ ├── init.py # Init file for includes module
│ ├── file.py # File handling functions
│ ├── scan.py # Scanning functions
│ └── write.py # File writing functions
└── units/
├── init.py # Init file for units module
├── banner.py # Banner display function
├── chknet.py # Network checking function
└── urls.py # Data related to URLs (e.g., blog URL)

How to Set Up :

1. Clone the repository:
   
    git clone <repository_url>
    cd openred
 

2. Install the necessary packages:
   
    pip install -r requirements.txt


3. Make sure the directory structure is correct:
    - The `main.py` should be at the root level (`openred/`).
    - The `packages/` and `units/` directories should contain their respective files as shown above.

How to Run :

To use this tool, run the `main.py` file with the appropriate arguments:

python main.py -u <url> -o <output_file>

Example:
python main.py -u http://example.com -o output.txt

Arguments
-u or --url: Enter the URL to scan for open redirect vulnerabilities.
-i or --input: Enter the input file name to read URLs from (optional).
-o or --output: Enter the output file name to save the scan results.
-b or --blog: Opens the specified blog URL in the browser.

Explanation of Modules :
>>main.py: The main script that parses command-line arguments and triggers the relevant functions.

>>units/banner.py: Displays a welcome banner when the tool is run.

>>units/chknet.py: Checks if there is an active internet connection before proceeding with scans.

>>units/urls.py: Contains URL-related data, such as the blog URL.

>>packages/includes/file.py: Handles reading from and writing to files.

>>packages/includes/scan.py: Contains the logic to scan URLs for open redirect vulnerabilities.

>>packages/includes/write.py: Handles writing scan results to the specified output file.

Example Workflow :
>>Check for Network: Before starting, the tool checks if the internet connection is available.
>>Display Banner: A welcome banner is displayed to the user.
>>Scan URL: The tool scans the provided URL for open redirect vulnerabilities.
>>Read/Write Files: If an input file is provided, the tool reads URLs from it. Results are written to the specified output file.
>>Open Blog: If the --blog option is used, the tool opens the specified blog URL in the browser.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
Contact
For any issues or questions, please open an issue on GitHub.

***************************************************************
Thank you for using the Open Redirect Bug Finder Tool!

