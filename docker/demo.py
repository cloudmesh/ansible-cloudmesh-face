#! /usr/bin/env python
"""Usage:
      demo.py --kind=KIND --count=N
      demo.py gather

Arguments:
  HOST     Host name
  OS       OS name
  KIND     category or classifier

Options:
  -h --help
  -o       OS
"""
from __future__ import print_function

from docopt import docopt
from cloudmesh_client.common.dotdict import dotdict
import os

if __name__ == '__main__':
    arguments = docopt(__doc__)



    arg = dotdict({
        'gather': arguments["gather"],
        'n':  arguments["--count"],
        'kind': arguments["--kind"]
    })

    if arg.gather:
        os.system("gather-csv.sh")
    else:

        if arg.kind == "classifier":
            arg['prg'] = "demo2.sh"
        elif arg.kind == "compare":
            arg['prg'] = "demo3.sh"
        else:
            print ("ERROR: wrong kind")
            sys.exit()

        os.system("docker rm openface")

        os.system("docker run -e HOST=`hostname` "
                  "-e PATH=$PATH:/root/torch/install/bin/ "
                  "-p 9000:9000 -p 8000:8000 "
                  "--name openface "
                  "-v $PWD:/root/openface/docker "
                  "-ti bamos/openface /bin/bash -c \"cd /root/openface/docker; bash ./{prg} {n}\" ".format(**arg))
