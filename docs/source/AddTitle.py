import os
for file_name in os.listdir("."):
    if file_name.endswith(".rst") and file_name != "index.rst":
        print(file_name)
        f = open(file_name, "w")
        f.write(file_name+"\n"+("="*len(file_name)))
        f.close()
