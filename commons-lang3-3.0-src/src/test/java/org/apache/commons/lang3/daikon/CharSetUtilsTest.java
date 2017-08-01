package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class CharSetUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.CharSetUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
