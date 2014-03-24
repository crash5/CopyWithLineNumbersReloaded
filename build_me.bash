#!/bin/bash

cd copy_with_line_numbers
echo "{\"url\": \"https://github.com/freeella/copy_with_line_numbers.sublime-package\", \"version\": \"`date "+%Y.%m.%d.%H.%M.%S"`\", \"description\": \"A sublime package to copy text with files name and numbers\"}" >package-metadata.json
zip ../Copy\ With\ Line\ Numbers.sublime-package *

TARGETFOLDER=/tmp

# ----------------------------------------
# Set folder for Linux
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  if [ -e ~/.config/sublime-text-3 ]; then
    TARGETFOLDER=~/.config/sublime-text-3
  elif [ -e ~/.config/sublime-text-2 ]; then
    TARGETFOLDER=~/.config/sublime-text-2
  fi

# ----------------------------------------
# Set folder for Mac OS X
elif [[ "$OSTYPE" == "darwin"* ]]; then
  if [ -e "~/Library/Application\ Support/Sublime\ Text\ 3" ]; then
    TARGETFOLDER="~/Library/Application\ Support/Sublime\ Text\ 3"
  elif [ -e "~/Library/Application\ Support/Sublime\ Text\ 2" ]; then
    TARGETFOLDER="~/Library/Application\ Support/Sublime\ Text\ 2" 
  fi

# ----------------------------------------
# Output instructions for platforms with unknown install paths
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "Copy 'Copy With Line Numbers.sublime-package' to your Sublime Text 'Installed Packages' folder"
  exit;
elif [[ "$OSTYPE" == "win32" ]]; then
  echo "Copy 'Copy With Line Numbers.sublime-package' to your Sublime Text 'Installed Packages' folder"
  exit;
else
  echo "Copy 'Copy With Line Numbers.sublime-package' to your Sublime Text 'Installed Packages' folder"
  exit;
fi

# ----------------------------------------
# Remove and reinstall
rm -rf ${TARGETFOLDER}/Installed\ Packages/Copy\ With\ Line\ Numbers.sublime-package
rm -rf ${TARGETFOLDER}/Packages/Copy\ With\ Line\ Numbers

cp ../Copy\ With\ Line\ Numbers.sublime-package ${TARGETFOLDER}/Installed\ Packages/

