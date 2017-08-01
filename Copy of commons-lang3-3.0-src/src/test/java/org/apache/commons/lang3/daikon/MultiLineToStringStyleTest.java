package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class MultiLineToStringStyleTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.builder.MultiLineToStringStyleTest.class);
junit.textui.TestRunner.run(suite);
}
}
