# Copyright (C) 2024 VI Software y contribuidores (contact@visoftware.tech)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(script_dir, 'old.txt'), 'r', encoding='utf-8') as f:
        old_header = f.read()
    logging.info("Successfully read 'old.txt'")
except Exception as e:
    logging.error("Error reading 'old.txt': " + str(e))

try:
    with open(os.path.join(script_dir, 'new.txt'), 'r', encoding='utf-8') as f:
        new_header = f.read()
    logging.info("Successfully read 'new.txt'")
except Exception as e:
    logging.error("Error reading 'new.txt': " + str(e))

action = input("Enter 'replace' to replace old header with new, 'add' to just add new header: ")

# Traverse every directory and subdirectory from the script's directory
for dirName, subdirList, fileList in os.walk(os.getcwd()):
    logging.info(f"Checking directory {dirName}")
    for fname in fileList:
        if fname.endswith('.js'):
            logging.info(f"Checking file {fname}")
            try:
                with open(os.path.join(dirName, fname), 'r+', encoding='utf-8') as f:
                    content = f.read()
                    if action == 'replace' and old_header in content:
                        content = content.replace(old_header, new_header)
                    elif action == 'add':
                        content = new_header + content
                    f.seek(0)
                    f.write(content)
                    f.truncate()
                logging.info(f"Successfully processed file {fname}")
            except Exception as e:
                logging.error(f"Error processing file {fname}: " + str(e))