package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class MutableLongTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.mutable.MutableLongTest.class);
junit.textui.TestRunner.run(suite);
}
}
