import os
import sys
from visualization import read_vis, write_vis, produce_pdf

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python run.py [<path> [<path> ...]]")
        print("   <path>:\tPath of input audio files to extract drum music score")
    else:
        file_paths = sys.argv[1:]
        for file_path in file_paths:
            # try:
            filename_ = read_vis(file_path)
            write_vis(filename_, "dataset_"+filename_+".ADT.txt")
            produce_pdf(filename_)
            # except Exception as e:
            #     print(e)
