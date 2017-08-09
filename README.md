# PyDuckGen
[![GitHub release](https://img.shields.io/github/release/thoughtfuldev/pyduckgen.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/thoughtfuldev/pyduckgen.svg?style=social&label=Star&style=flat-square)]()
[![GitHub commits](https://img.shields.io/github/commits-since/thoughtfuldev/pyduckgen/1.1.0.svg)]()

- [Introduction](#introduction)
- [Usage](#usage)
  - [Installation](#installation)
  - [Commands](#commands)
- [Adding new payloads](#adding-new-payloads)

![PyDuckGen Startscreen](http://i.epvpimg.com/DeQwcab.png)
---
## Introduction
PyDuck is a Python Script which helps you to get your once written USB Rubber Ducky Payloads onto your Duck's SDCard quickly. You can even change variable components by using a simple `set <attribute> <val>` command.
All of this is made easy with a Metasploit like interface.
Simply choose your payload with `<payload>`, configure it and there you go :)

## Usage

**Tested with Python 3.5.2**

### Installation
1. Download the [latest release](https://github.com/ThoughtfulDev/PyDuckGen/releases).
2. Run.
3. ???
4. Profit

**OR (if you want the Dev Version)**
0. Need Python 3.5.2 or higher...duhhh
1. Clone the Repo:
`git clone https://github.com/ThoughtfulDev/PyDuckGen.git`
2. Install dependencies: `cd PyDuckGen && pip install -r requirements.txt`
3. Start: `python PyDuckGen.py`
4. Enjoy

### Commands
You can get a list of all available commands by typing `help` at any time.

![Normal Commands](http://i.epvpimg.com/8MqGaab.png)

![Payload Commands](http://i.epvpimg.com/uxCOdab.png)

#### Example Payload Generation
```
pyd> hello_world
pyd (hello_world)> attributes
...
pyd (hello_world)> set language de
pyd (hello_world)> set sdcard_mount H:\
pyd (hello_world)> set text Hello Github <3
pyd (hello_world)> generate
```
You SDCard mounted on H:\ should now have the right inject.bin on its USB Stick ready to go :)
(It should open notepad and type 'Hello Github <3')

Here is another demontration.
```
pyd> mimikatz_lazagne_twinduck
pyd (mimikatz_lazagne_twinduck)> attributes
...
pyd (mimikatz_lazagne_twinduck)> set uac_bypass_key j
pyd (mimikatz_lazagne_twinduck)> set language de
pyd (mimikatz_lazagne_twinduck)> gen
```

As you can see if the Payload bypasses UAC you can set the key for bypassing e.g for US its ALT + y for Germany it is ALT + j.

## Adding new payloads
Each payload or module has its own folder in 'modules/'. Every module needs a module.json which is kind of a configuration file about its name, description, needed folders on the ducky, needed files and replacable attributes. Have a look at the existing modules and you should get the hang of it... at least i hope so...

If you want to have your Payload added feel free to make a pull request.
