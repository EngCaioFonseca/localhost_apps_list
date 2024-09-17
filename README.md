# App Launcher

App Launcher is a Streamlit-based application that helps you discover and launch other Streamlit applications running on your local machine. It scans a range of ports, identifies running Streamlit apps, and provides an easy-to-use interface to launch them.

## Features

- Automatically detects Streamlit applications running on ports 8501-8520
- Displays app titles, port numbers, and additional metadata
- Provides unique color identifiers for each app
- Shows app status, response time, and content size
- One-click launch of any detected application
- Refresh functionality to update the list of running apps

## Requirements

- Python 3.7+
- Streamlit
- Requests

## Installation

1. Clone this repository or download the `app_list_server.py` file.

2. Install the required packages:

bash
pip install streamlit requests


## Usage

1. Run the App Launcher:
bash
streamlit run app_list_server.py


2. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

3. You will see a list of all detected Streamlit applications running on your local machine.

4. Click on any app's button to launch it in a new tab.

5. Use the "Refresh" button to update the list of running applications.

## How it works

- The launcher scans ports 8501-8520 to find running Streamlit applications.
- For each detected app, it fetches the app's title and some basic metadata.
- A unique color is generated for each app based on its title for easy visual identification.
- The interface displays each app's title, port, status, response time, and content size.

## Customization

You can modify the `app_list_server.py` file to:

- Change the range of ports scanned (modify the `start_port` and `end_port` parameters in the `find_running_apps` function call)
- Adjust the metadata displayed for each app (modify the `get_app_metadata` function)
- Customize the color generation for app identifiers (modify the `get_color_for_app` function)

## Troubleshooting

- If you're not seeing any apps, make sure you have Streamlit applications running on the expected ports.
- Check that your firewall isn't blocking the launcher from accessing other local ports.
- If metadata isn't loading for some apps, try increasing the timeout in the `requests.get()` calls.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](link-to-your-issues-page).

## License

[MIT](https://choosealicense.com/licenses/mit/)
