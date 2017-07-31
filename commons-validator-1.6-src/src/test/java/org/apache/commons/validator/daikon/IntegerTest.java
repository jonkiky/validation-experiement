package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class IntegerTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.IntegerTest.class);
junit.textui.TestRunner.run(suite);
}
}
