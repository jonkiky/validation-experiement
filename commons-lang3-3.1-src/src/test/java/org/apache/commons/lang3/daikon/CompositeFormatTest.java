package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class CompositeFormatTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.CompositeFormatTest.class);
junit.textui.TestRunner.run(suite);
}
}
