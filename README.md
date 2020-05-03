# Script to hold down W key in game

Sometimes in game we need to hold down W key for a long time but not much usage of A/S/D. If you are lazy like me, you can use this script to hold down and release W key whenever required.

**Version 1.0**

The original target of this script is Wot Blitz (Windows 10) but it can be used with any other games with little bit of modifications.

---

#### Requirements

Windows (7/8/8.1/10)

Python 3.7

#### How to use

Install python 3.7 if not done already

From windows PowerShell install its required dependancies.
```python
pip3 install pywin32
pip3 install pynput
```
Then run the script in windows PowerShell or Command Prompt using command `python w_press.py`.
The script will keep running in the window and start monitoring the keystrokes from desired program (WoT Blitz as of now). 

Then switch to the game window or start the game.
Press **Q** to hold the W key.
Press **S** or **Q** again to release the W key.

### Features

- The desired program or window can be changed as per requirements and some modifications.
- The script will stop monitoring keystrokes as soon as you switch to another window using **Alt+Tab**.
- **Esc** key press will stop monitoring the keystrokes and exit from the script.

### Known bugs

- Unexpected behaviour when pressing Alt+Tab while the W key is being held by script
- Keypress monitoring will not stop automatically if game window is minimized or switched to other window using Win+Tab
