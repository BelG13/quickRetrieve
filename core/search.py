import argparse as ap
import json
from dotenv import dotenv_values


def main() -> None:
    """Search the folder/file name given as command argument in the database and
    allows a selection if many occurences exists.
    """
    configs = dotenv_values('./path.env')
    argparser = ap.ArgumentParser()
    
    # -- positional arguments -- #
    
    # file/folder name
    argparser.add_argument(
        "name",
        help="name of the file/folder you want to find",
    )
    
    # -- optional arguments -- #
    
    # move to the directory
    argparser.add_argument(
        "-g",
        "--goto",
        help="move to the proposed directory",
        action="store_true"
    )
    
    argparser.add_argument(
        "-f",
        "--file",
        help="you search only for files",
        action="store_true"
    )
    
    argparser.add_argument(
        "-d",
        "--dir",
        help="you search only for folder/directory",
        action="store_true"
    )

    args =argparser.parse_args()
    
    # -- data access -- #
    paths = []
    
    if not (args.file or args.dir):
        args.file = True
        args.dir  = True
    
    # access the folder data
    if args.dir:
        with open(configs["FOLDER_DATA_PATH"], "r") as file:
            
            folderMap  = json.loads(file.read())
            folderData = folderMap.get(args.name)
            
            if not folderData :
                pass
            elif type(folderData) is list:
                paths.extend(folderData)
            else:
                paths.append(folderData)
    
    # acces the file data
    if args.file:
        with open(configs["FILE_DATA_PATH"], "r") as file:
            
            fileMap = json.loads(file.read())
            fileData = fileMap.get(args.name)
            
            if not fileData:
                pass
            elif type(fileData) is list:
                paths.extend(fileData)
            else:
                paths.append(fileData)
    
    # no folder found
    if not paths:
        print("\nNo directory/file is named {}".format(args.name))
        return
    
    # only one found
    elif len(paths) == 1 :
        print()
        print("{0} : {1}".format(0, paths[0]))
    
    # many folders with the same name
    else:
        print()
        for i, path in enumerate(paths):
                print("{0} : {1}".format(i, path))
        
    # if that argument is given we'd like to move to the repo
    if args.goto :
        
        idx = int(input("\nSelect the wanted path by typing the corresponding number : "))
        with open(configs["TEMP_PATH"], 'w') as file:
            file.write(paths[idx])
            

if __name__ == '__main__':
    main()


