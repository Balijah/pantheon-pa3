#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 5:
    sys.stderr.write("Usage: python2 generate_trace.py <bandwidth_mbps> <delay_ms> <duration_secs> <outfile>\n")
    sys.exit(1)

# Parse command-line arguments
bandwidth_mbps = float(sys.argv[1])      # e.g., 50 for 50 Mbps
delay_ms = float(sys.argv[2])            # e.g., 10 ms (not used in output)
duration_secs = int(sys.argv[3])         # e.g., 60
outfile = sys.argv[4]

# Convert bandwidth to bytes per millisecond
bits_per_ms = (bandwidth_mbps * 1000000.0) / 1000.0
bytes_per_ms = bits_per_ms / 8.0
packet_size = 1500.0  # bytes
accumulator = 0.0
trace = []

# Generate timestamps (in ms) when packets would be sent
for ms in range(duration_secs * 1000):
    accumulator += bytes_per_ms
    while accumulator >= packet_size:
        trace.append(ms)
        accumulator -= packet_size

# Write timestamps to output file
with open(outfile, 'w') as f:
    for t in trace:
        f.write("%d\n" % t)
