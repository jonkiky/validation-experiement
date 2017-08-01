package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class DateFormatUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.time.DateFormatUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
