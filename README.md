# PyDuckGen

- [Introduction](#introduction)
- [Usage](#usage)
  - [Installation](#installation)
  - [Commands](#commands)
- [Adding new payloads](#adding-new-payloads)

![PyDuckGen Startscreen](http://i.epvpimg.com/XZogaab.png)

![PyDuckGen Payload Generation](http://i.epvpimg.com/pnn7eab.png)
---
## Introduction
PyDuck is a Python Script which helps you to get your once written USB Rubber Ducky Payloads onto your Duck's SDCard quickly. You can even change variable components by using a simple `set <attribute> <val>` command.
All of this is made easy with a Metasploit like interface.
Simply choose your payload with `use <payload>`, configure it and there you go :)

## Usage

**Tested with Python 3.5.2**

### Installation
0. Need Python 3.5.2 or higher...duhhh
1. Clone the Repo:
`git clone https://github.com/ThoughtfulDev/PyDuckGen.git`
2. Install dependencies: `cd PyDuckGen && pip install -r requirements.txt`
3. Start: `python PyDuckGen.py`
4. Enjoy

### Commands
You can get a list of all available commands by typing `help` at any time.

![Normal Commands](http://i.epvpimg.com/VyQSbab.png)

![Payload Commands](http://i.epvpimg.com/X9cugab.png)

#### Example Payload Generation
```
pyd> use hello_world
pyd (hello_world)> info
...
pyd (hello_world)> set language de
pyd (hello_world)> set sdcard_mount H:\
pyd (hello_world)> set text Hello Github <3
pyd (hello_world)> generate
```
You SDCard mounted on H:\ should now have the right inject.bin on its USB Stick ready to go :)
(It should open notepad and type 'Hello Github')

Here is another demontration.
```
pyd> use mimikatz_lazagne_twinduck
pyd (mimikatz_lazagne_twinduck)> info
...
pyd (mimikatz_lazagne_twinduck)> set uac_bypass_key j
pyd (mimikatz_lazagne_twinduck)> set language de
pyd (mimikatz_lazagne_twinduck)> gen
```

As you can see if the Payload bypasses UAC you can set the key for bypassing e.g for US its ALT + y for Germany it is ALT + j.

## Adding new payloads
Each payload or module has its own folder in 'modules/'. Every module needs a module.json which is kind of a configuration file about its name, description, needed folders on the ducky, needed files and replacable attributes. Have a look at the existing modules and you should get the hang of it... at least i hope so...

If you want to have your Payload added feel free to make a pull request.
