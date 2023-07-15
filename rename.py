import os
import re

# Prompt the user to enter the directory path
directory = input("Enter the directory path where the files are located: ")

# Validate the directory path
while not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
    directory = input("Enter the directory path where the files are located: ")

# Prompt the user to enter the season number
season_number = input("Enter the season number (e.g., 02): ")

# Validate the season number
while not season_number.isdigit():
    print("Invalid season number. Please enter a valid number.")
    season_number = input("Enter the season number (e.g., 02): ")

# Get a list of all files in the directory
files = os.listdir(directory)

# Regular expression pattern to match the episode number
pattern = r'E(\d+)'

# Loop through each file in the directory
for file in files:
    # Check if the file name matches the pattern
    match = re.search(pattern, file, re.IGNORECASE)

    if match:
        # Extract the episode number
        episode_number = match.group(1)

        # Generate the new file name
        new_file_name = f'S{season_number.zfill(2)}E{episode_number}'

        # Get the file extension
        file_extension = os.path.splitext(file)[1]

        # Rename the file
        os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name + file_extension))

        print(f"Renamed '{file}' to '{new_file_name + file_extension}'")

print("Renaming complete!")
