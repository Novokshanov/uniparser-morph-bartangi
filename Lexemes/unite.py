import os

def unite_files_in_directory(input_directory, output_filename):

    with open(output_filename, 'w', encoding='utf-8') as output_file:

        for filename in os.listdir(input_directory):
            input_file_path = os.path.join(input_directory, filename)

            if os.path.isfile(input_file_path) and filename.endswith('.txt'):
                with open(input_file_path, 'r', encoding='utf-8') as input_file:
                    content = input_file.read()

                    output_file.write(content + '\n')
                
                print(f"Added content from: {input_file_path}")

    print(f"All text files have been united into: {output_filename}")

if __name__ == "__main__":
    input_dir = input("Enter the input directory path: ")
    output_file_name = input("Enter the output file name (with .txt extension): ")
    
    unite_files_in_directory(input_dir, output_file_name)
