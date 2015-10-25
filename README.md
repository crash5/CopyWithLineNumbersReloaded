# Copy With Line Numbers Reloaded - Sublime Text Package

Use codes from:
 - https://github.com/freeella/copy_with_line_numbers.sublime-package
 - https://github.com/curiousstranger/copy_with_line_numbers.sublime-package


## Example

Single selection:
```
File: /home/dev/projects/CopyWithLineNumbersReloaded/README.md
1: Use codes from:
2:  - https://github.com/freeella/copy_with_line_numbers.sublime-package
```

Multi selection:
```
File: /home/dev/projects/CopyWithLineNumbersReloaded/Main.sublime-menu
04:         "children":
05:         [
06:             { "caption": "Copy With Line Numbers", "command": "copy_with_line_numbers" }
07:         ]
---
22:                             {
23:                                 "command": "open_file",
24:                                 "args": {"file": "${packages}/CopyWithLineNumbersReloaded/CopyWithLineNumbersReloaded.sublime-settings"},
25:                                 "caption": "Settings – Default"
26:                             },
```


## License

See LICENSE for license info
