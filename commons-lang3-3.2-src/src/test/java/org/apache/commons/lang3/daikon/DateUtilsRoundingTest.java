package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class DateUtilsRoundingTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.time.DateUtilsRoundingTest.class);
junit.textui.TestRunner.run(suite);
}
}