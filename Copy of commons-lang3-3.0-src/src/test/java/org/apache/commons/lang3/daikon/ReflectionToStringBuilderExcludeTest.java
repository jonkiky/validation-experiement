package org.apache.commons.lang3.daikon;
import junit.framework.TestSuite;
public class ReflectionToStringBuilderExcludeTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.lang3.builder.ReflectionToStringBuilderExcludeTest.class);
junit.textui.TestRunner.run(suite);
}
}
