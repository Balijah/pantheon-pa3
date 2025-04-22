#!/usr/bin/env python

import sys
import json

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "run_first":
        print json.dumps(["python", "./src/experiments/vegas_receiver.py"])
    else:
        print json.dumps(["python", "./src/experiments/vegas_sender.py"])

if __name__ == "__main__":
    main()
