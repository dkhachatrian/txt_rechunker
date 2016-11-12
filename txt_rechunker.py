# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:33:02 2016

@author: David
"""

MAX_LINE_LENGTH = 200
EOL_CHAR = '\n' #end of line char

import os
import re

def main():
    print("Give path to directory of files you want to rechunk.")
    print("Rechunked files will be placed in a new directory:")
#    in_dir = input("Give path to directory of files you want to rechunk:\n")
    in_dir = input()
    
    #do some splitting
    splitters = ['\\', '/']
    in_parts = [in_dir]
    
    for sep in splitters:
        if len(in_parts) == 1:
            in_parts = in_dir.split(sep)
    
    clean_in_dir = (os.sep).join(in_parts)
    # make out_dir
    in_parts[-1] = in_parts[-1] + '_rechunked'
    clean_out_dir= (os.sep).join(in_parts)
    if not os.path.exists(clean_out_dir):
        os.mkdir(clean_out_dir)
    
    for root, dirs, files in os.walk(clean_in_dir):
        try:
            for file in files:
                with open(os.path.join(root,file), newline = '') as inf:
                    with open(os.path.join(clean_out_dir,file), mode = 'w', newline = '') as outf:
                        for line in inf:
                            line = re.sub(r'[\n\r]', r'', line)
                            i = 0
                            while (len(line) - i)\
                            > (MAX_LINE_LENGTH - 1): #choppy cutting
                                outf.write(line[i:MAX_LINE_LENGTH-1] + EOL_CHAR)
                                i+=(MAX_LINE_LENGTH-1)
                            outf.write(line[i:] + EOL_CHAR)
        except UnicodeDecodeError:
            #probably trying to "convert" an executable or something
            #ignore
            pass

main()