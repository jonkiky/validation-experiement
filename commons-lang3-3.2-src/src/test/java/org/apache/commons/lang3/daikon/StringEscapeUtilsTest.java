package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class StringEscapeUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.StringEscapeUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
