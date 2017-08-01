package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class CharRangeTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.CharRangeTest.class);
junit.textui.TestRunner.run(suite);
}
}
