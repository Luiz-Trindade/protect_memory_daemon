<image src="https://www.gnu.org/graphics/gplv3-127x51.png">

# RAM Memory Protector

**Created by:** Luiz Gabriel Magalhães Trindade

**License:** GPL-3.0

---

## Description

The RAM Memory Protector is a simple program designed to monitor RAM memory usage and protect the system from potential memory overflows. It continuously checks running processes and terminates those that exceed a predefined limit. Additionally, the program adapts its behavior based on the system's power profile, ensuring a more aggressive or conservative approach depending on whether the computer is using battery power or connected to the charger.

---

## Features

- **Continuous Monitoring:** The program performs regular checks of RAM memory usage to detect and respond to potential issues.

- **Dynamic Adjustment:** The program's behavior is adjusted based on the system's power profile, providing an adaptive response.

- **Process Termination:** Processes exceeding the defined percentage of memory usage are terminated to prevent overflows.

---

## Requirements

- Python 3.x
- Psutil library (`pip install psutil`)
- python-daemon library (`pip install python-daemon`)

---

## How to Use

1. Ensure you have Python 3.x installed on your system.
2. Install the `psutil` library using the command `pip install psutil`.
3. Run the program using the command `python protect_memory_daemon.py`.

---

## Executable Creation

This program can be bundled into an executable using PyInstaller. Once created, configure the executable to start with the system according to the conventions of your operating system to enable the daemon functionality.

---

## Contributions

Contributions are welcome! Feel free to open issues or send pull requests to improve this project.

---

## License

This program is distributed under the GPL-3.0 license. See the [LICENSE](LICENSE) file for more details.
