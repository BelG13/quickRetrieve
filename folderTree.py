# Import module
import os
 
# Assign root
#TODO : in config
root = r"/Users/belboss/Desktop/Coding/bashTest/quickRetrieve"


folderMap = {}
def create_folder_map(root : str):
    
    for path, folders, files in os.walk(root):
        
        for folder_name in folders : 
            if folderMap.get(folder_name):
                folderMap[folder_name].append("{0}/{1}".format(path, folder_name))
            else:
                folderMap[folder_name] = ["{0}/{1}".format(path, folder_name)]
    
    return

if __name__ == "__main__":
    create_folder_map(root)
    print(folderMap)