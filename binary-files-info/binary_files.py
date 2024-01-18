# _*_ coding: utf-8 _*_

"""This module provides hello_world_function."""

import os, datetime

def file_information(file):

    filename = os.path.basename(file).split('/')[-1]
    
    if not os.path.isfile(file):
        return f"   Error: {filename} doesn't exist!!\n"
    
    filetype = os.path.basename(file).split('.')[-1]
    filesize = os.stat(file).st_size
    filepath = os.path.dirname(file)
    datecreated = datetime.date.fromtimestamp(os.path.getctime(file))
    info = f"\nFile Information\n\
        File name:      {filename}\n\
        File type:      {filetype}\n\
        File size:      {filesize} Bytes\n\
        File path:      {filepath}\n\
        Date created:   {datecreated}\n"
    
    return info
