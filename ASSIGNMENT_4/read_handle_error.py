def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            line_num = 1
            for line in file:
                print(f"Line {line_num}: {line.strip()}")
                line_num += 1
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    read_and_print_file("sample.txt")