# Auto Attend My Best BSI

![Build](https://github.com/ccrsxx/autobsi/actions/workflows/codeql-analysis.yml/badge.svg)
[![Heroku](https://pyheroku-badge.herokuapp.com/?app=bsi)](https://autobsi.herokuapp.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## About

This is a script that allows you to automatically attend your class on the My Best BSI site. It features a scheduler that will automatically starts the script when your class starts, it it also able to run when you are inside your class schedule. You can run it on your own computer or host it on a cloud server like heroku.

## Prerequisites

Make sure you have installed all of the following prerequisites on your machine:

- Python - [Download & Install Python](https://nodejs.org/en/download/).
- Git - [Download & Install Git](https://git-scm.com/downloads).
- Google Chrome version 90 or higher.

## Setup

First before running the script. You need to set up the `src/config.json` to allow the script to log in and attend the class. Follow these steps:

1. In the timetable section, you can find days for classes that you have to take per week. Change those days based on your schedule. Make sure it's written in English and typed correctly.
2. Inside the timetable you can find the name, time, and link. The name is for your class name, you can name it whatever you want here. The time is your class schedule, it's a list that consists of when your class starts and ends, it's formatted as 'HH:MM' i.e '12:30'. The link is the URL of the class that you attend, you can get it on My Best in your class attendance section.
3. The last section is username (nim) and password. This data is used to allow the script to log in to your My Best Account.

**Cloud tutorial coming soon...**

**Note**: If you have multiple classes a day, you will need to wrap your class name, time, and link to a list. The time section is always a list, so it's nested inside a list when you have more than one class a day. See the example at Thursday class on the default `src/config.json`.

## Installation

Follow all these steps shown below to use the script.

1. Clone this repository. Run:

   ```bash
   git clone https://github.com/ccrsxx/autobsi.git
   ```

2. Change the directory to the autobsi folder. Run:

   ```bash
   cd autobsi
   ```

3. Install the dependencies with pip. Run:

   ```bash
   pip install -r requirements.txt
   ```

4. Install the webdriver for selenium. Run:

   ```bash
   python setup.py
   ```

5. Run the script:

   ```bash
   python main.py
   ```
