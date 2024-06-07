def reader(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        # Simulate writing to output file
        with open(output_file, 'w') as file:
            file.write(content)
        print(f"File '{input_file}' read successfully and output written to '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
