import os

def rename_files(directory, season, extension):
    counter = 892
    for filename in os.listdir(directory):
        if counter < 10:
            new_filename = f"S{season}E00{counter}.{extension}"
        elif counter < 100:    
            new_filename = f"S{season}E0{counter}.{extension}"
        else:
            new_filename = f"S{season}E{counter}.{extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"{filename} -> {new_filename}")
        counter += 1

directory_path = input("Enter directory path >> ")
season = input("Enter season >> ")
extension = input("Enter extension >> ")
rename_files(directory_path + "/Season " + season, season, extension)
