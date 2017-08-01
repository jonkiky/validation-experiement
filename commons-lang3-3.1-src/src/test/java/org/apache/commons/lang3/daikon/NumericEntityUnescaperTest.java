package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class NumericEntityUnescaperTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest.class);
junit.textui.TestRunner.run(suite);
}
}
