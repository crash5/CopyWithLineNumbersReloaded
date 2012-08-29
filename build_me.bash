#!/bin/bash

cd ~/src/copy_with_line_numbers.sublime/copy_with_line_numbers
rm ../Copy\ With\ Line\ Numbers.sublime-package
zip ../Copy\ With\ Line\ Numbers.sublime-package *
#rm -Rf ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Copy\ With\ Line\ Numbers
# copy on linux:
cp  ../Copy\ With\ Line\ Numbers.sublime-package ~/.config/sublime-text-2/Installed\ Packages/
# copy on Mac:
#cp ../Copy\ With\ Line\ Numbers.sublime-package ~/Library/Application\ Support/Sublime\ Text\ 2/Installed\ Packages/

