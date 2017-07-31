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

def SelectTestCase(changed_fn):
    selected=[]
    logger( "start selection:")
    for key in testcases:
        #get list of functions
        T_fns=testcases.get(key).get_functions()

        for fn in T_fns:
            # find this function in test case
            changed_Program_invariant=[]
            #find changed program invariants in this test case
            if changed_fn in fn :
                logger(" ================changed_invariant =================  ")
                selected.append(key)
                break
    return   selected



log=[]
def logger(str):
    #print str
    log.append(str);

def saveLogger():
    logpath = "F:\experiment20170325Regression\log\loggerAlg3" + strftime("%Y%m%d%H", gmtime()) + ".txt"
    with open(logpath, 'wb') as f:
        pickle.dump(log,f)


def main():

    changed_function = ["loadResources"]
    logger("changed_function")
    logger(changed_function)


    mypath = "F:\experiment20170325Regression\Validation-result2"
    testFiles=[]
    testFiles=getAllFiles(mypath)
    selected=[]
    for f in testFiles:
        #print f
        mypath2 =mypath+"\\"+f
        parser(mypath2)
    logger("size of testcases :"+str(len(testcases)))


    for changed_function in changed_function:
        localselected =SelectTestCase(changed_function)
        if localselected!=[]:
                  selected.append(localselected)
    logger("selected Test Case:")
    logger(selected)
    print dict.fromkeys(selected[0]).keys()
    saveLogger()


if __name__ == "__main__": main()