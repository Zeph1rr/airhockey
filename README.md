#AIR HOCKEY

## Table of contents
 - [Usage](#Usage)
 - [Rules](#Rules)
 - [Controls](#Controls)
 - [Demo gif](#Demo)

## Usage

First of all, you should clone the project and install requirements

### Windows
```bash
git clone https://github.com/Zeph1rr/airhockey.git
cd airhockey
pip install -r requirements.txt
```

### MacOS, Linux
```bash
git clone https://github.com/Zeph1rr/airhockey.git
cd airhockey
pip3 install -r requirements.txt
```

Then just start the script and enjoy the game

### Windows
```bash
python .\src\main.py
```

### MacOS, Linux
```
python ./src/main.py
```

## Rules

- Game runs until victory of red or blue player
- Victory is achieved by gaining 6 points by any player
- Player gains point when circle collides with one of the horizontal borders
- You can reset game after victory
- After each collision with a car circle accelerates

## Controls

- W, S - Red car
- Up, Down - Blue car
- Space - Start new game
- Escape - Pause

# Demo

![demo](./readme-images/demo.gif)