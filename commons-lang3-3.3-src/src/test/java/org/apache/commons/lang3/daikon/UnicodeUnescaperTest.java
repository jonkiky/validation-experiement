package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class UnicodeUnescaperTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.translate.UnicodeUnescaperTest.class);
junit.textui.TestRunner.run(suite);
}
}
