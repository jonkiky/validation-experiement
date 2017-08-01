package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class EventListenerSupportTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.event.EventListenerSupportTest.class);
junit.textui.TestRunner.run(suite);
}
}
