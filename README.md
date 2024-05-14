# quickRetrieve
The goal of this prject is to add a new fontionnality to our terminal. we want you to be able to find wether a file exist or not and its precise location in $O(1)$ using the characteristic of $\textrm{HashMap}$ and $\textrm{TreeMap}$. Additionnaly, you will be able to locate files that have a similar name if your file name does not exit.

## Initial setup

To be ble to use the functionnality of the repo you need to make some adjustement. 

### cloning the Repo

First let's start by cloning the repo :

```
git clone https://github.com/BelG13/quickRetrieve.git
```

### create the path.env file
Once the repo has been cloned, create a ``path.env`` file under ``quickRetrieve/``.
```
cd <your_path_to_repo>
touch path.env
```

### Create your environement variables

open the ``path.env``file, copy, paste and fill the following template into your ``path.env``file
```
TEMP_PATH=<your_temp_path>
ROOT=<your_root_path>
FOLDER_DATA_PATH=<your_folder_data_path>
FILE_DATA_PATH=<your_file_data_path>
```

``TEMP_PATH`` represents a path to a file that will temporarily store data and will be deleted right after use, give it the path that suits you well.

``ROOT`` is the starting point of the program. the code will scan everything from the root and create data that stores the paths.

``FOLDER_DATA_PATH` is the path to the ${\textsf{\color{red}json file}}$ that store the data structure of folders.

``FILE_DATA_PATH`` is the path to the ${\textsf{\color{red}json file}}$ that store the data structure of files.

### create an alias to run the program

you have two ways of running the program, either by 
```
cd <your_path_to_repo>
. ./quickSearch.sh <your_file_name>
```

or by simply adding the following code to you startup file : 
```
alias search=". <your_path_to_repo>/quickSearch.sh"
```

and then running with :
```
search <your_file_name>
```
## Run the command 

the setup is now finished, but still the folder/file data needs to be created. then run :
```
python <path_to_your_repo>/folderTree.py
```

and now you are able to search for the precise location of any file from your ``ROOT`` directory.
You do that by running the following command from everywhere : 
```
search <your_file_name>
```
If there is no such file located under your ``ROOT``, nothing will be found.

## Curent stage of the Project.

This is the first draft of the project and it represents the minimam viable code to make it work properly.

### Upcoming update :

Functionnalites | stage | priority |assignation |
--- | --- | --- | --- |
Refractor the code for saving the data, use a decorator. | ${\textsf{\color{skyblue}Under implementation}}$ | ${\textsf{\color{lightgreen}low}}$ |${\textsf{\color{violet}Belg13}}$ |
Propose similar folder name if the user folder name does not exit | ${\textsf{\color{darkgrey}not started}}$ | ${\textsf{\color{lightgrey}medium}}$ |${\textsf{\color{violet}Belg13}}$ |
search <file_name> is not currently supported, needs to be fixed | ${\textsf{\color{skyblue}Under implementation}}$ | ${\textsf{\color{red}High}}$ |${\textsf{\color{violet}Belg13}}$
Store files without their extension | ${\textsf{\color{skyblue}Under implementation}}$ | ${\textsf{\color{red}High}}$ |${\textsf{\color{violet}Belg13}}$

