package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class AbstractCalendarValidatorTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.AbstractCalendarValidatorTest.class);
junit.textui.TestRunner.run(suite);
}
}
