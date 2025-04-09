# 🗃️ zipexesanitiser
a file integrity tool that safely removes zip archives and executable files from your downloads folder

![python](https://img.shields.io/badge/python-3.7+-blue.svg)
![license](https://img.shields.io/badge/license-mit-green.svg)

## [✨] : what it does
zipexesanitiser automatically cleans your downloads folder by removing zip archives that have already been extracted and potentially dangerous executable files. it safely moves these files to the recycle bin rather than permanently deleting them, giving you a chance to recover anything important!

perfect for : maintaining a clean downloads directory and reducing security risks from accumulated executable files 🧹

## [🎯]: key features
- **zip cleanup**: intelligently removes zip files once their contents have been extracted(yes,it double checks!)
- **exe removal**: safely clears executable files from your downloads folder
- **recycle bin safety**: uses send2trash to move files to recycle bin instead of permanent deletion
- **user notifications**: shows a friendly message box with deletion summary
- **zero configuration**: works out-of-the-box with your downloads folder
- **lightweight**: small footprint with minimal dependencies
- **windows integration**: native windows message box notifications

## [🚀]: how to use
```bash
# clone the repo
git clone https://github.com/ritikaslaptop/zipexesanitiser.git
cd zipexesanitiser

# install dependencies
pip install send2trash

# run the individual cleaners
python zip_cleaner/src/zip_cleaner.py  # to clean zip files
python exe_cleaner/src/exe_cleaner.py  # to clean executable files

# alternatively, use the pre-built executables in the builds folders(to be added soon)
```

you can also create shortcuts to run the executables with a single click, or set them up to run automatically on system startup.

## [🧠]: how it works
1. **zip file processing**:
   - locates all zip files in your downloads folder
   - checks if a folder with the same name exists (indicating extraction)
   - if extracted folder exists, moves the zip file to recycle bin

2. **exe file removal**:
   - finds all executable files in downloads folder
   - safely moves them to recycle bin
   - reports total number of removed files


## [🔧]: libraries used
| library | what it does in our app |
|---------|-------------------------|
| **os** | provides functions for working with file paths and directories |
| **glob** | finds all files matching a pattern (*.zip, *.exe) |
| **send2trash** | safely moves files to recycle bin instead of permanent deletion |
| **pathlib** | modern path manipulation library for cross-platform compatibility |
| **ctypes** | allows calling windows apis for displaying message boxes |
| **subprocess** | used in linux version to display notifications |

## [🔮] : future enhancements
- **custom folder support**: scan user-specified directories beyond downloads
- **file extension configuration**: add or remove file types to clean
- **gui interface**: simple window for configuration and manual scanning
- **silent mode**: option to run without notifications for automated tasks
- **scheduling**: built-in scheduler for periodic cleaning
- **file age filtering**: remove files older than a specified date
- **detailed logs**: save operation history to a log file
- **admin mode**: option to clean system-wide temporary folders
- **file signature scanning**: identify executables regardless of extension
- **macos & linux version**: support for macos&linux platforms with native notifications

## [🤝] : contributing
contributions welcome! feel free to submit issues or pull requests.

## [⚠️] : disclaimer
please use this tool carefully. while it moves files to the recycle bin rather than permanently deleting them, you should always ensure you have backups of important files.

## [📄] : license
this project is licensed under the mit license - see the license file for details.