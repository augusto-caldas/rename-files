import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # Remove content within [] and ()
        new_filename = re.sub(r'\[.*?\]|\(.*?\)', '', filename)  
        # Remove whitespace
        new_filename = re.sub(r'\s+\.', '.', new_filename)
        new_filename = new_filename.strip()  
        # Only rename if there are changes
        if new_filename != filename:  
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            # Print feedback to user
            print(f"Renamed '{filename}' to '{new_filename}'")

directory_path = './'
rename_files(directory_path)
