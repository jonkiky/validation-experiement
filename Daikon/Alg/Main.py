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

def SelectTestCase(changed_function_name,changed_invariant,connected_functions):
    selected=[]
    logger( "start selection:")
    for key in testcases:
        #get list of functions
        T_fns=testcases.get(key).get_functions()
        connected_functions_in_testcase = []
        #find connected function
        for fn in T_fns:
            for connected_function in connected_functions:
                if connected_function in T_fns.get(fn).functionName:
                    connected_functions_in_testcase.append(fn)

        if connected_functions_in_testcase==[]: # if connected function not be found then break
            logger(key+"  Select Test Case : No connected functions found ")
            continue
        for fn in T_fns:
            # find this function in test case
            if changed_function_name in T_fns.get(fn).functionName :#find this changed_function
                Post=T_fns.get(fn).get_postcondition()
                changed_Program_invariant=[]
                #find changed program invariants in this test case
                changed_Program_invariant =findProgramInvariants(T_fns.get(fn).get_postcondition(),changed_invariant)
                if changed_Program_invariant!=[]: # find changed invariant
                    #find Connected functions
                    for connected_fn in connected_functions_in_testcase:
                        if findProgramInvariants(T_fns.get(fn).get_precondition(),changed_Program_invariant)!=[]:
                            selected.append(key)
                            logger(key + " ================found it=================  ")
                        if findProgramInvariants(T_fns.get(fn).get_postcondition(),changed_Program_invariant)!=[]:
                            selected.append(key)
                            logger(key + " ================found it=================  ")
                        logger(  key + " Select Test Case : No changed invariants found in conneceted program ")
                        break
                else:
                    logger( key+" Select Test Case : No changed invariants found ")
            else:
                logger( key + " Select Test Case : No changed function found ")

    return   selected

def findProgramInvariants(Pi1, cPi2):
    changed=[]
    for change in cPi2:
        for pi in Pi1:
            if similar(change, pi) > 0.6:
                changed.append(change)
    return  changed



def getCallgraph(dir):
    #call graph
    with open(dir, "r+") as files:
        for line in files:
            'line = files.read()'
            if (line.startswith("C:")):
                'do nothing'
            else:
                re = line.replace("M:", "").replace("(O)", "").replace("(I)", "").replace("(M)", "").replace("(S)",
                                                                                                             "").replace(
                    "\\n", "").replace(":", ".").split()
                if(callgraph.has_key(re[1])):
                    callgraph.get(re[1]).append(re[0])
                else:
                    callgraph[re[1]]=[re[0]]


log=[]
def logger(str):
    log.append(str);

def saveLogger():
    logpath = "F:\experiment20170325Regression\log\loggerAlg1" + strftime("%Y%m%d%H", gmtime()) + ".txt"
    with open(logpath, 'wb') as f:
        pickle.dump(log,f)


def main():
    mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"
    mypath3 = "F:\experiment20170325Regression\BookStore-master2\daikon\callgraph.txt"
    find_Change_mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"

    find_Change_mfile = find_Change_mypath + "\\" + "BookDaoImplTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "BookDaoImplTest.txt"
    find_Change_fnName = "addBook"

    find_Change_mfile = find_Change_mypath + "\\" + "CategoryDaoImplTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "CategoryDaoImplTest.txt"

    find_Change_fnName = "save"
    find_Change_mfile = find_Change_mypath + "\\" + "CartTest.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "CartTest_modified.txt"
    find_Change_fnName = "Cart()"



    mypath = "F:\experiment20170325Regression\commons-lang-2.1-src"
    mypath3 = "F:\experiment20170325Regression\commons-lang-2.1-src\callgraph.txt"
    find_Change_mypath = "F:\experiment20170325Regression\commons-lang-2.1-src"

    find_Change_mfile = find_Change_mypath + "\\" + "ClassUtilsTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "ClassUtilsTest.txt"
    find_Change_fnName = "primitiveWrapperMap"



    find_Change_mfile = find_Change_mypath + "\\" + "EntitiesTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "EntitiesTest.txt"
    find_Change_fnName = "Unescape"

    find_Change_mfile = find_Change_mypath + "\\" + "ExceptionUtilsTestCase_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "ExceptionUtilsTestCase.txt"
    find_Change_fnName = "getStackFrameList"



    find_Change_mfile = find_Change_mypath + "\\" + "FractionTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "FractionTest.txt"
    find_Change_fnName = "toProperString"

    mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"
    mypath3 = "F:\experiment20170325Regression\BookStore-master2\daikon\callgraph.txt"
    find_Change_mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"
    find_Change_mfile = find_Change_mypath + "\\" + "CategoryDaoImplTest_modified.txt"
    find_Change_ofile = find_Change_mypath + "\\" + "CategoryDaoImplTest.txt"

    find_Change_fnName = "save"
    changed_Invariants = []
    changed_Invariants = findFnAndInv(find_Change_mfile, find_Change_ofile, find_Change_fnName)
    logger("changed_Invariants")
    logger(changed_Invariants)



    testFiles=[]
    testFiles=getAllFiles(mypath)

    getCallgraph(mypath3)
    selected=[]
    for f in testFiles:
        #print f
        mypath2 =mypath+"\\"+f
        parser(mypath2)
    logger("size of testcases :"+str(len(testcases)))
    for fn_change in changed_Invariants.get_functions():
         changed_invariant=fn_change.get_postcondition()
         changed_function_name=fn_change.functionName
         connected_functions=[]
         # find changed function's connected function
         for key in callgraph:
             if find_Change_fnName in key :
                 if callgraph.get(key)!=[]:
                     for item in callgraph.get(key):
                         connected_functions.append(item)

         connected_functions = list(set(connected_functions))
         logger("connected_functions:")
         logger(connected_functions)


         localselected =SelectTestCase(changed_function_name, changed_invariant,connected_functions)
         if localselected!=[]:
              selected.append(localselected)
    logger("selected Test Case:")
    logger(selected)
    print selected
    saveLogger()


if __name__ == "__main__": main()