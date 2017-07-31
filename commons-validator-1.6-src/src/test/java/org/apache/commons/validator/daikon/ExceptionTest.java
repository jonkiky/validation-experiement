package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class ExceptionTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.ExceptionTest.class);
junit.textui.TestRunner.run(suite);
}
}
