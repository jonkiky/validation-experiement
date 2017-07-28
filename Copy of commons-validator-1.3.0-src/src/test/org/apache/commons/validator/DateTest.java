/*
 * $Id: DateTest.java 155434 2005-02-26 13:16:41Z dirkv $
 * $Rev: 155434 $
 * $Date: 2005-02-26 05:16:41 -0800 (Sat, 26 Feb 2005) $
 *
 * ====================================================================
 * Copyright 2001-2005 The Apache Software Foundation
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

import java.io.IOException;
import java.util.*;

import junit.framework.Test;
import junit.framework.TestSuite;

import org.xml.sax.SAXException;

/**
 * Abstracts date unit tests methods.
 */
public class DateTest extends TestCommon {
    
    /**
     * The key used to retrieve the set of validation
     * rules from the xml file.
     */
    protected String FORM_KEY = "dateForm";
    
    /**
     * The key used to retrieve the validator action.
     */
    protected String ACTION = "date";


    public DateTest(String name) {
        super(name);
    }
    
    /**
     * Start the tests.
     *
     * @param theArgs the arguments. Not used
     */
    public static void main(String[] theArgs) {
        junit.awtui.TestRunner.main(new String[]{DateTest.class.getName()});
    }

    /**
     * Load <code>ValidatorResources</code> from 
     * validator-numeric.xml.
     */
    protected void setUp() throws IOException, SAXException {
        // Load resources
        loadResources("DateTest-config.xml");
    }

    protected void tearDown() {
    }
    
    /**
     * @return a test suite (<code>TestSuite</code>) that includes all methods
     *         starting with "test"
     */
    public static Test suite() {
        // All methods starting with "test" will be executed in the test suite.
        return new TestSuite(DateTest.class);
    }

    /**
     * Tests the date validation.
     */
    public void testValidDate() throws ValidatorException {
        // Create bean to run test on.
        ValueBean info = new ValueBean();
        info.setValue("12/01/2005");
        valueTest(info, true);
    }

    /**
     * Tests the date validation.
     */
    public void testInvalidDate() throws ValidatorException {
        // Create bean to run test on.
        ValueBean info = new ValueBean();
        info.setValue("12/01as/2005");
        valueTest(info, false);
    }

    
    /**
     * Utlity class to run a test on a value.
     *
     * @param	info	Value to run test on.
     * @param	passed	Whether or not the test is expected to pass.
     */
    protected void valueTest(Object info, boolean passed) throws ValidatorException {
        // Construct validator based on the loaded resources
        // and the form key
        Validator validator = new Validator(resources, FORM_KEY);
        // add the name bean to the validator as a resource
        // for the validations to be performed on.
        validator.setParameter(Validator.BEAN_PARAM, info);
        validator.setParameter(Validator.LOCALE_PARAM, Locale.US);

        // Get results of the validation.
        ValidatorResults results = null;

        // throws ValidatorException,
        // but we aren't catching for testing
        // since no validation methods we use
        // throw this
        results = validator.validate();

        assertNotNull("Results are null.", results);

        ValidatorResult result = results.getValidatorResult("value");

        assertNotNull(ACTION + " value ValidatorResult should not be null.", result);
        assertTrue(ACTION + " value ValidatorResult should contain the '" + ACTION + "' action.", result.containsAction(ACTION));
        assertTrue(ACTION + " value ValidatorResult for the '" + ACTION + "' action should have " + (passed ? "passed" : "failed") + ".", (passed ? result.isValid(ACTION) : !result.isValid(ACTION)));
    }


}
