# 📝 Useful Shell Commands

Here are a few basic shell commands that will help you navigate and work with this project:

---

### Change Directory

Use the `cd` command to move between folders in your terminal.

```sh
cd path/to/your/folder
```

---

### Run a Shell Script

To execute a shell script (e.g., `build.sh` or `deploy-local.sh`), use:

```sh
./script_name.sh
```
Example:
```sh
./build.sh
```

### Grand execution permission
```sh
chmod +x <filname>
```


---

### Run a Python Script

To run a Python script (e.g., `init_db.py`), use:

```sh
python3 path/to/script.py
```
---

### Basic Docker Commands

Here are some useful Docker commands for working with containers and images:

#### List Docker Images

Shows all Docker images on your system.

```sh
docker images
```

#### List Running Containers

Shows all currently running Docker containers.

```sh
docker ps
```

#### List All Containers (including stopped)

```sh
docker ps -a
```
#### Clean Docker workspace: 
docker system prune -f
---

### Basic SQLite Commands

When you are inside the SQLite prompt, here are some useful commands:

#### Show All Tables

Lists all tables in the current database.

```
.tables
```

#### Select Data from a Table

Shows all rows from a specific table (replace `TableName` with the actual table name).

```
SELECT * FROM <table name>
```
