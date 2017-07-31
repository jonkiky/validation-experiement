/*
 * $Id: RetrieveFormTest.java 329836 2005-10-31 15:12:50Z niallp $
 * $Rev: 329836 $
 * $Date: 2005-10-31 15:12:50 +0000 (Mon, 31 Oct 2005) $
 *
 * ====================================================================
 * Copyright 2005 The Apache Software Foundation
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
import java.io.InputStream;
import java.util.Locale;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.xml.sax.SAXException;

/**
 * Tests retrieving forms using different Locales.
 */
public class RetrieveFormTest extends TestCase {

    /**
     * Resources used for validation tests.
     */
    private ValidatorResources resources = null;
    
    /**
     * Prefix for the forms.
     */
    private static final String FORM_PREFIX = "testForm_";
    
    /**
     * Prefix for the forms.
     */
    private static final Locale CANADA_FRENCH_XXX = new Locale("fr", "CA", "XXX");

   /**
    * @return a test suite (<code>TestSuite</code>) that includes all methods
    *         starting with "test"
    */
   public static Test suite() {
       // All methods starting with "test" will be executed in the test suite.
       return new TestSuite(RetrieveFormTest.class);
   }

    /**
     * Constructor for FormTest.
     * @param name
     */
    public RetrieveFormTest(String name) {
        super(name);
    }

    /** 
     * Load <code>ValidatorResources</code> from multiple xml files.
     */
    protected void setUp() throws IOException, SAXException {
        InputStream[] streams =
            new InputStream[] {
                this.getClass().getResourceAsStream(
                    "RetrieveFormTest-config.xml")};

        this.resources = new ValidatorResources(streams);

        for (int i = 0; i < streams.length; i++) {
            streams[i].close();
        }
    }

   /**
    * Test a form defined only in the "default" formset.
    */
    public void testDefaultForm() throws ValidatorException {

        String formKey = FORM_PREFIX + "default";

        // *** US locale ***
        checkForm(Locale.US, formKey, "default");

        // *** French locale ***
        checkForm(Locale.FRENCH, formKey, "default");

        // *** France locale ***
        checkForm(Locale.FRANCE, formKey, "default");

        // *** Candian (English) locale ***
        checkForm(Locale.CANADA, formKey, "default");

        // *** Candian French locale ***
        checkForm(Locale.CANADA_FRENCH, formKey, "default");

        // *** Candian French Variant locale ***
        checkForm(CANADA_FRENCH_XXX, formKey, "default");

    }

   /**
    * Test a form defined in the "default" formset and formsets
    * where just the "language" is specified.
    */
    public void testLanguageForm() throws ValidatorException {

        String formKey = FORM_PREFIX + "language";

        // *** US locale ***
        checkForm(Locale.US, formKey, "default");

        // *** French locale ***
        checkForm(Locale.FRENCH, formKey, "fr");

        // *** France locale ***
        checkForm(Locale.FRANCE, formKey, "fr");

        // *** Candian (English) locale ***
        checkForm(Locale.CANADA, formKey, "default");

        // *** Candian French locale ***
        checkForm(Locale.CANADA_FRENCH, formKey, "fr");

        // *** Candian French Variant locale ***
        checkForm(CANADA_FRENCH_XXX, formKey, "fr");

    }

   /**
    * Test a form defined in the "default" formset, formsets
    * where just the "language" is specified and formset where
    * the language and country are specified.
    */
    public void testLanguageCountryForm() throws ValidatorException {

        String formKey = FORM_PREFIX + "language_country";

        // *** US locale ***
        checkForm(Locale.US, formKey, "default");

        // *** French locale ***
        checkForm(Locale.FRENCH, formKey, "fr");

        // *** France locale ***
        checkForm(Locale.FRANCE, formKey, "fr_FR");

        // *** Candian (English) locale ***
        checkForm(Locale.CANADA, formKey, "default");

        // *** Candian French locale ***
        checkForm(Locale.CANADA_FRENCH, formKey, "fr_CA");

        // *** Candian French Variant locale ***
        checkForm(CANADA_FRENCH_XXX, formKey, "fr_CA");

    }

   /**
    * Test a form defined in all the formsets
    */
    public void testLanguageCountryVariantForm() throws ValidatorException {

        String formKey = FORM_PREFIX + "language_country_variant";

        // *** US locale ***
        checkForm(Locale.US, formKey, "default");

        // *** French locale ***
        checkForm(Locale.FRENCH, formKey, "fr");

        // *** France locale ***
        checkForm(Locale.FRANCE, formKey, "fr_FR");

        // *** Candian (English) locale ***
        checkForm(Locale.CANADA, formKey, "default");

        // *** Candian French locale ***
        checkForm(Locale.CANADA_FRENCH, formKey, "fr_CA");

        // *** Candian French Variant locale ***
        checkForm(CANADA_FRENCH_XXX, formKey, "fr_CA_XXX");

    }

   /**
    * Test a form not defined
    */
    public void testFormNotFound() throws ValidatorException {

        String formKey = "INVALID_NAME";

        // *** US locale ***
        checkFormNotFound(Locale.US, formKey);

        // *** French locale ***
        checkFormNotFound(Locale.FRENCH, formKey);

        // *** France locale ***
        checkFormNotFound(Locale.FRANCE, formKey);

        // *** Candian (English) locale ***
        checkFormNotFound(Locale.CANADA, formKey);

        // *** Candian French locale ***
        checkFormNotFound(Locale.CANADA_FRENCH, formKey);

        // *** Candian French Variant locale ***
        checkFormNotFound(CANADA_FRENCH_XXX, formKey);


    }

    private void checkForm(Locale locale, String formKey, String expectedVarValue) {

        // Retrieve the Form
        Form testForm = resources.getForm(locale, formKey);
        assertNotNull("Form '" +formKey+"' null for locale " + locale, testForm);

        // Validate the expected Form is retrieved by checking the "localeVar"
        // value of the field.
        Field testField = (Field)testForm.getField("testProperty");
        assertEquals("Incorrect Form '"   + formKey  + "' for locale '" + locale + "'",
                     expectedVarValue, 
                     testField.getVarValue("localeVar"));
    }

    private void checkFormNotFound(Locale locale, String formKey) {

        // Retrieve the Form
        Form testForm = resources.getForm(locale, formKey);
        assertNull("Form '" +formKey+"' not null for locale " + locale, testForm);

    }

}
