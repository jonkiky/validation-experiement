package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class BackgroundInitializerTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.concurrent.BackgroundInitializerTest.class);
junit.textui.TestRunner.run(suite);
}
}
