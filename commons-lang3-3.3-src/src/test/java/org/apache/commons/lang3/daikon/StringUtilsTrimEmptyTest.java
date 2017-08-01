package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class StringUtilsTrimEmptyTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.StringUtilsTrimEmptyTest.class);
junit.textui.TestRunner.run(suite);
}
}
