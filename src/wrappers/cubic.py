#!/usr/bin/env python

from subprocess import check_call

import arg_parser


def main():
    args = arg_parser.receiver_first()

    if args.option == 'deps':
        print 'iperf'
        return

    if args.option == 'receiver':
        cmd = ['iperf', '-Z', 'cubic', '-s', '-p', args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = ['iperf', '-Z', 'cubic', '-c', args.ip, '-p', args.port,
               '-t', '75']
        check_call(cmd)
        return

def run_first():
	return ['iperf', '-Z', 'cubic', '-c', '127.0.0.1', '-p', '5003', '-t', '75']


if __name__ == '__main__':
    main()
