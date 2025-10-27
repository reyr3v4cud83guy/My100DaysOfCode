# 🚀 Project Setup Guide

This guide will help you set up the Python Learning Journey project on your local machine.

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- A code editor (VS Code recommended)
- Web browser for testing demos

## 🔧 Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/reyr3v4cud83guy/My100DaysOfCode.git
cd My100DaysOfCode
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
# Test a simple Python script
python introduction.py

# Test the calculator
python simple_calculator.py
```

## 🎮 Running Interactive Demos

### Local Development Server
For the best experience with the web demos, run a local server:

```bash
# Using Python's built-in server
python -m http.server 8000

# Then open http://localhost:8000 in your browser
```

### Individual Project Testing
```bash
# Test individual Python projects
python bank_account.py
python expense_tracker.py
python mini_game.py  # Requires pygame
python ml_training.py  # Requires scikit-learn
```

## 📁 Project Structure

```
My100DaysOfCode/
├── demos/                  # Interactive web demos
│   ├── business-apps/     # Business application demos
│   ├── games/             # Game demos
│   ├── smart-tools/       # Utility tool demos
│   └── data-analytics/    # Data analysis demos
├── .github/workflows/     # GitHub Actions
├── .vscode/              # VS Code settings
├── Python files...       # Core Python projects
├── index.html            # Main portfolio page
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🛠️ Development Tools

### Recommended VS Code Extensions
- Python
- Pylint
- HTML CSS Support
- Live Server
- GitLens

### Python Development
```bash
# Install development dependencies
pip install jupyter ipython

# Launch Jupyter for experimentation
jupyter notebook
```

## 🌐 GitHub Pages Setup

The project includes automatic GitHub Pages deployment:

1. Push changes to the main branch
2. GitHub Actions will automatically deploy
3. Site will be available at: `https://yourusername.github.io/My100DaysOfCode/`

## 🐛 Troubleshooting

### Common Issues

**Import Errors:**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

**Pygame Issues:**
```bash
# On Windows, you might need:
pip install pygame --upgrade
```

**Permission Errors:**
```bash
# On macOS/Linux, you might need:
sudo pip install -r requirements.txt
```

### Getting Help

1. Check the [Issues](https://github.com/reyr3v4cud83guy/My100DaysOfCode/issues) page
2. Review the [Contributing Guide](CONTRIBUTING.md)
3. Contact: Osman6176@gmail.com

## 🎯 Next Steps

1. Explore the Python projects in the root directory
2. Try the interactive demos in the `demos/` folder
3. Modify existing projects or create new ones
4. Share your improvements via Pull Requests

---

*Happy coding! 🐍*