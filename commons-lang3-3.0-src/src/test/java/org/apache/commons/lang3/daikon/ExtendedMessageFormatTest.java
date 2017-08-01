package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class ExtendedMessageFormatTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.ExtendedMessageFormatTest.class);
junit.textui.TestRunner.run(suite);
}
}
