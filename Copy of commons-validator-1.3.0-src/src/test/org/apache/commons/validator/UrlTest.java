/*
 * $Id: UrlTest.java 329871 2005-10-31 17:50:55Z niallp $
 * $Rev: 329871 $
 * $Date: 2005-10-31 17:50:55 +0000 (Mon, 31 Oct 2005) $
 *
 * ====================================================================
 * Copyright 2003-2005 The Apache Software Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.validator;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Performs Validation Test for url validations.
 */
public class UrlTest extends TestCase {

   private boolean printStatus = false;
   private boolean printIndex = false;//print index that indicates current scheme,host,port,path, query test were using.

   public UrlTest(String testName) {
      super(testName);
   }

   public static Test suite() {
      return new TestSuite(UrlTest.class);
   }

   protected void setUp() {
      for (int index = 0; index < testPartsIndex.length - 1; index++) {
         testPartsIndex[index] = 0;
      }
   }

   protected void tearDown() {
   }

   public void testIsValid() {
    	testIsValid(testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES);
    	setUp();
    	int options =
    		UrlValidator.ALLOW_2_SLASHES
    			+ UrlValidator.ALLOW_ALL_SCHEMES
    			+ UrlValidator.NO_FRAGMENTS;
    
    	testIsValid(testUrlPartsOptions, options);
   }

   public void testIsValidScheme() {
      if (printStatus) {
         System.out.print("\n testIsValidScheme() ");
      }
      String[] schemes = {"http", "gopher"};
      //UrlValidator urlVal = new UrlValidator(schemes,false,false,false);
      UrlValidator urlVal = new UrlValidator(schemes, 0);
      for (int sIndex = 0; sIndex < testScheme.length; sIndex++) {
         TestPair testPair = testScheme[sIndex];
         boolean result = urlVal.isValidScheme(testPair.item);
         assertEquals(testPair.item, testPair.valid, result);
         if (printStatus) {
            if (result == testPair.valid) {
               System.out.print('.');
            } else {
               System.out.print('X');
            }
         }
      }
      if (printStatus) {
         System.out.println();
      }

   }

   /**
    * Create set of tests by taking the testUrlXXX arrays and
    * running through all possible permutations of their combinations.
    *
    * @param testObjects Used to create a url.
    */
   public void testIsValid(Object[] testObjects, int options) {
      UrlValidator urlVal = new UrlValidator(null, options);
      assertTrue(urlVal.isValid("http://www.google.com"));
      assertTrue(urlVal.isValid("http://www.google.com/"));
      int statusPerLine = 60;
      int printed = 0;
      if (printIndex)  {
         statusPerLine = 6;
      }
      do {
         StringBuffer testBuffer = new StringBuffer();
         boolean expected = true;
         for (int testPartsIndexIndex = 0; testPartsIndexIndex < testPartsIndex.length; ++testPartsIndexIndex) {
            int index = testPartsIndex[testPartsIndexIndex];
            TestPair[] part = (TestPair[]) testObjects[testPartsIndexIndex];
            testBuffer.append(part[index].item);
            expected &= part[index].valid;
         }
         String url = testBuffer.toString();
         boolean result = urlVal.isValid(url);
         assertEquals(url, expected, result);
         if (printStatus) {
            if (printIndex) {
               System.out.print(testPartsIndextoString());
            } else {
               if (result == expected) {
                  System.out.print('.');
               } else {
                  System.out.print('X');
               }
            }
            printed++;
            if (printed == statusPerLine) {
               System.out.println();
               printed = 0;
            }
         }
      } while (incrementTestPartsIndex(testPartsIndex, testObjects));
      if (printStatus) {
         System.out.println();
      }
   }

   static boolean incrementTestPartsIndex(int[] testPartsIndex, Object[] testParts) {
      boolean carry = true;  //add 1 to lowest order part.
      boolean maxIndex = true;
      for (int testPartsIndexIndex = testPartsIndex.length - 1; testPartsIndexIndex >= 0; --testPartsIndexIndex) {
         int index = testPartsIndex[testPartsIndexIndex];
         TestPair[] part = (TestPair[]) testParts[testPartsIndexIndex];
         if (carry) {
            if (index < part.length - 1) {
               index++;
               testPartsIndex[testPartsIndexIndex] = index;
               carry = false;
            } else {
               testPartsIndex[testPartsIndexIndex] = 0;
               carry = true;
            }
         }
         maxIndex &= (index == (part.length - 1));
      }


      return (!maxIndex);
   }

   private String testPartsIndextoString() {
      StringBuffer carryMsg = new StringBuffer("{");
      for (int testPartsIndexIndex = 0; testPartsIndexIndex < testPartsIndex.length; ++testPartsIndexIndex) {
         carryMsg.append(testPartsIndex[testPartsIndexIndex]);
         if (testPartsIndexIndex < testPartsIndex.length - 1) {
            carryMsg.append(',');
         } else {
            carryMsg.append('}');
         }
      }
      return carryMsg.toString();

   }

   public void testValidateUrl() {
      assertTrue(true);
   }

   /**
    * Only used to debug the unit tests.
    * @param argv
    */
   public static void main(String[] argv) {

      UrlTest fct = new UrlTest("url test");
      fct.setUp();
      fct.testIsValid();
      fct.testIsValidScheme();
   }
   //-------------------- Test data for creating a composite URL
   /**
    * The data given below approximates the 4 parts of a URL
    * <scheme>://<authority><path>?<query> except that the port number
    * is broken out of authority to increase the number of permutations.
    * A complete URL is composed of a scheme+authority+port+path+query,
    * all of which must be individually valid for the entire URL to be considered
    * valid.
    */
   TestPair[] testUrlScheme = {new TestPair("http://", true),
                               new TestPair("ftp://", true),
                               new TestPair("h3t://", true),
                               new TestPair("3ht://", false),
                               new TestPair("http:/", false),
                               new TestPair("http:", false),
                               new TestPair("http/", false),
                               new TestPair("://", false),
                               new TestPair("", true)};

   TestPair[] testUrlAuthority = {new TestPair("www.google.com", true),
                                  new TestPair("go.com", true),
                                  new TestPair("go.au", true),
                                  new TestPair("0.0.0.0", true),
                                  new TestPair("255.255.255.255", true),
                                  new TestPair("256.256.256.256", false),
                                  new TestPair("255.com", true),
                                  new TestPair("1.2.3.4.5", false),
                                  new TestPair("1.2.3.4.", false),
                                  new TestPair("1.2.3", false),
                                  new TestPair(".1.2.3.4", false),
                                  new TestPair("go.a", false),
                                  new TestPair("go.a1a", true),
                                  new TestPair("go.1aa", false),
                                  new TestPair("aaa.", false),
                                  new TestPair(".aaa", false),
                                  new TestPair("aaa", false),
                                  new TestPair("", false)
   };
   TestPair[] testUrlPort = {new TestPair(":80", true),
                             new TestPair(":65535", true),
                             new TestPair(":0", true),
                             new TestPair("", true),
                             new TestPair(":-1", false),
                             new TestPair(":65636", true),
                             new TestPair(":65a", false)
   };
   TestPair[] testPath = {new TestPair("/test1", true),
                          new TestPair("/t123", true),
                          new TestPair("/$23", true),
                          new TestPair("/..", false),
                          new TestPair("/../", false),
                          new TestPair("/test1/", true),
                          new TestPair("", true),
                          new TestPair("/test1/file", true),
                          new TestPair("/..//file", false),
                          new TestPair("/test1//file", false)
   };
   //Test allow2slash, noFragment
   TestPair[] testUrlPathOptions = {new TestPair("/test1", true),
                                    new TestPair("/t123", true),
                                    new TestPair("/$23", true),
                                    new TestPair("/..", false),
                                    new TestPair("/../", false),
                                    new TestPair("/test1/", true),
                                    new TestPair("/#", false),
                                    new TestPair("", true),
                                    new TestPair("/test1/file", true),
                                    new TestPair("/t123/file", true),
                                    new TestPair("/$23/file", true),
                                    new TestPair("/../file", false),
                                    new TestPair("/..//file", false),
                                    new TestPair("/test1//file", true),
                                    new TestPair("/#/file", false)
   };

   TestPair[] testUrlQuery = {new TestPair("?action=view", true),
                              new TestPair("?action=edit&mode=up", true),
                              new TestPair("", true)
   };

   Object[] testUrlParts = {testUrlScheme, testUrlAuthority, testUrlPort, testPath, testUrlQuery};
   Object[] testUrlPartsOptions = {testUrlScheme, testUrlAuthority, testUrlPort, testUrlPathOptions, testUrlQuery};
   int[] testPartsIndex = {0, 0, 0, 0, 0};

   //---------------- Test data for individual url parts ----------------
   TestPair[] testScheme = {new TestPair("http", true),
                            new TestPair("ftp", false),
                            new TestPair("httpd", false),
                            new TestPair("telnet", false)};


}