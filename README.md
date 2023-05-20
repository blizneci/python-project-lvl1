# Brain Games

[![Actions Status](https://github.com/blizneci/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/blizneci/python-project-lvl1/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/77c9d0297ea0ce915756/maintainability)](https://codeclimate.com/github/blizneci/python-project-lvl1/maintainability)

## About this project

This is a set of 5 games for your brain.
## Games:
- Even or not
- Calculator
- Greatest common divisor
- Progression
- Prime number

#### Even or not

You will be given a number. You need to answer whether it is [even](https://en.m.wikipedia.org/wiki/Parity_(mathematics)) or not.
Answer "yes" if given number is even, otherwise "no".

[![asciicast](https://asciinema.org/a/585545.svg)](https://asciinema.org/a/585545)

#### Calculator

You will be given an arithmetic expression. You need to calculate the result and enter it as an answer.

[![asciicast](https://asciinema.org/a/cvIvJRDY7nyUF4RcgpylNhkka.svg)](https://asciinema.org/a/cvIvJRDY7nyUF4RcgpylNhkka)

#### Greatest common divisor

You will be given two numbers. You need to find the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) and enter it as an answer.

[![asciicast](https://asciinema.org/a/9gIlMvVjq44rBu6qz8SzeDMqS.svg)](https://asciinema.org/a/9gIlMvVjq44rBu6qz8SzeDMqS)

#### Progression

You will be given an [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression) with one missing number.
You need to figure out this missing number and enter it as an answer.

[![asciicast](https://asciinema.org/a/cIdzzJ7Meshnsjbg2gcLPQKcf.svg)](https://asciinema.org/a/cIdzzJ7Meshnsjbg2gcLPQKcf)

#### Prime number

You will be given a number. You need to answer whether it is a [prime number](https://en.wikipedia.org/wiki/List_of_prime_numbers) or not.

[![asciicast](https://asciinema.org/a/wApTrkPC3zc72BjcxcQhfsCFd.svg)](https://asciinema.org/a/wApTrkPC3zc72BjcxcQhfsCFd)

## Installation

Use python3.11 or higher and package manager [poetry1.2.0](https://python-poetry.org/docs/) or higher to install dependencies, build and install package.
Use ```make install``` to install dependencies, ```make build``` to build and ```make package-install``` to install games.

## Usage

Every game asks 3 question. If your answer isn't correct, the game will finish. To start game just run these commands in the terminal:
- ```brain-even``` for Even or not game
- ```brain-calc``` for Calculator game
- ```brain-gcd``` for Greatest common diviser game
- ```brain-prime``` for Prime number game
- ```brain-progression``` for Progression game
