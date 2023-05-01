# number-system-conversion
:arrows_counterclockwise: System for converting numbers from certain bases to others.

## Introduction

Basically, this project is a web system that transforms numbers from a specific base (which can be decimal, binary, octal or hexadecimal) to another base (following the same bases available for input). For example, it converts a number in base Octal to Hexadecimal, Binary to Decimal, Decimal to Octal, etc.

The idea for this project was taken from [app-ideas](https://github.com/florinpop17/app-ideas), and basically, it's my first personal project creating an API + Front integration.

To create the API I used Python and the [Sanic](https://sanic.dev/en/) library. As for the front, I used [Bootstrap](https://getbootstrap.com/) to facilitate the creation of the layout, however, for communication with the API, pure Javascript was used.

## Running the System

To facilitate the execution of this system, I suggest that you use [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).

Using your terminal, go to the root directory of that project and run the following command:

```
docker-compose up
```

If you want to stop the execution, just press CTRL + C.

## Accessing the system in your browser

To use the system, access "[http://localhost:8888](http://localhost:8888)" in your browser.

## Final considerations

Again, this is my first project integrating an API and Front, so don't be too hard on me, haha. Any suggestions are welcome and I'd love to hear them. Cya! :-)