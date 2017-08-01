package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class NumberUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.math.NumberUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
