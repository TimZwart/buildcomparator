#!/bin/python
import subprocess;
import pdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("buildartifactpath")
parser.add_argument("comparisonartifactpath")
arguments = parser.parse_args();


branchesoutput = subprocess.check_output(['git', 'branch'])
branchesoutputlines = branchesoutput.split("\n")
branchesoutputlineswords = [ x.split() for x in branchesoutputlines ]
branches = [ x[-1] for x in branchesoutputlineswords if len(x) > 0 ]
for branch in branches
  maven_output = subprocess.check_output(['mvn', 'package'])
  #go to the path
  subprocess.check_output(['unzip', arguments.buildartifactpath, '-d', arguments.buildartifactpath.".unzipped"])
  subprocess.check_output(['diff', arguments.buildartifactpath, arguments.comparisonartifactpath])

pdb.set_trace()
