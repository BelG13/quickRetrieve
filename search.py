import argparse as ap
import logging
import json
from dotenv import dotenv_values


def main() -> None:
    
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
    
    
    with open("folders.json", "r") as file:
        
        folderMap = json.loads(file.read())
        paths = folderMap.get(args.name)
    
    if not paths:
        print("\nNo directory/file is named {}".format(args.name))
        return
        
    elif len(paths) == 1 :
        idx = 0
        
    else:
        print()
        for i, path in enumerate(paths):
                print("{0} : {1}".format(i, path))
        
    
    if args.goto :
        
        idx = int(input("\nSelect the wanted path by typing the corresponding number : "))
        with open(configs["TEMP_PATH"], 'w') as file:
            file.write(paths[idx])
            

if __name__ == '__main__':
    main()


