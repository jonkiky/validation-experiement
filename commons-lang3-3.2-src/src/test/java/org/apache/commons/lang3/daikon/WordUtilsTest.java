package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class WordUtilsTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.WordUtilsTest.class);
junit.textui.TestRunner.run(suite);
}
}
