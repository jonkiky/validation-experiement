package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class ConstructorUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.reflect.ConstructorUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
