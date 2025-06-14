# Signal Encoder App

A desktop application built with Python and Kivy that visualizes various digital encoding schemes based on binary input. This tool helps understand how binary data is translated into physical signals in digital communication.

## Features

* **Binary Input:** Easily input a sequence of binary '0's and '1's.
* **Multiple Encoding Schemes:**
    * NRZ-L (Non-Return-to-Zero Level)
    * NRZ-I (Non-Return-to-Zero Invert)
    * RZ (Return-to-Zero)
    * Manchester Encoding
    * Differential Manchester Encoding
* **Real-time Signal Visualization:** See the waveform drawn dynamically based on the selected encoding scheme.
* **Clear Functionality:** Reset the input and signal display for new experiments.
* **Interactive UI:** User-friendly interface with buttons for each encoding type.
* **Custom Styling:** Features a custom welcome message, button colors, and a visually appealing signal display area with grid lines and voltage labels.

## Technologies Used

* **Python:** The core programming language.
* **Kivy:** A powerful, open-source Python framework for developing cross-platform applications (including desktop and mobile GUIs).

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.x installed on your system.
* `pip` (Python package installer).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/abdulwaheedrrr/signalEncoder_App.git](https://github.com/abdulwaheedrrr/signalEncoder_App.git)
    cd signalEncoder_App
    ```

2.  **Install Kivy:**
    It's recommended to use a Python virtual environment.
    ```bash
    # (Optional) Create a virtual environment
    python -m venv venv
    # (Optional) Activate the virtual environment
    # On Windows: .\venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate

    pip install kivy
    ```
    (Ensure Kivy is installed correctly for your OS as per Kivy's official documentation if you face issues).

### Running the Application

Once Kivy is installed, you can run the application directly:

```bash
python main_program.py

