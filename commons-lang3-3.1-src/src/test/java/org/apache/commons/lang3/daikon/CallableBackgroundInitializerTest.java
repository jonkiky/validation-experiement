package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class CallableBackgroundInitializerTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.concurrent.CallableBackgroundInitializerTest.class);
junit.textui.TestRunner.run(suite);
}
}
