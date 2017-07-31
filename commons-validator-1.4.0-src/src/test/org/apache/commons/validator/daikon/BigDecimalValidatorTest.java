package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class BigDecimalValidatorTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.BigDecimalValidatorTest.class);
junit.textui.TestRunner.run(suite);
}
}
