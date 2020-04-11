"""
network_test_job.py

Example multi-testscript job file

"""
# see https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html
# for how job files work

__author__ = "Hank Preston"
__copyright__ = "Copyright (c) 2019, Cisco Systems Inc."
__contact__ = ["hapresto@cisco.com"]
__credits__ = []
__version__ = 1.0

import os
from pyats.easypy import run

# compute the script path from this location
SCRIPT_PATH = os.path.dirname(__file__)


def main(runtime):
    """job file entrypoint"""

    # run script
    run(
        testscript=os.path.join(SCRIPT_PATH, "testbed_connection.py"),
        runtime=runtime,
        taskid="Device Connections",
    )
    run(
        testscript=os.path.join(SCRIPT_PATH, "interface_errors.py"),
        runtime=runtime,
        taskid="Interface Errors",
    )
