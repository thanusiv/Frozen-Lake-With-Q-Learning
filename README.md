# Frozen Lake using Q-Learning

## Table of Contents

- [Overview](#Overview)
- [Demo](#Demo)
- [How to Load Project](#how-to-load-project)
- [Features](#Features)
- [Technologies Used](#technologies-used)
- [Acknowledgements](#acknowledgements)

## Overview

This is a project that showcases the Q-Learning algorithm. The project is about getting an agent to reach the goal while not stepping into the holes that are placed in the environment. Once the algorithm runs, you can see for yourself how the agent traverses through its environment without any previous knowledge. I implemented both the Frozen Lake environment and Q-Learning algorithm from scratch. The OpenAI Gym library has an environment for the frozen lake game but I wanted to create it myself to fully understand the implementation of this algorithm. 

Try it out for yourself!

## Demo

<img src="gifs/1.gif?raw=true"/> <img src="gifs/2.gif?raw=true"/> <img src="gifs/3.gif?raw=true"/>

## How to Load Project

Clone the Github repository to a local directory. Create a virtual environment if wanted and use `pip install -r requirements.txt` to install all the required dependencies (this project doesn't really require any additional dependencies, so skip this step if you like). Open and run the `main.py` file using an IDE or from the terminal.

## Features

- Implemented both the Q-Learning Algorithm and the Frozen Lake environment from scratch
- Can see the agent traverse the environment after training via the console of the IDE or terminal 
- Environment can be altered to make it bigger but would need to make some small changes to the code to do so
- Use of OOP in Python can be used as template for future projects

## Technologies Used

- [Visual Studio Code](https://code.visualstudio.com/) - IDE used to build the project
- [Python 3.8.3](https://www.python.org/downloads/) - Programming language used

## Acknowledgements

- Thanks to [deeplizard](https://deeplizard.com/) for teaching me about the Q-Learning algorithm!
