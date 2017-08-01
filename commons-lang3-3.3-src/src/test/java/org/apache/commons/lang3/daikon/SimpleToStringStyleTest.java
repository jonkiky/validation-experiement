package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class SimpleToStringStyleTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.builder.SimpleToStringStyleTest.class);
junit.textui.TestRunner.run(suite);
}
}
