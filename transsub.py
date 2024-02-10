def load_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def replace_subtitle_lines(subtitle_text, japanese_text_file_path):
    japanese_text = load_text_from_file(japanese_text_file_path).strip().split('\n')
    subtitle_lines = subtitle_text.strip().split('\n')
    
    result_subtitle = ""
    for i in range(len(subtitle_lines)):
        result_subtitle += f"{subtitle_lines[i]}\n{japanese_text[i % len(japanese_text)]}\n\n"
    
    return result_subtitle

def main():
    subtitle_file_path = input("Enter the full path of the subtitle file: ")
    japanese_text_file_path = input("Enter the full path of the Japanese text file: ")

    with open(subtitle_file_path, "r", encoding="utf-8") as f:
        subtitle_text = f.read()

    result_subtitle = replace_subtitle_lines(subtitle_text, japanese_text_file_path)

    with open(subtitle_file_path, "w", encoding="utf-8") as f:
        f.write(result_subtitle)

    print("Subtitle lines replaced successfully!")

if __name__ == "__main__":
    main()
