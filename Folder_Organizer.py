#!/usr/bin/env python
# coding: utf-8


import os 
import shutil
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Organizes into subdirectories based on file type.")

# Add arguments
parser.add_argument("path_to_clean", type=str, help="The path you would like to organize.")


# path_to_clean="C:\\Users\\zafri\\Downloads"
# path_to_clean="C:\\Users\\zafri\\OneDrive\\Desktop"

# Parse the arguments
args = parser.parse_args()

path_to_clean = args.path_to_clean

os.chdir(path_to_clean)
os.listdir(path_to_clean)


# Document file types
document_file_types = [
    "doc", "docx", "pdf", "txt", "xls", "xlsx", 
    "ppt", "pptx", "odt", "ods", "rtf", "md", "csv"
]

# Music file types
music_file_types = [
    "mp3", "wav", "aac", "flac", "ogg", "m4a", 
    "wma", "alac"
]

# Video file types
video_file_types = [
    "mp4", "avi", "mkv", "mov", "wmv", "flv", 
    "webm", "m4v", "3gp"
]

def findfiletypes(path_to_clean):
    """
    Returns a list of file types found in input path 

    Parameters:
    path_to_clean (string): Path to folder to clean up
    
    Returns:
    typesoffiles (list): Lists of file types found. 
    """
    typesoffiles=[]
    for file in os.listdir(path_to_clean):
        filetype=file.split(".")[-1]
        typesoffiles.append(filetype)
    typesoffiles=set(typesoffiles)
    
    print (typesoffiles)
    return typesoffiles

findfiletypes(path_to_clean)


def organizebyfiletypes(path_to_clean):
    """
    Returns a list of file types found in input path 

    Parameters:
    path_to_clean (string): Path to folder to clean up
    
    Returns:
    typesoffiles (list): Lists of file types found. 
    """
    folder_pathtoclean = path_to_clean.split("\\")[-1].strip("./")
    folder_pathtoclean

    # os.chdir(path_to_clean)
    current_dir = os.getcwd()
    print (os.getcwd())


    
    typesoffiles=[]
    for file in os.listdir(current_dir):
        filetype=file.split(".")[-1]
        print (filetype)
        if filetype in document_file_types:
            print (file)
            new_documents_folder= folder_pathtoclean + "_Documents"
            os.makedirs(new_documents_folder, exist_ok=True)
            currentfilepath= current_dir + "/" + file
            newfilepath= current_dir + "/" + new_documents_folder + "/" + file

            shutil.move(currentfilepath, newfilepath) 
            print(currentfilepath + " --> " + newfilepath)
        if filetype in music_file_types:
            print (file)
            new_music_folder= folder_pathtoclean + "_Music"
            os.makedirs(new_music_folder, exist_ok=True)
            currentfilepath= current_dir + "/" + file
            newfilepath= current_dir + "/" + new_music_folder + "/" + file

            shutil.move(currentfilepath, newfilepath) 
            print(currentfilepath + " --> " + newfilepath)
        if filetype in video_file_types:
            #print (file)
            new_video_folder= folder_pathtoclean + "_Video"
            os.makedirs(new_video_folder, exist_ok=True)
            currentfilepath= current_dir + "/" + file
            newfilepath= current_dir + "/" + new_video_folder + "/" + file

            shutil.move(currentfilepath, newfilepath) 
            print(currentfilepath + " --> " + newfilepath)
        if filetype in ["zip"]:
            #print (file)
            new_zip_folder= folder_pathtoclean + "_Zip"
            os.makedirs(new_zip_folder, exist_ok=True)
            currentfilepath= current_dir + "/" + file
            newfilepath= current_dir + "/" + new_zip_folder + "/" + file

            shutil.move(currentfilepath, newfilepath) 
            print(currentfilepath + " --> " + newfilepath)
        
        
        
        



organizebyfiletypes(path_to_clean)



print ("done.") 




