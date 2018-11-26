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
  subprocess.check_output(['git', 'checkout', branch])
  log_output = subprocess.check_output('git', 'log', '--oneline')
  log_lines = log_output.split("\n")
  log_words = [ x.split() for x in log_lines ]
  commits = [x[0] for x in log_words if len(x) > 0]
  for commit in commits
    subprocess.check_output(['git', 'checkout', commit])
    maven_output = subprocess.check_output(['mvn', 'package'])
    #go to the path
    unzip_output = subprocess.check_output(['unzip', arguments.buildartifactpath, '-d', arguments.buildartifactpath+".unzipped"])
    unzip_output2 = subprocess.check_output(['unzip', arguments.comparisonartifactpath, '-d', arguments.comparisonartifactpath+".unzipped"])
    diff_output = subprocess.check_output(['diff -r', arguments.buildartifactpath+".unzipped", arguments.comparisonartifactpath+".unzipped"])

pdb.set_trace()
