/*
 * $Id: ValueBean.java 155434 2005-02-26 13:16:41Z dirkv $
 * $Rev: 155434 $
 * $Date: 2005-02-26 13:16:41 +0000 (Sat, 26 Feb 2005) $
 *
 * ====================================================================
 * Copyright 2000-2005 The Apache Software Foundation
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

/**                                                       
 * Value object for storing a value to run tests on. 
 */                                                       
public class ValueBean {
   
   protected String value = null;
   
   /**
    * Gets the value.
    */
   public String getValue() {
      return value;	
   }

   /**
    * Sets the value.
    */
   public void setValue(String value) {
      this.value = value;	
   }
      
}                                                         