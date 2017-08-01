package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class CharEncodingTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.CharEncodingTest.class);
junit.textui.TestRunner.run(suite);
}
}
