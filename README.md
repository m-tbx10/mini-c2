# Mini Python C2 Framework

A lightweight command-and-control (C2) framework written in Python for educational and authorized security research.


## Overview

This project implements a minimal C2 architecture consisting of:

- A Python-based C2 server
- A modular agent (beacon) that communicates with the server
- A simple tasking and response protocol
- [Optional encryption for agent-server communication]


---

## Features

- HTTP-based agent beaconing
- Tasking system (server → agent)
- Command execution on the agent
- Structured logging
- Modular architecture for future extension
- Configurable communication settings

---

## Project Structure

```
mini-c2/
├── server/ 
├── agent/ 
├── shared/ 
├── logs/ 
├── config.example.py
└── README.md
```

---

## Requirements

- Python 3.9+
- Flask (or FastAPI, depending on your choice)
- requests
- cryptography (optional)

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Start the C2 Server 

```
python server/c2_server.py
```

### Run the Agent

```
python agent/agent.py
```

---

## Disclaimer

This project is intended only for educational purposes and authorized security testing.
Do not deploy this software on systems without explicit permission.

---

## Author

Muhammed Tayyeb

Cyber Security Undergraduate | Offensive Tooling Enthusiast