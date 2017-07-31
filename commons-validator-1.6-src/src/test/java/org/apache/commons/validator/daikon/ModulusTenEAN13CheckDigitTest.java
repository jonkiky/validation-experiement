package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class ModulusTenEAN13CheckDigitTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.checkdigit.ModulusTenEAN13CheckDigitTest.class);
junit.textui.TestRunner.run(suite);
}
}
