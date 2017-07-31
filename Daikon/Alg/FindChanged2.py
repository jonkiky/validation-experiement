from Classes import ProgramInvariant,TestCase,Functions

def parser(dir,fnName):
    with open(dir, 'r') as f:
        isPrecondition = False
        isPostcondition=False
        isFunction=False
        functionName=""
        Pre=[]
        Post=[]
        functions={}
        lastFunction=""
        for line in f.readlines():
            if ":::ENTER" in line :# Funtion's preconditon invariants
                if isFunction: # already in function
                    isFunction=False
                    functions[functionName]=Functions(functionName,"", Pre, Post)
                    Pre = []
                    Post = []
                    lastFunction=""
                if fnName in line:
                    isPrecondition = True
                    isPostcondition = False
                    functionName = line.split(":::")[0]
                    lastFunction = functionName
                    isFunction=True
            if isFunction:
                if ":::EXIT"  in line:# Funtion's Post invariants
                    isPrecondition = False
                    isPostcondition = True
                if(isPrecondition):
                    Pre.append(line)
                if (isPostcondition):
                    Post.append(line)
        if lastFunction!="":
            functions[lastFunction]=Functions(functionName, "", Pre, Post)
        return functions


def findFnAndInv(dir,old,fnName):
    fns_modified =parser(dir,fnName)
    fns_orign= parser(old,fnName)
    testcase = TestCase()
    for key in fns_modified:
        fn_modified=fns_modified.get(key)
        fn_orign = fns_orign.get(key)
        if fn_modified=={} and fn_orign!={}:  #the modified function be removed from program
            testcase.__add__(Functions(fns_modified.get(key).functionName, "", "", changed_Invariants))
        if fn_modified!=None and fn_orign==None: #the modified function is a new function to the program
            continue
        if fn_modified == None and fn_orign == None: # must be an error
            continue
        if fn_modified !=None and fn_orign!=None:  # the modified function appear at both orignal program and modified program
            changed_Invariants=[]
            changed_Invariants =findProgramInvariants(fn_modified.get_postcondition(),fn_orign.get_postcondition())
            if changed_Invariants!=[]:
                testcase.__add__(Functions(fns_modified.get(key).functionName, "", "", changed_Invariants))

    return  testcase

def findProgramInvariants(cPi2,Pi1):
    changed=[]
    for pi in Pi1:
        if pi not in cPi2 and "===" not in pi:
            changed.append(pi)
    return  changed




def main():
    find_Change_mypath = "F:\experiment20170325Regression\BookStore-master2\daikon"
    find_Change_mfile=find_Change_mypath+"\\"+"BookDaoImplTest_modified.txt"
    find_Change_ofile=find_Change_mypath+"\\"+"BookDaoImplTest.txt"
    find_Change_fnName="addBook"
    changed_Invariants=[]
    if "Cart()" in "cn.tf.bean.Cart.Cart():::EXIT":
        print "true"
    #changed_Invariants= findFnAndInv(find_Change_mfile,find_Change_ofile,find_Change_fnName)
    print "test"



if __name__ == "__main__": main()