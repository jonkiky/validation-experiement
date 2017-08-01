package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class DefaultToStringStyleTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.builder.DefaultToStringStyleTest.class);
junit.textui.TestRunner.run(suite);
}
}
