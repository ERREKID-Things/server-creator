# 🚀 Server Creator

**Server Creator** is a lightweight tool designed to quickly set up servers on your `localhost` or local PC.

---

## 🛠️ Installation

To install this module directly from GitHub, open your terminal and run the following command:

```bash
pip install git+https://github.com/ERREKID-Things/server-creator.git
```

---

## 💻 How to use

Once installed, you can easily integrate it into your Python project:

### 1. Simple Import
```python
import server

# Example: Start your server
server.start()
```

### 2. Custom Port (Example)
```python
import server

# If your module supports arguments
server.start(port=8080)
```

---

## 📂 Project Structure
To ensure `import server` works correctly after installation, your repository should look like this:

* `setup.py` (Required for pip installation)
* `server/` (Main folder)
    * `__init__.py` (Makes the folder a package)
    * `server.py` (Your main logic)

---

## 🤝 Contributing
If you want to improve **Server Creator**, feel free to fork the repository and submit a Pull Request!

---

*Developed by ERREKID-Things*
