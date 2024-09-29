import os

TRANSLITERATION_MAP = {
    'а': 'a', 'ā': 'ā', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'j': 'ǰ', '-': '',
    'ж': 'ž', 'з': 'z', 'и': 'i', 'ӣ': 'ī', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'Й': 'Y',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ӯ': 'ū', 'ӡ': 'ӡ',
    'ф': 'f', 'х': 'x', 'ц': 'c', 'ч': 'č', 'ӌ': 'ǰ', 'ш': 'š', 'ẋ': 'x̌', 'қ': 'q', 'δ': 'δ',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'w': 'w', 'ӧ': 'ö', 'ϑ': 'θ', 'ғ': 'ɣ'
}

def transliterate(text):
    transliterated_text = ''
    for char in text:
        transliterated_text += TRANSLITERATION_MAP.get(char, char)
    
    return transliterated_text

def transliterate_files_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        input_file_path = os.path.join(input_directory, filename)
        if os.path.isfile(input_file_path):
            with open(input_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            transliterated_content = transliterate(content)

            output_file_path = os.path.join(output_directory, filename)

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(transliterated_content)

            print(f"Transliterated file saved: {output_file_path}")

if __name__ == "__main__":
    input_dir = input("Enter the input directory path: ")
    output_dir = input("Enter the output directory path: ")
    
    transliterate_files_in_directory(input_dir, output_dir)
    print("Transliteration process completed.")

