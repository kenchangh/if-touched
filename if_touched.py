import os
import subprocess


def watch_files(directory, action):
    file_contents = store_content(directory)
    
    while True:
        new_file_content = store_content(directory)
        
        shared_content = set(file_contents.items()) &
                         set(new_file_content.items())
        
        if len(shared_content) != len(new_file_content):
            subprocess.call(action, shell=True)


def store_content(directory):
    files = [os.path.join(path,fn) for fn in next(os.walk(directory))[2]]
    
    file_contents = {}
    
    for _file in files:
        with open(_file) as f:
            content = f.read()
        
        file_contents[_file] = content
    
    return file_contents
