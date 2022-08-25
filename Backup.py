import os
import shutil

source = input("Enter the source path")
destination = input("Enter the destination path")

source = source+"/"
destination = destination+"/"

listOfFiles = os.listdir(source)

for file in listOfFiles:
    shutil.copy((source + file), destination)