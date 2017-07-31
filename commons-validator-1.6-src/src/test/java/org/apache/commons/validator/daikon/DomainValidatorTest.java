package org.apache.commons.validator.daikon;
import junit.framework.TestSuite;
public class DomainValidatorTest {
public static void main(String arg[]){
TestSuite suite = new TestSuite();
suite.addTestSuite(org.apache.commons.validator.routines.DomainValidatorTest.class);
junit.textui.TestRunner.run(suite);
}
}
