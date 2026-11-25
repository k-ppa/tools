const min = document.getElementById("min");
const max = document.getElementById("max");
const close = document.getElementById("close");
const header = document.querySelector("header");
const browserText = document.querySelector("#browser");
const sizeText = document.querySelector("#size");

browserText.textContent = navigator.userAgent;
sizeText.innerHTML = `<u>Window's size:</u> ${outerWidth}px x ${outerHeight}px`;

addEventListener("pywebviewready", () => {
	addEventListener("resize", () => {
		sizeText.innerHTML =
			`<u>Window's size:</u> ${outerWidth}px x ${outerHeight}px`;
	});

	min.addEventListener("click", () => {
		pywebview.api.minimize();
	});

	max.addEventListener("click", () => {
		pywebview.api.toggle_maximize();
	});

	close.addEventListener("click", () => {
		pywebview.api.close();
	});

	header.addEventListener("dblclick", (event) => {
		if (event.target.tagName == "HEADER") {
			pywebview.api.toggle_maximize();
		}
	});

	header.addEventListener("mousedown", (event) => {
		if (event.target.tagName == "HEADER") {
			pywebview.api.maximize("restore");
		}
	});
});
