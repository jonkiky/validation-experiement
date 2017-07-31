package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class LocaleTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.LocaleTest.class);
junit.textui.TestRunner.run(suite);
}
}
