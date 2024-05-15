import logging
import json
import os
from math import ceil
from dotenv import dotenv_values # type: ignore

def save_data(func):
    """Run the data creation function and do all the necessary
    processesing on the data (compute space, etc). All extra processing
    that one would want to make using the data should be done in the wrapper
    bellow. It is meant to be used as a decorator.

    Args:
        func (function): the function that creates the dict data, it returns
                       a tuple of two dicts, respectively for the folder 
                       and files paths

    Returns:
        function: wrapper function with all the processings
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -- %(message)s",
        datefmt="%d-%m-%Y"
        )
    logger = logging.getLogger(__name__)
    
    configs = dotenv_values('./path.env')
    
    def wrapper(*args, **kwargs):
        folder_data, file_data = func(*args, **kwargs)
        
        # save folder data
        with open(configs["FOLDER_DATA_PATH"], 'w') as file:
            json.dump(folder_data, file)
            
            # size in kb
            size_folders = ceil(os.path.getsize(configs["FOLDER_DATA_PATH"]) / 1000)
            logger.info("Size of folder data : {} kb".format(size_folders))
    
        # save files data
        with open(configs["FILE_DATA_PATH"], 'w') as file:
            json.dump(file_data, file)
            
            #size in kb
            size_files = ceil(os.path.getsize(configs["FILE_DATA_PATH"]) / 1000)
            logger.info("Size of folder data : {} kb".format(size_files))
            
        return 
    
    return wrapper