# pywebview_flask_serving_UI
a pywebview desktop app with the flask server serving the UI on the root endpoint

## About Pywebview
pywebview is a lightweight cross-platform wrapper around a webview component that allows to display HTML content in its own native GUI window. It gives you power of web technologies in your desktop application, hiding the fact that GUI is browser based. You can use pywebview either with a lightweight web framework like Flask (opens new window)or on its own with a two way bridge between Python and DOM. [Docs](https://pywebview.flowrl.com/)

### My personal opinion about pywebview
Pywebview IMO is a fantastic tool to build awesome desktop apps around the python stack. I chose pywebview as my go to because I wanted the flexibility to build the UI as i saw fit (instead of being constrained by some GUI kit like QT, Toga, Flet or Tauri) while being able to take advantage of python and python SDKs for AI/ML/LLM apps.

I personally believe that python is the best tool for data science or AI/LLM apps, so this was a no brainer for me when I discovered it.

### Why QT and not GTK as the webview engine on Linux
I had no idea what the difference was when I got started, and TBH it really didn't make a difference for dev. But when I moved to packaging the app for Windows, getting GTK system dependencies installed on Windows (using GitHub CI) was a nightmare, I wasted hours! Trust me on this, using QT is so much simpler, you'll thank me later.

### Ubuntu dependencies
Now I'm getting even more opinionated. I use Ubuntu to dev, I can't help you on other platforms sorry 😕.

The system dependencies appear to exist already on Ubuntu 24.04 LTS, but just in case they don't exist on your system, [this is what you need](https://pywebview.flowrl.com/guide/installation.html#linux):
`sudo apt install python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebchannel libqt5webkit5-dev`

### Installing python dependencies
The python dependencies should be setup in a virtual environment. The following gets you up and running.
1. install the _virtualenv_ package: `sudo apt update && sudo apt upgrade && sudo apt install -y python3-virtualenv`
2. setup a virtual env in your project root: `virtualenv .venv` where _.venv_ is the name of your virtual env
3. activate the virtual env: `source .venv/bin/activate`
4. install project dependencies: `python -m pip install Flask Flask-Cors Flask[async] pywebview pywebview[qt] qtpy pyside2`

or if you prefer to use the included requirements file: `python -m pip install -r requirements.txt`

NB: To deactivate the virtual env simply type: `deactivate`

### running the app
ensure that you're in the virtual env you created above and it's activated i.e. step 3 above, then execute `python app.py`

All done! 🙌

### Trivia
If you're wondering why `python -m pip install` and not simply `pip install`, ask chatgpt, you'll thank me later.
