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

def SelectTestCase(changed_function_name,changed_invariant):
    selected=[]
    logger( "start selection:")
    for key in testcases:
        #get list of functions
        T_fns=testcases.get(key).get_functions()

        for fn in T_fns:
            # if  changed_function_name != T_fns.get(fn).functionName :
            #     continue

            # find this function in test case
            changed_Program_invariant=[]
             #find changed program invariants in this test case
            # changed_Program_invariant =findProgramInvariants(T_fns.get(fn).get_postcondition(),changed_invariant)
            # if changed_Program_invariant!=[]: # find changed invariant
            #     selected.append(key)
            #     changed_Program_invariant = []
            #     logger(key + " ================found it=================  ")
            #     logger(" ================changed_Program_invariant =================  ")
            #     logger(changed_Program_invariant)
            #     logger( " ================get_postcondition =================  ")
            #     logger(T_fns.get(fn).get_postcondition())
            #     logger(" ================changed_invariant =================  ")
            #     logger(changed_invariant)
            #     break
            changed_Program_invariant = findProgramInvariants(T_fns.get(fn).get_precondition(), changed_invariant)
            print  1
            if changed_Program_invariant != []:  # find changed invariant
                selected.append(key)
                logger(key + " ================found it=================  ")
                logger(" ================changed_Program_invariant =================  ")
                logger(changed_Program_invariant)
                logger(" ================get_precondition =================  ")
                logger(T_fns.get(fn).get_precondition())
                logger(" ================changed_invariant =================  ")
                logger(changed_invariant)
                break
            logger( key+" Select Test Case : No changed invariants found ")

    return   selected

def findProgramInvariants(Pi1, cPi2):
    changed=[]
    for change in cPi2:
        for pi in Pi1:
            if similar(change,pi)>0.85:
                changed.append(change)
    return  changed



log=[]
def logger(str):
    log.append(str);
    #print str;

def saveLogger():
    logpath = "F:\experiment20170325Regression\log\loggerAlg2" + strftime("%Y%m%d%H", gmtime()) + ".txt"
    with open(logpath, 'wb') as f:
        pickle.dump(log,f)


def main():

    find_Change_mypath = "F:\experiment20170325Regression\commons-lang-2.1-src"
    find_Change_mfile = find_Change_mypath + "\\" + "BookDaoImplTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "BookDaoImplTest.txt"
    find_Change_fnName = "addBook"
    find_Change_mfile = find_Change_mypath + "\\" + "CategoryDaoImplTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "CategoryDaoImplTest.txt"
    find_Change_fnName = "save"

    find_Change_mfile = find_Change_mypath + "\\" + "CartTest.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "CartTest_modified.txt"
    find_Change_fnName = "Cart()"

    find_Change_mfile = find_Change_mypath + "\\" + "NumberUtilsTest.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "NumberUtilsTest_modified.txt"
    find_Change_fnName = "isNumber"


    changed_Invariants = []
    changed_Invariants = findFnAndInv(find_Change_mfile, find_Change_ofile, find_Change_fnName)
    logger("changed_Invariants")
    logger(changed_Invariants)


    mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"

    mypath = "F:\experiment20170325Regression\commons-lang-2.1-src"
    testFiles=[]
    testFiles=getAllFiles(mypath)
    selected=[]
    for f in testFiles:
        #print f
        mypath2 =mypath+"\\"+f
        parser(mypath2)
    logger("size of testcases :"+str(len(testcases)))

    for fn_change in changed_Invariants.get_functions():
         changed_invariant=fn_change.get_postcondition()
         changed_function_name=fn_change.functionName
         localselected =SelectTestCase(changed_function_name, changed_invariant)
         if localselected!=[]:
              selected.append(localselected)
    logger("selected Test Case:")
    logger(selected)
    print dict.fromkeys(selected[0]).keys()
    #saveLogger()


if __name__ == "__main__": main()