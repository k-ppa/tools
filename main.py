# NOTE: Get color palette from internet and use it

from pathlib import Path

import webview

gui_files = Path(__file__).parent / "gui"
home = gui_files / "index.html"
home_icon = gui_files / "icons" / "house.svg"
theme_icon = gui_files / "icons" / "palette.svg"
logo = gui_files / "icons" / "tool-case.svg"

state = {"min": False, "max": False}
print("Loading...", end="", flush=True)


def window_minimized():
    state["min"] = True
    window.evaluate_js('max.firstElementChild.src = "../../icons/maximize.svg";')  # ty: ignore[missing-union-attribute]
    print("Minimized")


def window_maximized(maximized: bool = True):
    if maximized:
        state["max"] = True
        window.evaluate_js('max.firstElementChild.src = "../../icons/minimize.svg";')  # ty: ignore[missing-union-attribute]
        print("Maximized")
    else:
        state["max"] = False
        if not state["min"]:
            window.evaluate_js(  # ty: ignore[missing-union-attribute]
                'max.firstElementChild.src = "../../icons/maximize.svg";'
            )
            print("Restored from maximized")
        else:
            print("Restored from minimized")
    state["min"] = False


class Api:
    def minimize(self):
        window.minimize()  # ty: ignore[missing-union-attribute]
        print("Minimize function ran")

    def maximize(self, mode="auto"):
        if (state["max"] or mode == "restore") and mode != "maximize":
            window.restore()  # ty: ignore[missing-union-attribute]
            print("Maximize function ran (restored)")
        else:
            window.maximize()  # ty: ignore[missing-union-attribute]
            print("Maximize function ran (maximized)")

    def close(self):
        window.destroy()  # ty: ignore[missing-union-attribute]
        print("Close function ran")


api = Api()
window = webview.create_window(
    title="tools",
    url=str(home),
    js_api=api,
    frameless=True,
    easy_drag=False,
    resizable=True,
    transparent=False,  # I don't think this is supported on windows
    text_select=False,  # Causes some wierd stuff when dragging the window
    draggable=False,  # Enable this to drag and drop files
    # (needs some other complex functions for `draggable` to work)
)
if window is None:
    raise RuntimeError("Failed to create WebView window")

window.events.before_show += lambda: print("\rGUI Loading...", end="")
window.events.loaded += lambda: print(
    "\rGUI opened in another window",
    "\nPress 'Ctrl'+'C', press the close button in the GUI or close this terminal to close the program",
    flush=True,
)
window.events.closed += lambda: print("Window destroyed")
window.events.maximized += lambda: window_maximized()
window.events.restored += lambda: window_maximized(False)
window.events.minimized += lambda: window_minimized()
webview.start(gui="qt", debug=False, icon=str(logo))
print("WebView event loop ended")
print(
    "Close this terminal if it hasn't automatically closed "
    "as the program may keep running in the background (sometimes)"
)
