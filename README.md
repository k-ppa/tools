# <u>tools</u>

This is a collection of the useful tools that I've made

## Run this program

> This project uses [uv](https://docs.astral.sh/uv/) for managing dependencies. Install uv if it isn't already installed on your system

**Open the project's folder 'tools' in the terminal and run this command:**
```bash
uv run main.py
```
Then the GUI will open in another window  
_<ins>Note:</ins> This command will automatically install all the dependencies (including the entire browser engine, which might take some time) when its run for the first time_

> [!TIP]
> [Download](https://github.com/nicoverbruggen/libron/releases/latest/download/Libron.zip) and [Install](https://www.wikihow.com/Install-Fonts-on-Your-PC) the font [`Libron`](https://github.com/nicoverbruggen/libron) for the text in the GUI to show up properly

---

## Backend

I use `pywebview` with `Qt WebEngine (pyside6)` to show the web based gui and have python as the backend.  
The tools can be used from this GUI
> I don't use the native WebView for the GUI as Qt WebEngine runs chromium for rendering the webpage. So, the GUI will remain the same regardless of the OS or device *(hopefully)*
> 'qt' also allows the window to have a custom icon

> [!NOTE]
> Dragging the window may be laggy as the program uses Qt. Replace the given line in `main.py` to reduce the lag.
> ```python
> webview.start(gui="qt", debug=False, icon=str(logo))
> # Find the above line in main.py and replace it with the line given below
> webview.start(debug=False)
> ```
> This just removes `gui="qt"` so that the program won't use Qt WebEngine and will fall back to the webview of the OS, which _might_ have better performance when dragging the window  
> > Doing this changes the browser engine which might change how the GUI looks  
> > Also, this does not support custom icon. Custom icon is only supported when `gui` is set to "qt" or "gtk"
