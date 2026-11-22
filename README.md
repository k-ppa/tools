# <u>tools</u>

> This is a collection of the useful python programs that I've made over time

## Run this program

1. Install uv if it isn't installed
2. **Open the project's folder 'tools' in the terminal and run these commands:**
	```bash
	uv sync
	uv run main.py
	```
3. The GUI will be opened in another window

> [!TIP]
> Install the font [`Libron`](https://github.com/nicoverbruggen/libron/releases/latest) for the text in the GUI to show up properly

---

## Backend

I use `pywebview` with `Qt WebEngine (pyside6)` to show the web based gui and have python as the backend.
The useful python programs that I made (that wll be added in the future) can be used from this GUI
> I don't use the native WebView for the GUI as Qt WebEngine runs chromium for rendering the webpage. So, the GUI will remain the same regardless of the OS or device *(hopefully)*
> 'qt' also allows the window to have a custom icon

> [!NOTE]
> Dragging the window may be laggy as the program uses qt. Replace the given line in `main.py` to reduce the lag.
> ```python
> webview.start(gui="qt", debug=False, icon=str(logo))
> # Find the above line in main.py and replace it with the line given below
> webview.start(debug=False, icon=str(logo))
> 
> # Just remove `gui="qt"` so that the program won't use Qt WebEngine
> # Doing this might change how the GUI looks
> ```
