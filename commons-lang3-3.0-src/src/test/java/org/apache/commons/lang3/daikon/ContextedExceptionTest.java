package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class ContextedExceptionTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.exception.ContextedExceptionTest.class);
junit.textui.TestRunner.run(suite);
}
}
