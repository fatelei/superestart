# -*- coding: utf8 -*-

import argparse
import xmlrpclib

from datetime import datetime

from croniter import croniter
from supervisor.childutils import listener


def cli():
    """Command line."""
    parser = argparse.ArgumentParser(description="superestart")
    parser.add_argument("--group_name",
                        type=str,
                        dest="group_name",
                        help="group name")
    parser.add_argument("--program_name",
                        type=str,
                        dest="program_name",
                        help="program name")
    parser.add_argument("--crontab",
                        type=str,
                        dest="cron_str",
                        required=True,
                        help="crontab like string")
    parser.add_argument("--api_endpoint",
                        type=str,
                        dest="api",
                        required=True,
                        help="supervisord api endpoint")
    return parser


def main():
    parser = cli()
    args = parser.parse_args()

    server = xmlrpclib.Server("http://%s/RPC2" % args.api_endpoint)
    now = datetime.now()

    time_iter = croniter(args.cron_str, now)
    next_execute_time = time_iter.get_next(datetime)

    if not args.group_name and not args.program_name:
        raise Exception("group_name or program_name should be set")

    group_name = args.group_name
    program_name = args.program_name

    while True:
        listener.ready()
        headers, _ = listener.wait()
        if headers["eventname"] == "TICK":
            cur_now = datetime.now()
            if cur_now >= next_execute_time:
                if group_name:
                    server.supervisor.stopProcessGroup(group_name)
                    server.supervisor.startProcessGroup(group_name)
                elif program_name:
                    server.supervisor.stopProcess(program_name)
                    server.supervisor.startProcess(program_name)
                next_execute_time = time_iter.get_next(datetime)
        listener.ok()


if __name__ == "__main__":
    main()
