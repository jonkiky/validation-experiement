package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class FlagsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.util.FlagsTest.class);
junit.textui.TestRunner.run(suite);
}
}