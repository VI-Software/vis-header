# vis-header

VIS-header is a Python script that allows you to replace or add headers in all JavaScript (.js) files in your project.

## Prerequisites
- Python 3.x installed on your system.
- The script, along with 'old.txt' and 'new.txt' files, should be placed in the root directory of your project.
- How to Use
- Prepare two text files: 'old.txt' and 'new.txt'. 'old.txt' should contain the old header you want to replace, and 'new.txt' should contain the new header you want to add or use for replacement.

Run the script using a Python interpreter. You can do this by opening a terminal in the script's directory and running the command next command:
```python 
python ./vis-header/index.py
```

The script will prompt you to enter an action: 'replace' or 'add'. Enter 'replace' if you want to replace the old header with the new one. Enter 'add' if you want to add the new header to the beginning of each file.

The script will then traverse every directory and subdirectory from the script's parent directory, and for each '.js' file, it will perform the action you specified.

The script logs its progress, including the files it checks and any errors it encounters. You can view these logs in the terminal.

Please note that the script opens files in 'r+' mode, which means it will overwrite the files. Ensure you have a backup of your files or use a version control system to track changes.


```
Copyright (C) 2024 VI Software y contribuidores (contact@visoftware.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```