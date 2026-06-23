# ✅ Task Manager – by CAgent_47


A simple but powerful task manager built with Python and tkinter.
It works offline, saves tasks in a .txt file, and keeps your shit organized — because who has time to remember everything?

# Update(V1.3):

**your tasks saving in json file**
**Swith from tkinter to CLI**
**Delete Task Soon...**
**Show Task In CLI**

## 🔧 What it does  

- ➕ Add a task — it automatically adds a timestamp  
- 🧾 Shows all tasks in a clean list  
- 🗑️ Delete everything at once (but first, it asks: “Are you sure?”)  
- ⚠️ No empty tasks allowed — because that’s just浪费时间  

## 📁 How it saves tasks  

Tasks are saved in a simple `config.json` file like this:

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

Maximum Task = 100
if tasks equal 100:
```python
def deleteAllTask():
    if os.path.exists(configuration):
        result = input('Are you sure you want to delete ALL tasks? (y/n): ')
        if result.lower() == 'y':
            with open(configuration, 'w') as f:
                json.dump([], f, indent=4)
            print("All tasks deleted.")
            return True
        else:
            print("Deletion cancelled.")
            return False
    return False

print("ERROR: Maximum tasks reached!")
if deleteAllTask():
    task_list = []
```
**Note:** 
*This function is responsible for managing so that the number of tasks does not increase to the point where it slows down the execution of the program.*

---
## 🛠️ Run it yourself  

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

![Download_Me](https://github.com/CAgent47/TaskManager/archive/refs/heads/main.zip)

```bash
git clone https://github.com/CAgent_47/task-manager.git
cd '[CAgent_47]TaskManager'
python main.py
```

📄 License

MIT — do whatever you want with it. Just don’t blame me if it breaks your Linux. 😄

---

# -👤Created By CAgent_47

# -📜MTA Scripter • Linux Learner🐧 • Python Learner • SQL • Bash Scripter 🇺🇸🔥

**Topics:** 
[#bash](https://github.com/topics/bash) •
[#linux](https://github.com/topics/linux) •
[#python](https://github.com/topics/python) •
[#debian](https://github.com/topics/debian) •
[#ubuntu](https://github.com/topics/ubuntu) •
[#CAgent_47](https://github.com/topics/CAgent47)

---

![Banner](banner.png)
