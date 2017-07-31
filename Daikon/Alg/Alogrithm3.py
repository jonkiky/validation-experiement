from os import listdir
from os.path import isfile, join
import re
import json
from Classes import ProgramInvariant,TestCase,Functions
import pickle
from FindChanged import  findFnAndInv
from difflib import SequenceMatcher
from time import gmtime, strftime




def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

testcases={}
callgraph={}

def getAllFiles(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f)) if f.endswith('txt')]
    #print onlyfiles
    return onlyfiles


def parser(dir):
    testcase=TestCase()
    testcase.name=dir;
    fns = {}

    with open(dir, 'r') as f:
        isPrecondition = False;
        isPostcondition=False;
        functionName=""
        Pre=[]
        Post=[]

        for line in f.readlines():
            if ":::ENTER" in line:# Funtion's preconditon invariants
                #End of last function
                if functionName!="":
                    fns[functionName]=Functions(functionName,"",Pre,Post);
                    Pre = []
                    Post = []
                isPrecondition = True
                isPostcondition = False
                functionName = line.split(":::")[0]

            if ":::EXIT"  in line:# Funtion's Post invariants
                isPrecondition = False
                isPostcondition = True
            if(isPrecondition):
                Pre.append(line)
            if (isPostcondition):
                Post.append(line)
        fns[functionName] = Functions(functionName,"", Pre, Post);
        testcase.functions=fns
        testcases[dir]=testcase

def SelectTestCase(changed_invariant):
    selected=[]
    logger( "start selection:")
    for key in testcases:
        #get list of functions
        T_fns=testcases.get(key).get_functions()

        for fn in T_fns:
            # find this function in test case
            changed_Program_invariant=[]
             #find changed program invariants in this test case
            changed_Program_invariant =findProgramInvariants(T_fns.get(fn).get_postcondition(),changed_invariant)
            if changed_Program_invariant!=[]: # find changed invariant
                selected.append(key)
                changed_Program_invariant = []
                logger(key + " ================found it=================  ")
                logger(" ================changed_Program_invariant =================  ")
                logger(changed_Program_invariant)
                logger( " ================get_postcondition =================  ")
                logger(T_fns.get(fn).get_postcondition())
                logger(" ================changed_invariant =================  ")
                logger(changed_invariant)
            changed_Program_invariant = findProgramInvariants(T_fns.get(fn).get_precondition(), changed_invariant)
            if changed_Program_invariant != []:  # find changed invariant
                selected.append(key)
                logger(key + " ================found it=================  ")
                logger(" ================changed_Program_invariant =================  ")
                logger(changed_Program_invariant)
                logger(" ================get_precondition =================  ")
                logger(T_fns.get(fn).get_precondition())
                logger(" ================changed_invariant =================  ")
                logger(changed_invariant)

            logger( key+" Select Test Case : No changed invariants found ")

    return   selected

def findProgramInvariants(Pi1, cPi2):
    changed=[]

    for pi in Pi1:
            if cPi2 in pi:
                changed.append(cPi2)
    return  changed



log=[]
def logger(str):
    #print str
    log.append(str);

def saveLogger():
    logpath = "F:\experiment20170325Regression\log\loggerAlg3" + strftime("%Y%m%d%H", gmtime()) + ".txt"
    with open(logpath, 'wb') as f:
        pickle.dump(log,f)


def main():

    changed_Invariants = ["CoreOperationGreaterThan "]
    logger("changed_Invariants")
    logger(changed_Invariants)


    mypath = "F:\experiment20170325Regression\commons-lang-2.1-src"

    mypath="F:\experiment20170325Regression\jxpath-full"
    testFiles=[]
    testFiles=getAllFiles(mypath)
    selected=[]
    for f in testFiles:
        #print f
        mypath2 =mypath+"\\"+f
        parser(mypath2)
    logger("size of testcases :"+str(len(testcases)))


    for changed_invariant in changed_Invariants:
        localselected =SelectTestCase(changed_invariant)
        if localselected!=[]:
                  selected.append(localselected)
    logger("selected Test Case:")
    logger(selected)
    print dict.fromkeys(selected[0]).keys()
    saveLogger()


if __name__ == "__main__": main()