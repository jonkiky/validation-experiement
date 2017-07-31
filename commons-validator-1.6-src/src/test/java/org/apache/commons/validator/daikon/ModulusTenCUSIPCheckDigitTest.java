package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class ModulusTenCUSIPCheckDigitTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.checkdigit.ModulusTenCUSIPCheckDigitTest.class);
junit.textui.TestRunner.run(suite);
}
}
