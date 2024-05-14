import argparse as ap
import logging
import json
from dotenv import dotenv_values


def main() -> None:
    """Search the folder/file name given as command argument in the database and
    allows a selection if many occurences exists.
    """
    configs = dotenv_values('./path.env')
    argparser = ap.ArgumentParser()
    
    # positional arguments
    argparser.add_argument(
        "name",
        help="name of the file/folder you want to find",
    )
    
    #optional arguments
    argparser.add_argument(
        "-g",
        "--goto",
        help="move to the proposed directory",
        action="store_true"
    )

    args =argparser.parse_args()
    
    # access the folder data
    with open(configs["FOLDER_DATA_PATH"], "r") as file:
        
        folderMap = json.loads(file.read())
        paths = folderMap.get(args.name)
    
    # no folder found
    if not paths:
        print("\nNo directory/file is named {}".format(args.name))
        return
    
    # only one found
    elif len(paths) == 1 :
        idx = 0
    
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


