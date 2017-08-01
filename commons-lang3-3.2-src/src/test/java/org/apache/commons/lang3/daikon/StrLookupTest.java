package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class StrLookupTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.StrLookupTest.class);
junit.textui.TestRunner.run(suite);
}
}
