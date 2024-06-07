import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns the contents as a ConfigBox (dictionary).
    
    :param path_to_yaml: Path to the YAML file.
    :return: ConfigBox containing the YAML file contents.
    """
    with path_to_yaml.open('r') as file:
        try:
            data = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} is loaded successfully")
            return ConfigBox(data)
        except BoxValueError:
            raise ValueError("yaml file is empty")
        except Exception as e:
            raise e
        
@ensure_annotations
def create_dirs(path_to_dirs:list, verbose=True):
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created a directory at : {path}") 

@ensure_annotations
def get_size(path:Path)->str:
    size = round(os.path.getsize(path)/1024)
    return f"{size} KB"