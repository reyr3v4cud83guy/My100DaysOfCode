// Universal Theme Toggle Utility for Demos
// Add this script to any demo to enable dark/light mode functionality

// Theme toggle functionality
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  const newTheme = currentTheme === "dark" ? "light" : "dark";

  document.documentElement.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme);

  updateThemeUI(newTheme);
}

function updateThemeUI(theme) {
  const themeIcon = document.getElementById("themeIcon");
  const themeText = document.getElementById("themeText");

  if (themeIcon && themeText) {
    if (theme === "dark") {
      themeIcon.className = "fas fa-sun";
      themeText.textContent = "Light";
    } else {
      themeIcon.className = "fas fa-moon";
      themeText.textContent = "Dark";
    }
  }
}

// Load saved theme on page load
function initializeTheme() {
  const savedTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeUI(savedTheme);
}

// Auto-initialize when DOM is loaded
document.addEventListener("DOMContentLoaded", initializeTheme);

// CSS Variables for consistent theming across all demos
const themeCSS = `
:root {
    --bg-gradient: linear-gradient(135deg, #0ea5e9 0%, #06b6d4 50%, #10b981 100%);
    --card-bg: #ffffff;
    --text-color: #1f2937;
    --text-secondary: #6b7280;
    --border-color: rgba(255, 255, 255, 0.9);
    --shadow: rgba(0, 0, 0, 0.1);
    --accent-color: #0ea5e9;
    --success-color: #10b981;
    --danger-color: #ef4444;
    --warning-color: #f59e0b;
    --info-color: #06b6d4;
}

[data-theme="dark"] {
    --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f766e 100%);
    --card-bg: #1e293b;
    --text-color: #f1f5f9;
    --text-secondary: #94a3b8;
    --border-color: rgba(30, 41, 59, 0.9);
    --shadow: rgba(0, 0, 0, 0.4);
    --accent-color: #06b6d4;
    --success-color: #10b981;
    --danger-color: #f87171;
    --warning-color: #fbbf24;
    --info-color: #0ea5e9;
}

.theme-toggle {
    position: fixed;
    top: 20px;
    right: 20px;
    background: var(--border-color);
    border: none;
    padding: 10px 20px;
    border-radius: 25px;
    cursor: pointer;
    color: var(--text-color);
    font-weight: bold;
    transition: all 0.3s ease;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.theme-toggle:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px var(--shadow);
}

body {
    transition: all 0.3s ease;
}
`;

// Inject theme CSS if not already present
if (!document.querySelector("#theme-styles")) {
  const style = document.createElement("style");
  style.id = "theme-styles";
  style.textContent = themeCSS;
  document.head.appendChild(style);
}
