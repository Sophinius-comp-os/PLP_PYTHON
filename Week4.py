def process_file(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Example modification: Uppercase each line
                modified_line = line.upper()
                outfile.write(modified_line)

        print(f"File '{input_filename}' processed and written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_filename_and_process():
    """
    Prompts the user for a filename, handles errors, and calls process_file.
    """
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")
    process_file(input_filename, output_filename)

if __name__ == "__main__":
    get_filename_and_process()
