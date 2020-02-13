# OS Module in Python

**os.getcwd()** returns the current working directory as a string. 

**os.listdir()** returns the contents of the current working directory as a list of strings. 

**os.walk()** creates a generator that can return information about the current directory and subdirectories. 

It returns the following items for each directory it traverses:

- current directory path as a string
- subdirectory names in the current directory as lists of strings
- filenames in current directory as a list of strings

It’s often useful to use os.walk() with a for loop to iterate over the contents of a directory and its subdirectories.

For example, the following code will print all files in the directories and subdirectories of the current working directory.

```python
import os
cwd = os.getcwd()
for dir_path, dir_names, file_names in os.walk(cwd):
    for f in file_names:
        print(f)
```

**os.chdir("/absolute/or/relative/path")** changes the current working directory to either the absolute or relative path provided.

**os.path.join()** create a path that will work on most any operating system by joining multiple strings into one file path

Basically, if we are on a Unix or macOS system, os.path.join() sticks a forward slash (“/”) between each string you provide to create a path. If the operating system needs a “\” instead (like in Windows), then join will use a back slash.

**os.remove("my_file_path")** to remove a file

# SHUTIL Module

**shutil.copy2("source_file", "destination")** copy2 method is identical to the copy method, but in addition to copying the file contents it also attempts to preserve all the source file's metadata. If the platform doesn't allow for full metadata saving, then copy2 doesn't return failure and it will just preserve any metadata it can.

**shutil.move("source_file", "destination")** change a file’s location. It uses copy2 as the default under the hood.

**shutil.rmtree("my_file_path")** removes a directory and all files and directories in it.
