# Motion Detector (IoT_LaB)

A command-line Python application that reads sensor data from an IoT device through the **ThingSpeak API**. It shows the CPU temperature and motion-detection status of a Raspberry Pi-style sensor setup as text or as graphs. The app also includes a login system, a unit converter and two small games.

## Table of Contents

1. [Purpose](#purpose)
2. [Features](#features)
3. [Prerequisites and Dependencies](#prerequisites-and-dependencies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Maintainer](#maintainer)

## Purpose

The project was created to practise working with a web API, JSON data, data visualisation and menu-driven programs in Python. It fetches the latest readings from a ThingSpeak channel and presents them in a way that is easy to read:

- **Text view**: each reading is printed with a status message such as *IT is OK* or *IT IS ON FIRE!*.
- **Graph view**: temperature and movement are plotted over time.

## Features

- Fetch the **N most recent** readings from ThingSpeak
- Show temperature in **Celsius** or **Fahrenheit**
- Display results as **text** or as **graphs** (matplotlib)
- Save results to a JSON history file
- Sign up / sign in with user rights (`viewer`, `super-user`, `admin`)
- Unit converter for temperature, length and weight
- Games: Number Guessing and Rock Paper Scissors

| Reading | ThingSpeak field | Description |
|---------|------------------|-------------|
| Movement | `field1` | `1` = movement detected, otherwise no movement |
| CPU temperature | `field2` | Temperature in °C (converted to °F on request) |

## Prerequisites and Dependencies

- **Python 3.8** or newer
- An **internet connection** (the app calls the ThingSpeak API)
- A desktop environment that can open matplotlib windows (needed for the graph view)

External libraries:

| Library | Used for |
|---------|----------|
| [`requests`](https://pypi.org/project/requests/) | Sending HTTP requests to the ThingSpeak API |
| [`pandas`](https://pypi.org/project/pandas/) | Organising the readings into a data frame |
| [`matplotlib`](https://pypi.org/project/matplotlib/) | Drawing the temperature and movement graphs |
| [`colorama`](https://pypi.org/project/colorama/) | Coloured text in the terminal menus |

## Installation

1. **Clone or download** the repository and open the project folder:

   ```bash
   git clone https://github.com/Uunii/1st-Year-at-LAB-University/edit/main/First_Half/Introduction_to_IoT_Pipeline_course/Movement_App
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the user database.** The app expects a `user-data.json` file in the same folder. Create it with an empty list:

   ```bash
   echo "[]" > user-data.json
   ```

## Usage

Start the program from the project folder:

```bash
python M_App_Main.py
```

### Example session

1. Choose **2 - Sign up** and create an account.
2. Choose **1 - Sign in** and log in with your username and password.
3. In the main menu choose **2 - Motion Detector**.
4. Pick a temperature unit (**1** Celsius or **2** Fahrenheit), then **1 - Text** or **2 - Graph**.
5. Enter how many results you want to see, for example `5`.

Example text output:

```text
Connecting to API...
 Status code: 200
Getting recent 5 results...

Date: 2024-10-14 Time: 12:30:05
The temperature of the CPU is 48.3°C IT is OK
Movement detected: NO
```

After viewing the results, the app asks whether to save them to `History_C.json` (Celsius) or `History_F.json` (Fahrenheit).

### Main menu options

| Option | Action |
|--------|--------|
| `1` | Unit converter |
| `2` | Motion Detector (ThingSpeak readings) |
| `3` | Admin page (admins only) |
| `4` | Games |
| `0` | Log out |

> **Note:** Passwords are stored as plain text in `user-data.json`. This project is for learning purposes and should not be used to store real credentials.

## Project Structure

```text
motion-detector/
├── M_App_Main.py       # Main program
├── requirements.txt    # Python dependencies
├── user-data.json      # User accounts (create manually)
├── History_C.json      # Saved Celsius results (created by the app)
└── History_F.json      # Saved Fahrenheit results (created by the app)
```
