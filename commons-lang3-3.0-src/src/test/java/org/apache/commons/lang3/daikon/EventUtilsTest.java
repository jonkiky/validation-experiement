package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class EventUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.event.EventUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
