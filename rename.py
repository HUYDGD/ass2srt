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
season_number = input("Enter the season number (e.g., 01): ")

# Validate the season number
while not season_number.isdigit():
    print("Invalid season number. Please enter a valid number.")
    season_number = input("Enter the season number (e.g., 01): ")

# Get a list of all files in the directory
files = os.listdir(directory)

# Sort the files using a natural sort with numeric sorting
files = natsorted(files, alg=ns.REAL)

# Regular expression pattern to match the episode number
pattern = r'(\d+)'

# Loop through each file in the directory
for i, file in enumerate(files, start=1):
    # Generate the new episode number
    episode_number = str(i).zfill(2)

    # Generate the new file name
    new_file_name = f'S{season_number.zfill(2)}E{episode_number}'

    # Get the file extension
    file_extension = os.path.splitext(file)[1]

    # Generate the new file path
    new_file_path = os.path.join(directory, new_file_name + file_extension)

    # Rename the file
    os.rename(os.path.join(directory, file), new_file_path)

    print(f"Renamed '{file}' to '{new_file_path}'")

print("Renaming complete!")
