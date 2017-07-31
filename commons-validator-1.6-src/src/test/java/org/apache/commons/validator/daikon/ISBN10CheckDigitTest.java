package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class ISBN10CheckDigitTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.checkdigit.ISBN10CheckDigitTest.class);
junit.textui.TestRunner.run(suite);
}
}
