# Unclosed File Bug in Python

This repository demonstrates a common but easily overlooked error in Python: failing to properly close files.  Leaving files open can lead to resource exhaustion and data corruption in some cases, especially in scenarios involving exceptions or long-running processes. 

The `bug.py` file shows an example of a function that opens a file but doesn't close it explicitly. The `bugSolution.py` file offers a fix by implementing proper exception handling and `with` statements to ensure file closure.