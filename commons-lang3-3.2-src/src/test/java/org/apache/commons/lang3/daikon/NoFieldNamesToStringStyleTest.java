package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class NoFieldNamesToStringStyleTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.builder.NoFieldNamesToStringStyleTest.class);
junit.textui.TestRunner.run(suite);
}
}
