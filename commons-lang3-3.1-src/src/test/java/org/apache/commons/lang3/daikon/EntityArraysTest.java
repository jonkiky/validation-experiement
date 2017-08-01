package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class EntityArraysTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.text.translate.EntityArraysTest.class);
junit.textui.TestRunner.run(suite);
}
}
