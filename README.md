
# README

- This folder contains a bunch of simple example files to help you get started adding behavior (plugins, syntaxes, etc) to Sublime Text.

- All these files can be placed in your Sublime Packages/User folder which can be reached by doing "Preferences" -> "Browse Packages..." and then opening the "User" folder.

- Files added to this folder are automatically picked up by Sublime Text and changes are auto-reloaded as well so you almost never need to restart sublime, or refresh anything. You can just make changes, save, and then immediately test your new functionality with running instance of Sublime.

- To catch syntax errors in python or JSON files or to see debug output from print statements in python code, try opening the console window with Ctrl+Tilde or by going to "View" -> "Show Console"

- You can also make new folders, named whatever you want, next to the "User" folder and add your extensions there. This helps keep your own extensions seperate from some of the automatically generated files in the User folder.

---

- A note about the package control plugin:
	- By default sublime does not come with a way to download plugins made by other people.
	- However, you can easily install the "Package Control System" from the command palette by pressing Ctrl+Shift+P and typing in and looking for "Install Package Control"
	- After a couple seconds for that to install you should then be able to open the command palette again and look for "Package Control: Install Package"
	- After selecting this option, wait for 2-3 seconds for another prompt to show up
	- This prompt is where you can search through and install packages made by the community and uploaded to the [Package Control Website](https://packagecontrol.io)
	- Here are some packages that I highly recommend
		- **Alignment** - Set up a keybinding for "alignment" (I have it bound to alt+a). Then when you have multiple cursors, hitting the keybinding will add spaces to each cursor such that they all line up. This is extremely useful when formatting mutliple lines of similar code (like array definitions, or repeated calls to the same function/macro)
		- **HighlightWords** - Automatically changes the color of NOTE: and TODO: in all your files so they are really easy to see. It's configurable to other patterns, but I haven't ever actually configured it to do anything more
		- **Insert Nums** - Add a binding for the "prompt_insert_nums" (I have it bound to Ctrl+Alt+Shift+N) or the "insert_nums" command with a "format" argument of "0:1" (I have it bound to Ctrl+Alt+N). Then when you have multiple cursors, you can generate numbers at each cursor location that increment by some fixed amount. For example, the format 0:1 will make the first cursor have the text "0" and the next cursor "1" and next cursor "2" etc. Where the format "10:3" will generate "10" "13" "16" etc.

---

- Besides the files included in this folder, you can also take a look at any of the plugins I have created for myself at [SublimeData Github Repo](https://github.com/PiggybankStudios/SublimeData)

- Visual Studio Code is another popular text editor option that can be similarly extended. For a while I tried converting my sublime plugins over to VS Code. That repository can be found at [VS Code Taylor Ext Repo](https://bitbucket.org/stampede247/vscodetaylorext) and [VS Code Data Repo](https://bitbucket.org/stampede247/vscodedata)

- Also see [Sublime Text Docs](https://www.sublimetext.com/docs/) under **Customization** and **Package Development** for offical documentation on all these different files

---

The rest of this README is dedicated to explaining what each of the example files in the respository do:

## **Default (Windows).sublime-keymap** (JSON)
- This file will automatically be generated for you if you go to "Preferences" -> "Key Bindings".
- The left pane will contain the default bindings (uneditable) while the right pane will contain your own custom bindings that will overwrite or add to the default bindings
- The file uses the JSON syntax (like most .sublime-something files)
- This is where you can change the key bindings for sublime text. You can add entirely new bindings or you can replace existing ones by defining them in in this file.
- The actual default bindings are stored elsewhere and are not editable directly, instead your User version is applied on top of the defaults, so anything you don't overwrite will use the default bindings
- Each key-binding object has two have properties, "keys" and "command" and look like:
		{ "keys": ["ctrl+m"], "command": "my_demonstration" },
- When you add a command class in python like "MyDemonstrationCommand" it translates to a lowercase with underscores name like "my_demonstration" (also note that "Command" suffix is removed)

## **ignored_file.txt** and **ignored_folder_that_is_suffix_matched**
- Demonstrations of ignoring files and folders for SublimeToolsBrownBag.sublime-project

## **ModifiedMonokai.tmTheme** (XML)
- A customized version of the default theme "Monokai" that has a few extra colors for custom scopes that I wanted for TODO.sublime-syntax. It also has a slightly darker background color and might be somewhat out of date copared to the latest version of Monokai since it's been years since I copied and made this customized version

## **MyDemonstrationCommands.sublime-commands** (JSON)
- This file declares commands that should be available from the "Command Palette" which can be brought up with Ctrl+Shift+P

## **MyDemonstrationPlugin.py** (Python)
- This is an actual "plugin" that adds a new TextCommand and a new EventListener that provides some autocomplete entries
- The command is named "MyDemonstrationCommand" which can be run using the following name in other places (like sublime-keymap, or sublime-commands): "my_demonstration"
- This command prints out a string to the debug console and also adds parenthesis around each piece of text that is selected in the current file
- The event listener will run every time that auto-complete items are requested by Sublime and can provide any number of potential auto-complete entries
- Python files are where the real extension functionality lives. You can add almost anything you want using python classes. Sublime has pretty good documentation on the API too which should be the main thing you reference when writing code for sublime plugins - [API Reference](https://www.sublimetext.com/docs/api_reference.html)
- Also check out [How to Create Your Own Sublime Text Plugin](https://www.tutorialspoint.com/sublime_text/sublime_text_developing_plugin.htm)

## **PIN_INPUT.sublime-snippet** (XML)
- This file adds a new "snippet" which is sorta like a high powered, always available, auto-complete entry
- If you add this to sublime and start typing "PIN_INPUT" you will see it show up in the auto-complete dialog
- When you select it, it will generate text and also take you the the process of replacing various pieces of the snippet one group at a time (with tab taking you to the next replacement group)
- See [Sublime Text Snippets](https://docs.sublimetext.io/guide/extensibility/snippets.html)

## **run_my_batch_file.sublime-build** (JSON)
- Adds a new "Build System" that can be run with Ctrl+B (after you've selected this tool from the "Tools" -> "Build System" menu)
- This is a simple hook to allow you to run things on the command-line using some information from the sublime-project or the state of the window (like the path of the current file that is open)
- The standard output of the build process is shown in a temporary "build" window that pops up at the bottom.
- A regular expression can be used to find errors in the build output and parse them so that sublime can jump you to the referenced file path and line number
- A custom syntax can also be used to color the build output nicely
- See [Build Systems Documentation](https://www.sublimetext.com/docs/build_systems.html)

## **SublimeToolsBrownBag.sublime-project** (JSON)
- Defines a "project" in sublime. Try double clicking this to open the project with Sublime.
- Each project contains any number of folders. Relative paths or absolute paths are accepted
- Specific folder or file patterns can be excluded from the project. Really useful when you don't want your project-wide search results to contain specific sub-directories or specific file types
- See [Sublime Text Projects Documentation](https://www.sublimetext.com/docs/projects.html)

## **SublimeToolsBrownBag.sublime-workspace** (JSON)
- This is all the "temporary" state information about the project, this should usually be ignored in your source control because it will change every time you open the project.
- It can safely be deleted whenever you want to reset the state of the project (like which files are opened, what the layout of the window is, which files were recently viewed, etc.)

## **TODO.sublime-settings** (JSON)
- This file pairs with TODO.sublime-syntax to declare which file types should use the syntax by default

## **TODO.sublime-syntax** (YAML)
- This is an entirely new language syntax definition. Normally this would be a syntax for a programming language, but I have used this system to color my notes files (like this one) with nice colors based on some simple syntax (like lines that start with - are turned blue, and [X] are turned grey)
- This file is in yaml format but I believe you can also accomplish the same sort of thing using JSON syntax. You just have to do a lot more escaping because the regular expressions have to be put inside JSON strings
- This syntax is based on the TextMate grammar I believe. Use the TextMate Manual for reference "https://macromates.com/textmate/manual/"
- The idea is a syntax can use regular expressions to match various patterns and push/pop "scopes" to mark bits of the file as various parts of the language. Then the Theme you have selected will map specific scopes to preset colors
- You can manually change which syntax is being used currently by clicking the button in the very bottom right of the window. Or by opening the command palette (Ctrl+Shift+P) and looking for something like "Set Syntax: TODO List Syntax"
