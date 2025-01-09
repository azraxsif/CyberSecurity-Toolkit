# Advanced Port Scanner ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) [![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)
***Overview***
---
This was one of the earliest CyberSecurity tools I built for fun. This is a basic yet powerful multi-threaded port scanner written in Python. It checks a set of ports on a given IP address or hostname, detecting open ports and capturing service banners where possible. The results are stored as a text file for future reference. 

---
## *Reasons why my project stands out*
| Feature             | Description                                      |
|---------------------|--------------------------------------------------|
| Multi-threading     | Fast port scanning simultaneously                |
| Banner grabbing     | Detects service banners on open ports            |
| Output logging      | Saves results to `scan_results.txt`              |
| Hostname Resolution | Automatically resolves hostnames to IP addresses |

---
## *How It Works*
---
- Accepts a target IP address or hostname, as well as a port range for scanning.
- Resolves the hostname into an IP address (if relevant).
- TCP is used to check the status of all ports within the defined range.
- Identifies open ports and attempts to obtain service banners.
- Logs open ports to a file and shows results on the console.
---

## *Installation*
1. Clone the repository:
```bash
git clone https://github.com/azraxsif/port_scanner.git
cd port_scanner
```
2. Make sure Python 3.6+ is installed.
3. No external libraries are required—this script uses Python's built-in modules.
---

## *Usage*
1. Run the script:

```bash
python port_scanner.py
```

2. Follow the prompts.

3. Let the magic happen!

4. Example output:

```yaml
=== Advanced Port Scanner ===
Enter target IP or hostname: scanme.nmap.org
Enter start port: 20
Enter end port: 80
[INFO] Resolved scanme.nmap.org to 45.33.32.156
[INFO] Starting scan...
Target: 45.33.32.156
Ports: 20-80
Scan started at: 2025-01-09 10:00:00

[+] Port 22 is OPEN. Banner: SSH-2.0-OpenSSH_7.6
[+] Port 80 is OPEN. Banner: HTTP/1.1 400 Bad Request

[INFO] Scan completed at: 2025-01-09 10:01:00
Scanning complete. Results saved to scan_results.txt.

```
---
## *Customisation*
- Change the timeout for connecting attempts by altering the sock.The scan_port method includes a settimeout(1) line.
- Port Range: Enter a specific port range, or scan common ports by default.
- Output file: Change the filename or enable more thorough logging.
---
## *Limitations*
- Scanning is only supported over TCP.
- Filtered ports cannot be detected if a firewall discreetly drops packets.
- Certain services have limited banner grabbing capabilities.
---
## *Future Improvements*
- Include functionality for UDP scanning.
- Include OS and service detection capabilities.
- Create a graphical user interface (GUI) for simplicity of usage.
---
## *License*
This project is licensed under the MIT License. See the LICENSE file for details.
---
## Acknowledgments
Inspired by the functionality of tools like Nmap.
Built using Python's socket and threading libraries for efficient networking and performance.

---
## Contact
For questions, feedback, or contributions:
# [![GitHub](https://img.shields.io/badge/GitHub-azraxsif-pink)](https://github.com/azraxsif)
# [asifazra03@gmail.com](mailto:asifazra03@gmail.com) 





