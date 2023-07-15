import os
import re
from natsort import natsorted, ns

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

# Sort the files using a natural sort with numeric sorting
files = natsorted(files, alg=ns.REAL)

# Regular expression pattern to match the episode number
pattern = r'(\d+)'

# Loop through each file in the directory
for i, file in enumerate(files, start=1):
    # Extract the numeric part of the file name
    match = re.search(pattern, file)
    if match:
        episode_number = match.group(1)
    else:
        episode_number = str(i)

    # Generate the new file name
    new_file_name = f'S{season_number.zfill(2)}E{episode_number.zfill(2)}'

    # Get the file extension
    file_extension = os.path.splitext(file)[1]

    # Check if the new file name already exists
    new_file_path = os.path.join(directory, new_file_name + file_extension)
    if os.path.exists(new_file_path):
        print(f"File '{new_file_name + file_extension}' already exists. Skipping...")
        continue

    # Rename the file
    os.rename(os.path.join(directory, file), new_file_path)

    print(f"Renamed '{file}' to '{new_file_name + file_extension}'")

print("Renaming complete!")
