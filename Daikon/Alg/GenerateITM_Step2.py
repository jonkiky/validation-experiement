from Classes import ProgramInvariant,TestCase,Functions
import os
import sys
import argparse
import csv

def compareInvs(ppts, invs1, data2):
    results = []
    for i in xrange(0, len(ppts)):
        ppt = ppts[i]
        results.append([])
        if ppt in data2:
            for j in xrange(0, len(invs1[i])):
                inv = invs1[i][j][1]
                if inv in data2[ppt]:
                        results[i].append(1)
                else:
                        results[i].append(0)

        else: #ppt not in buggy version, fill vector with 0s
            for j in xrange(0, len(invs1[i])):
                results[i].append(0)
    return results

def main():
    reader1 = csv.reader()
    reader2 = csv.reader()

if __name__ == "__main__": main()