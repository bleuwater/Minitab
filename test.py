import pandas as pd
from mtbpy import mtbpy
import sys
def main():
        if len(sys.argv[1:]) > 0:
            mtbpy.mtb_instance().add_message("The following arguments were passed to Python: \n{0}".format(sys.argv[1:]))
            for i in range(0,len(sys.argv[1:])):
                if sys.argv[1:][i] == "ArgToBePrintedToStdOut":
                    print("The following arguments were printed to Stdout: '{0}'".format(sys.argv[1:][i]), file=sys.stdout)
                if sys.argv[1:][i] == "ArgToBePrintedToStdErr":
                    print("The following arguments were printed to Stderr: '{0}'".format(sys.argv[1:][i]), file=sys.stderr)
        else:
            mtbpy.mtb_instance().add_message("Minitab successfully located your Python installation.")

main()
