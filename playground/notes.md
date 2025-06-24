# 📝 Useful Commands for Windows (PowerShell)

Here are a few basic commands that will help you navigate and work with this project in a Windows environment using PowerShell:

---

### Change Directory

Use the `cd` command to move between folders in your terminal.

```powershell
cd path\to\your\folder
```

---

### Run a PowerShell Script

To execute a PowerShell script (e.g., `build.ps1` or `deploy-local.ps1`), use:

```powershell
.\script_name.ps1
```
Example:
```powershell
.\build.ps1
```

---

### Run a Python Script

To run a Python script (e.g., `init_db.py`), use:

```powershell
python path\to\script.py
```
Example:
```powershell
python playground\init_db.py
```

---

### Basic Docker Commands

Here are some useful Docker commands for working with containers and images:

#### List Docker Images

```powershell
docker images
```

#### List Running Containers

```powershell
docker ps
```

#### List All Containers (including stopped)

```powershell
docker ps -a
```

---

### Basic SQLite Commands

When you are inside the SQLite prompt, here are some useful commands:

#### Show All Tables

```
.tables
```

#### Select Data from a Table

```
SELECT * FROM TableName;
```
