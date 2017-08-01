package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class DurationFormatUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.time.DurationFormatUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
