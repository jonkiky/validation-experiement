#!/usr/bin/env python3
# input two invariant matrix (for validation) A and B
# output a matrix only include invariants that are different between A and B

import os
import sys
import argparse
import csv
from difflib import SequenceMatcher



def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

result ={}
def filter(line1, line2, startCol):
    for i in range(startCol, len(line2)):
        if line2[i] == '0':
            continue
        else:
            if line1[i] == '1':
                global  result
                result[i]=1


if __name__ == '__main__':

    # parser = argparse.ArgumentParser(description="compare two matrix (csv) output difference")
    # parser.add_argument('first', help='matrix A need to compare', type=argparse.FileType('r'))
    # parser.add_argument('second', help='base matrix B', type=argparse.FileType('r'))
    # parser.add_argument('-n', '--no-names', action='store_true', help="instead of printing program point and invariant names, print line numbers, this option can significantly reduce output file size")
    # args = parser.parse_args()
    f1=open("1.csv","r")
    f2 = open("1_6.csv", "r")
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    writer = csv.writer(sys.stdout)
    #sys.exit(1)
    # output header
    #writer.writerow(next(reader1))
    header=next(reader1)
    next(reader2)

    # calculate first data column
    startCol = 2
    j=0
    change_function=["EmailValidator.isValid",
"EmailValidator.isValidDomain",
"EmailValidator.isValidUser",
"EmailValidator.isValidIpAddress",
"EmailValidator.isValidSymbolicDomain",
"Field.isClientValidation",
"Field.setClientValidation",
"Field.getIndexedPropertySize",
"FormSet.merge",
"ISBNValidator.isValid",
"ISBNValidator.Sum",
"ISBNValidator.Clean",
"ISBNValidator.toInt",
"ISBNValidator.isFormatted",
"ISBNValidator.isValidPattern",
"UrlValidator.isValidAuthority",
"UrlValidator.isValidPath",
"UrlValidator.isValidQuery",
"UrlValidator.isValid",
"UrlValidator.isValidScheme",
"ValidatorResult.ResultStatus",
"ValidatorUtils.copyMap"]

    change_function=["CreditCardType.matches",
"field.addMsg",
"field.getMessage",
"field.getMessages",
"field.addArg",
"field.ensureArgsCapacity",
"field.addVar",
"field.getVar",
"field.getVarValue",
"field.getVars",
"field.process",
"field.processVars",
"field.processMessageComponents",
"field.processArg",
"field.runDependentValidators",
"field.validate",
"EmailValidator.isValid",
"EmailValidator.isValidDomain",
"EmailValidator.isValidUser",
"EmailValidator.isValidIpAddress",
"EmailValidator.isValidSymbolicDomain",
"EmailValidator.stripComments",
"Form.getField",
"Form.containsField",
"Form.merge",
"Form.process",
"Form.validate",
"FormSet.Merge",
"FormSet.displayKey",
"GenericTypeValidator.formatByte",
"GenericTypeValidator.formatShort",
"GenericTypeValidator.formatInt",
"GenericTypeValidator.formatLong",
"GenericTypeValidator.formatFloat",
"GenericTypeValidator.formatDouble",
"GenericTypeValidator.formatDate",
"GenericValidator.matchRegexp",
"GenericValidator.isDate",
"ISBNValidator.isValid",
"ISBNValidator.sum",
"ISBNValidator.clean",
"ISBNValidator.toInt",
"ISBNValidator.isFormatted",
"ISBNValidator.isValidPattern",
"UrlValidator.isValid",
"UrlValidator.isValidScheme",
"UrlValidator.isValidAuthority",
"UrlValidator.isValidPath",
"UrlValidator.isValidQuery",
"UrlValidator.isValidFragment",
"Validator.Validate",
"ValidatorAction.executeValidationMethod",
"ValidatorAction.loadValidationClass",
"ValidatorAction.getParameterValues",
"ValidatorAction.isValid",
"ValidatorResources.ValidatorResources",
"ValidatorResources.initDigester",
"ValidatorResources.addFormSet",
"ValidatorResources.addValidatorAction",
"ValidatorResources.getValidatorAction",
"ValidatorResources.getValidatorActions",
"ValidatorResources.getForm",
"ValidatorResources.processForms",
"ValidatorResults.getPropertyNames",
"AbstractNumberValidator.minValue",
"ByteValidator.processParsedValue",
"DoubleValidator.processParsedValue",
"LongValidator.processParsedValue",
"ShortValidator.processParsedValue",
"Flags.isOn",
"Flags.turnOnAll",
"ValidatorUtils.getValueAsString",
"ValidatorUtils.copyFastHashMap",
"ValidatorUtils.copyMap"]
    change_function=["CreditCardValidator.isValid",
"EmailValidator.isValid",
"EmailValidator.isValidDomain",
"EmailValidator.isValidUser",
"EmailValidator.isValidIpAddress",
"EmailValidator.isValidSymbolicDomain",
"EmailValidator.stripComments",
"Field.addMsg",
"Field.getMessage",
"Field.addArg",
"Field.ensureArgsCapacity",
"Field.getArg",
"Field.addVar",
"Field.getVar",
"Field.getVarValue",
"Field.process",
"Field.processVars",
"Field.processMessageComponents",
"Field.processArg",
"Field.getDependencyList",
"Field.clone",
"Field.validateForRule",
"Field.runDependentValidators",
"Field.validate",
"Form.getField",
"Form.addField",
"Form.getFields",
"Form.containsField",
"Form.merge",
"Form.process",
"Form.validate",
"FormSet.Merge",
"FormSet.getForm",
"FormSet.process",
"FormSet.displayKey",
"GenericTypeValidator.formatByte",
"GenericTypeValidator.formatByte",
"GenericTypeValidator.formatShort",
"GenericTypeValidator.formatShort",
"GenericTypeValidator.formatInt",
"GenericTypeValidator.formatLong",
"GenericTypeValidator.formatLong ",
"GenericTypeValidator.formatDate",
"GenericTypeValidator.formatFloat	",
"GenericTypeValidator.formatDouble",
"GenericValidator.matchRegexp",
"GenericValidator.isDate",
"ISBNValidator.isValid",
"ISBNValidator.sum",
"ISBNValidator.clean",
"ISBNValidator.toInt",
"ISBNValidator.isFormatted",
"ISBNValidator.isValidPattern",
"UrlValidator.isValid",
"UrlValidator.isValidScheme",
"UrlValidator.isValidAuthority",
"UrlValidator.isValidPath",
"UrlValidator.isValidQuery",
"UrlValidator.isValidFragment",
"validator.clear",
"validator.validate",
"ValidatorAction.readJavascriptFile",
"ValidatorAction.generateJsFunction",
"ValidatorAction.getDependencyList",
"ValidatorAction.loadValidationClass",
"ValidatorAction.loadParameterClasses",
"ValidatorAction.getParameterValues",
"ValidatorAction.isValid",
"ValidatorAction.getClassLoader",
"ValidatorAction.onlyReturnErrors",
"ValidatorResult.isValid",
"ValidatorResult.getResult",
"ValidatorResult.getActions",
"ValidatorResult.getActionMap",
"ValidatorResults.getValidatorResult",
"ValidatorResults.getPropertyNames",
"ValidatorResults.getResultValueMap",
"Flags.isOn",
"Flags.turnOnAll",
"ValidatorUtils.getValueAsString",
"ValidatorUtils.copyFastHashMap",
"ValidatorUtils.copyMap",
"AbstractCalendarValidator.Compare",
"ByteValidator.processParsedValue",
"CurrencyValidator.Parse",
"DoubleValidator.processParsedValue",
"IntegerValidator.processParsedValue",
"LongValidator.processParsedValue",
"PercentValidator.Parse",
"ShortValidator.processParsedValue"]
    change_db_table=[]
    change_lib=[]

    for line1 in reader1:
        'changed invariants'
        if "junit" not in line1[0]:
            for line2 in reader2:
               if similar(line1[1],line2[1])>0.8:
                   filter(line1, line2, startCol)
                   break
        'changed functions'
        for item in change_function:
            if  item in line1[0]:
                for i in range(startCol, len(line1)):
                    if line1[i] == '0':
                        continue
                    else:
                         result[i] = 1
        'changed library'
        for item in change_lib:
            if item in line1[0]:
                for i in range(startCol, len(line1)):
                    if line1[i] == '0':
                        continue
                    else:
                        result[i] = 1
        'changed database table'
        for item in change_db_table:
            if item in line1[0]:
                for i in range(startCol, len(line1)):
                    if line1[i] == '0':
                        continue
                    else:
                        result[i] = 1
    print result
    for key in result:
             print key
             print header[key]


