import os
import pysubs2

# Prompt the user to enter the directory path
directory = input("Enter the directory path where the .ass files are located: ")

# Validate the directory path
while not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
    directory = input("Enter the directory path where the .ass files are located: ")

# Get a list of all .ass files in the directory
ass_files = [file for file in os.listdir(directory) if file.endswith('.ass')]

# Loop through each .ass file and convert it to .srt
for ass_file in ass_files:
    # Generate the corresponding .srt filename
    srt_file = os.path.splitext(ass_file)[0] + '.srt'

    # Open the .ass file using pysubs2
    subs = pysubs2.load(os.path.join(directory, ass_file), encoding='utf-8')

    # Save the subtitles as .srt
    subs.save(os.path.join(directory, srt_file), encoding='utf-8')

    print(f"Converted '{ass_file}' to '{srt_file}'")

print("Conversion complete!")