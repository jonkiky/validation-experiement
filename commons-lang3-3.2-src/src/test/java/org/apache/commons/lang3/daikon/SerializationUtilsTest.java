package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class SerializationUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.SerializationUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
