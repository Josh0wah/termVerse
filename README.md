**Description:**
termVerse is a simple Python script that will display the Bible verse of the day from VerseOfTheDay.com directly in your Linux terminal.

**Installation:**
  Dependencies:
  1. Make sure Python is installed on your system
     e.g.
     Ubuntu/Debian-based distro:
     $ sudo apt install python
  
     Arch/Arch-based distro:
     $ sudo pacman -S python
  
  2. Install the required Python modules using the following commands
     Ubuntu/Debian-based distro:
     $ sudo apt install python-requests
     $ sudo apt install python-beautifulsoup4
  
     Arch/Arch-based distro:
     $ sudo pacman -S python-requests
     $ sudo pacman -S install python-beautifulsoup4

   3. Download the termVerse.py file to wherever you save your scripts e.g. ~/.scripts

**Usage:**
  You'll likely want to either have termVerse run whenever you launch a new terminal, or assign it to a command

  To run on launch, add the following line to the end of your .bashrc or .zshrc file:
  python path/to/script/termVerse.py

  To assign to a command, add an alias to your .bashrc or .zshrc file
  e.g.
  alias votd='python path/to/script/termVerse.py'
