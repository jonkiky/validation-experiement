package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class ISBNValidatorTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.ISBNValidatorTest.class);
junit.textui.TestRunner.run(suite);
}
}