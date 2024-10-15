#!/usr/bin/env python3
import json
import subprocess






def main():
    sub_proc = subprocess.run(["cargo", "run", "--quiet"], capture_output=True, text=True)
    
    stuff = json.loads(sub_proc.stdout)

    print(stuff)
    
main()
