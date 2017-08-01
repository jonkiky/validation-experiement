package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class DefaultExceptionContextTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.exception.DefaultExceptionContextTest.class);
junit.textui.TestRunner.run(suite);
}
}
