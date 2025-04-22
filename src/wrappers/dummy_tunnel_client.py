#!/usr/bin/env python2
"""
Dummy Tunnel Client for Pantheon Auto-Test Mode.

This script reads commands from stdin interactively using raw_input()
and immediately echoes "ACK" to stdout. Debug info is printed to stderr.
"""
import sys
import time

while True:
    try:
        line = raw_input("> ")  # Prompt and read input
    except EOFError:
        break
    time.sleep(0.007)  # Simulated processing delay
    sys.stdout.write("ACK\n")
    sys.stdout.flush()
