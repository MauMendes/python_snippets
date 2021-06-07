import os

def directory_size(start_path="."):
    dir_size = 0
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            dir_size += os.path.getsize(fp)
    return round(dir_size/1024/1024,2) # in MBytes
    
path = "."

for dir in os.listdir(path):
    curr_dir = path + "\\" + dir
    size = directory_size(curr_dir)
    if size >100:
        print( curr_dir + "-" + str(size) + " MBytes" )