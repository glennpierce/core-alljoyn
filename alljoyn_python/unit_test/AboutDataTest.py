#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Glenn Pierce. All rights reserved.
# 
#    Permission to use, copy, modify, and/or distribute this software for any
#    purpose with or without fee is hereby granted, provided that the above
#    copyright notice and this permission notice appear in all copies.
# 
#    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.



# TEST(AboutDataTest, SetDeviceId) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setdeviceid(aboutData,
#                                            "avec-awe1213-1234559xvc123");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* deviceId;
#     status = alljoyn_aboutdata_getdeviceid(aboutData, &deviceId);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("avec-awe1213-1234559xvc123", deviceId);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetAppName) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* appName;
#     status = alljoyn_aboutdata_getappname(aboutData, &appName, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("Application", appName);

#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_getappname(aboutData, &appName, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("aplicacion", appName);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetManufacturer) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* manufacturer;
#     status = alljoyn_aboutdata_getmanufacturer(aboutData, &manufacturer, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("Manufacturer", manufacturer);

#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_getmanufacturer(aboutData, &manufacturer, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("manufactura", manufacturer);

#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetModelNumber) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "xBnc345");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* modelNumber;
#     status = alljoyn_aboutdata_getmodelnumber(aboutData, &modelNumber);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("xBnc345", modelNumber);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetSupportedLanguage) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     size_t numLanguages =
#         alljoyn_aboutdata_getsupportedlanguages(aboutData, NULL, 0);
#     const char** languages = new const char*[numLanguages];

#     size_t numRetLang =
#         alljoyn_aboutdata_getsupportedlanguages(aboutData,
#                                                 languages,
#                                                 numLanguages);
#     EXPECT_EQ(numLanguages, numRetLang);
#     EXPECT_EQ(1u, numLanguages);
#     EXPECT_STREQ("en", languages[0]);

#     delete [] languages;
#     languages = NULL;

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     numLanguages = alljoyn_aboutdata_getsupportedlanguages(aboutData, NULL, 0);
#     languages = new const char*[numLanguages];

#     numRetLang =
#         alljoyn_aboutdata_getsupportedlanguages(aboutData,
#                                                 languages,
#                                                 numLanguages);
#     EXPECT_EQ(numLanguages, numRetLang);
#     EXPECT_EQ(2u, numLanguages);
#     EXPECT_STREQ("en", languages[0]);
#     EXPECT_STREQ("es", languages[1]);
#     delete [] languages;
#     languages = NULL;
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetSupportedLanguage_Duplicate) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     /* Duplicate language already added from constructor */
#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     /* Duplicate language already added, error status should be generated */
#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     /*
#      * Even though "en" and "es" languages have been added multiple times only
#      * two languages should be reported in the list of SupportedLanguages.
#      */
#     size_t numRetLang = alljoyn_aboutdata_getsupportedlanguages(aboutData, NULL, 0);
#     EXPECT_EQ(2u, numRetLang);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, DISABLED_SetSupportedLanguage_Invalid_Tag) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     /* Invalid language tag not defined in RFC5646 */
#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "abc");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "232");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     /* Invalid subtag not defined in RFC5646 */
#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "en-t324");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "zh-gfjk");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     size_t numRetLang =
#         alljoyn_aboutdata_getsupportedlanguages(aboutData, NULL, 0);
#     EXPECT_EQ(1u, numRetLang);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, GetSupportedLanguages) {
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     size_t numLanguages;
#     numLanguages =
#         alljoyn_aboutdata_getsupportedlanguages(aboutData, NULL, 0);
#     EXPECT_EQ(1u, numLanguages);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetDescription) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* description;
#     status = alljoyn_aboutdata_getdescription(aboutData, &description, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("A poetic description of this application", description);

#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_getdescription(aboutData, &description, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("Una descripcion poetica de esta aplicacion", description);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetDateOfManufacture) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setdateofmanufacture(aboutData, "2014-01-20");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* dateOfManufacture;
#     status = alljoyn_aboutdata_getdateofmanufacture(aboutData, &dateOfManufacture);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("2014-01-20", dateOfManufacture);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, DISABLED_SetDateOfManufacture_Negative) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     /* Invalid date should fail */
#     status = alljoyn_aboutdata_setdateofmanufacture(aboutData, "2014-41-20");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setdateofmanufacture(aboutData, "201a-02-20");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setdateofmanufacture(aboutData, "2013-02-29");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setdateofmanufacture(aboutData, "04/31/2014");
#     EXPECT_NE(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetSoftwareVersion) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* softwareVersion;
#     status = alljoyn_aboutdata_getsoftwareversion(aboutData, &softwareVersion);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("0.1.2", softwareVersion);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetHardwareVersion) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_sethardwareversion(aboutData, "3.2.1");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* hardwareVersion;
#     status = alljoyn_aboutdata_gethardwareversion(aboutData, &hardwareVersion);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("3.2.1", hardwareVersion);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetSupportUrl) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_setsupporturl(aboutData, "www.example.com");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* supportUrl;
#     status = alljoyn_aboutdata_getsupporturl(aboutData, &supportUrl);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("www.example.com", supportUrl);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, IsValid) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));
#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, IsValid_Negative) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     /* DefaultLanguage and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* DeviceId and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* AppName and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* Manufacturer and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* ModelNumber and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /*Description and other required fields are missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* SoftwareVersion missing */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     /* Now all required fields are set for English */
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* Missing AppName/Manufacture/Description */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#      Missing Manufacture/Description
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     /* Missing Description */
#     EXPECT_FALSE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, GetAboutData) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     alljoyn_msgarg aboutArg = alljoyn_msgarg_create();
#     status = alljoyn_aboutdata_getaboutdata(aboutData, aboutArg, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     alljoyn_msgarg args;

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::APP_ID, &args);
#     int8_t* appIdOut;
#     size_t appIdNum;
#     alljoyn_msgarg_get(args, "ay", &appIdNum, &appIdOut);
#     ASSERT_EQ(16u, appIdNum);
#     for (size_t i = 0; i < appIdNum; ++i) {
#         EXPECT_EQ(appId[i], appIdOut[i]);
#     }

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::DEFAULT_LANGUAGE, &args);
#     char* defaultLanguage;
#     alljoyn_msgarg_get(args, "s", &defaultLanguage);
#     EXPECT_STREQ("en", defaultLanguage);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::DEVICE_ID, &args);
#     char* deviceId;
#     alljoyn_msgarg_get(args, "s", &deviceId);
#     EXPECT_STREQ("fakeID", deviceId);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::APP_NAME, &args);
#     char* appName;
#     alljoyn_msgarg_get(args, "s", &appName);
#     EXPECT_STREQ("Application", appName);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::MANUFACTURER, &args);
#     char* manufacturer;
#     alljoyn_msgarg_get(args, "s", &manufacturer);
#     EXPECT_STREQ("Manufacturer", manufacturer);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::MODEL_NUMBER, &args);
#     char* modelNumber;
#     alljoyn_msgarg_get(args, "s", &modelNumber);
#     EXPECT_STREQ("123456", modelNumber);

#     alljoyn_msgarg_destroy(aboutArg);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, GetMsgArg_es_language) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     alljoyn_msgarg aboutArg = alljoyn_msgarg_create();
#     alljoyn_msgarg args;
#     status = alljoyn_aboutdata_getaboutdata(aboutData, aboutArg, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::APP_ID, &args);
#     int8_t* appIdOut;
#     size_t appIdNum;
#     alljoyn_msgarg_get(args, "ay", &appIdNum, &appIdOut);
#     ASSERT_EQ(16u, appIdNum);
#     for (size_t i = 0; i < appIdNum; ++i) {
#         EXPECT_EQ(appId[i], appIdOut[i]);
#     }

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::DEFAULT_LANGUAGE, &args);
#     char* defaultLanguage;
#     alljoyn_msgarg_get(args, "s", &defaultLanguage);
#     EXPECT_STREQ("en", defaultLanguage);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::DEVICE_ID, &args);
#     char* deviceId;
#     alljoyn_msgarg_get(args, "s", &deviceId);
#     EXPECT_STREQ("fakeID", deviceId);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::APP_NAME, &args);
#     char* appName;
#     alljoyn_msgarg_get(args, "s", &appName);
#     EXPECT_STREQ("aplicacion", appName);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::MANUFACTURER, &args);
#     char* manufacturer;
#     alljoyn_msgarg_get(args, "s", &manufacturer);
#     EXPECT_STREQ("manufactura", manufacturer);

#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                   AboutData::MODEL_NUMBER, &args);
#     char* modelNumber;
#     alljoyn_msgarg_get(args, "s", &modelNumber);
#     EXPECT_STREQ("123456", modelNumber);
#     alljoyn_msgarg_destroy(aboutArg);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# void VerifyAppName(alljoyn_aboutdata aboutData, const char* language, const char* expectedAppName)
# {
#     alljoyn_msgarg aboutArg = alljoyn_msgarg_create();
#     QStatus status = alljoyn_aboutdata_getaboutdata(aboutData, aboutArg, language);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg args;
#     alljoyn_msgarg_getdictelement(aboutArg, "{sv}", AboutData::APP_NAME, &args);
#     char* appName;
#     alljoyn_msgarg_get(args, "s", &appName);
#     EXPECT_STREQ(expectedAppName, appName);

#     alljoyn_msgarg_destroy(aboutArg);
# }

# TEST(AboutDataTest, GetMsgArg_best_language) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setappname(aboutData, "en appName", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "en manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData, "en description", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "de-CH");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "de-CH appName", "de-CH");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "de-CH manufacturer", "de-CH");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData, "de-CH description", "de-CH");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "de-CH"));

#     // Test requesting languages that resolve to the language that happens
#     // to be the default language.
#     VerifyAppName(aboutData, "EN", "en appName");
#     VerifyAppName(aboutData, "EN-US", "en appName");
#     VerifyAppName(aboutData, "en-a-bbb-x-a-ccc", "en appName");

#     // Test requesting languages that resolve to a language other than
#     // the default language.
#     VerifyAppName(aboutData, "DE-CH", "de-CH appName");
#     VerifyAppName(aboutData, "de-ch-1901", "de-CH appName");

#     // Test requesting languages that resolve to nothing and so use the
#     // default language.
#     VerifyAppName(aboutData, "de", "en appName");
#     VerifyAppName(aboutData, "fr", "en appName");

#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, InitUsingMsgArgBadSignature) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     alljoyn_msgarg notADictionary =
#         alljoyn_msgarg_create_and_set("s", "incorrect type.");

#     status = alljoyn_aboutdata_createfrommsgarg(aboutData, notADictionary, "en");
#     EXPECT_EQ(ER_BUS_SIGNATURE_MISMATCH, status) << "  Actual Status: "
#                                                  << QCC_StatusText(status);

#     alljoyn_msgarg_destroy(notADictionary);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, UTF8_test) {
#     char str[] = "привет";
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     status = alljoyn_aboutdata_setappname(aboutData, str, "ru");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char* esOut;
#     status = alljoyn_aboutdata_getappname(aboutData, &esOut, "ru");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ(str, esOut);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, GetAnnouncedAboutData) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     alljoyn_msgarg announceArg = alljoyn_msgarg_create();
#     status = alljoyn_aboutdata_getannouncedaboutdata(aboutData, announceArg);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg args;
#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::APP_ID, &args);
#     int8_t* appIdOut;
#     size_t appIdNum;
#     alljoyn_msgarg_get(args, "ay", &appIdNum, &appIdOut);
#     ASSERT_EQ(16u, appIdNum);
#     for (size_t i = 0; i < appIdNum; ++i) {
#         EXPECT_EQ(appId[i], appIdOut[i]);
#     }

#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::DEFAULT_LANGUAGE, &args);
#     char* defaultLanguage;
#     alljoyn_msgarg_get(args, "s", &defaultLanguage);
#     EXPECT_STREQ("en", defaultLanguage);

#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::DEVICE_ID, &args);
#     char* deviceId;
#     alljoyn_msgarg_get(args, "s", &deviceId);
#     EXPECT_STREQ("fakeID", deviceId);

#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::APP_NAME, &args);
#     char* appName;
#     alljoyn_msgarg_get(args, "s", &appName);
#     EXPECT_STREQ("Application", appName);

#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::MANUFACTURER, &args);
#     char* manufacturer;
#     alljoyn_msgarg_get(args, "s", &manufacturer);
#     EXPECT_STREQ("Manufacturer", manufacturer);

#     status = alljoyn_msgarg_getdictelement(announceArg, "{sv}",
#                                            AboutData::MODEL_NUMBER, &args);
#     char* modelNumber;
#     alljoyn_msgarg_get(args, "s", &modelNumber);
#     EXPECT_STREQ("123456", modelNumber);

#     alljoyn_msgarg_destroy(announceArg);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, SetOEMSpecificField) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");
#     alljoyn_msgarg arg = alljoyn_msgarg_create();

#     status = alljoyn_msgarg_set(arg, "s", "888-555-1234");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_msgarg_set(arg, "s", "800-555-4321");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg value;
#     status = alljoyn_aboutdata_getfield(aboutData, "SupportNumber", &value, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char buf[2];
#     alljoyn_msgarg_signature(value, buf, 2);
#     EXPECT_STREQ("s", buf);
#     const char* supportNumber;
#     status = alljoyn_msgarg_get(value, "s", &supportNumber);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("888-555-1234", supportNumber);

#     status = alljoyn_aboutdata_getfield(aboutData, "SupportNumber", &value, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg_signature(value, buf, 2);
#     EXPECT_STREQ("s", buf);
#     status = alljoyn_msgarg_get(value, "s", &supportNumber);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("800-555-4321", supportNumber);

#     alljoyn_msgarg_destroy(arg);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, GetMsgArgWithOEMSpecificField) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t appId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, appId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     alljoyn_msgarg arg = alljoyn_msgarg_create();
#     status = alljoyn_msgarg_set(arg, "s", "888-555-1234");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_msgarg_set(arg, "s", "800-555-4321");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg aboutArg = alljoyn_msgarg_create();
#     status = alljoyn_aboutdata_getaboutdata(aboutData, aboutArg, "en");

#     alljoyn_msgarg args;
#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::APP_ID, &args);
#     int8_t* appIdOut;
#     size_t appIdNum;
#     alljoyn_msgarg_get(args, "ay", &appIdNum, &appIdOut);
#     ASSERT_EQ(16u, appIdNum);
#     for (size_t i = 0; i < appIdNum; ++i) {
#         EXPECT_EQ(appId[i], appIdOut[i]);
#     }

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::DEFAULT_LANGUAGE, &args);
#     char* defaultLanguage;
#     alljoyn_msgarg_get(args, "s", &defaultLanguage);
#     EXPECT_STREQ("en", defaultLanguage);

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::DEVICE_ID, &args);
#     char* deviceId;
#     alljoyn_msgarg_get(args, "s", &deviceId);
#     EXPECT_STREQ("fakeID", deviceId);

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::APP_NAME, &args);
#     char* appName;
#     alljoyn_msgarg_get(args, "s", &appName);
#     EXPECT_STREQ("Application", appName);

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::MANUFACTURER, &args);
#     char* manufacturer;
#     alljoyn_msgarg_get(args, "s", &manufacturer);
#     EXPECT_STREQ("Manufacturer", manufacturer);

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            AboutData::MODEL_NUMBER, &args);
#     char* modelNumber;
#     alljoyn_msgarg_get(args, "s", &modelNumber);
#     EXPECT_STREQ("123456", modelNumber);

#     status = alljoyn_msgarg_getdictelement(aboutArg, "{sv}",
#                                            "SupportNumber", &args);
#     char* supportNumber;
#     alljoyn_msgarg_get(args, "s", &supportNumber);
#     EXPECT_STREQ("888-555-1234", supportNumber);
#     alljoyn_msgarg_destroy(aboutArg);
#     alljoyn_aboutdata_destroy(aboutData);
# }

# TEST(AboutDataTest, InitUsingMsgArg) {
#     QStatus status = ER_FAIL;
#     alljoyn_aboutdata aboutData = alljoyn_aboutdata_create("en");

#     uint8_t originalAppId[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 };
#     status = alljoyn_aboutdata_setappid(aboutData, originalAppId, 16);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdeviceid(aboutData, "fakeID");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "Application", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "Manufacturer", "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmodelnumber(aboutData, "123456");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "A poetic description of this application",
#                                               "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setsoftwareversion(aboutData, "0.1.2");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "en"));

#     status = alljoyn_aboutdata_setsupportedlanguage(aboutData, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setappname(aboutData, "aplicacion", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setmanufacturer(aboutData, "manufactura", "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     status = alljoyn_aboutdata_setdescription(aboutData,
#                                               "Una descripcion poetica de esta aplicacion",
#                                               "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_TRUE(alljoyn_aboutdata_isvalid(aboutData, "es"));

#     alljoyn_msgarg arg = alljoyn_msgarg_create();

#     status = alljoyn_msgarg_set(arg, "s", "888-555-1234");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_msgarg_set(arg, "s", "800-555-4321");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     status = alljoyn_aboutdata_setfield(aboutData, "SupportNumber", arg, "es");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     alljoyn_msgarg aboutArg = alljoyn_msgarg_create();
#     status = alljoyn_aboutdata_getaboutdata(aboutData, aboutArg, "en");

#     alljoyn_aboutdata aboutDataInit = alljoyn_aboutdata_create("en");
#     status = alljoyn_aboutdata_createfrommsgarg(aboutDataInit, aboutArg, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     uint8_t* appId;
#     size_t num;
#     status = alljoyn_aboutdata_getappid(aboutDataInit, &appId, &num);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     ASSERT_EQ(16u, num);
#     for (size_t i = 0; i < num; i++) {
#         EXPECT_EQ(originalAppId[i], appId[i]);
#     }

#     char* deviceId;
#     status = alljoyn_aboutdata_getdeviceid(aboutDataInit, &deviceId);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("fakeID", deviceId);

#     char* appName;
#     status = alljoyn_aboutdata_getappname(aboutDataInit, &appName, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("Application", appName);

#     char* manufacturer;
#     status = alljoyn_aboutdata_getmanufacturer(aboutDataInit, &manufacturer, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("Manufacturer", manufacturer);

#     char* modelNumber;
#     status = alljoyn_aboutdata_getmodelnumber(aboutDataInit, &modelNumber);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("123456", modelNumber);

#     char* description;
#     status = alljoyn_aboutdata_getdescription(aboutDataInit, &description, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("A poetic description of this application", description);

#     alljoyn_msgarg value;
#     alljoyn_aboutdata_getfield(aboutDataInit, "SupportNumber", &value, "en");
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);

#     char buf[2];
#     alljoyn_msgarg_signature(value, buf, 2);
#     EXPECT_STREQ("s", buf);
#     const char* supportNumber;
#     status = alljoyn_msgarg_get(value, "s", &supportNumber);
#     EXPECT_EQ(ER_OK, status) << "  Actual Status: " << QCC_StatusText(status);
#     EXPECT_STREQ("888-555-1234", supportNumber);

#     size_t number_languages =
#         alljoyn_aboutdata_getsupportedlanguages(aboutDataInit, NULL, 0);
#     EXPECT_EQ(2u, number_languages);
#     /* TODO complete the test for language and other required */
#     alljoyn_msgarg_destroy(aboutArg);
#     alljoyn_aboutdata_destroy(aboutData);
#     alljoyn_aboutdata_destroy(aboutDataInit);
# }




import unittest

from AllJoynPy import AllJoyn, AboutListener, MsgArg, AboutData, \
    QStatusException, AboutObjectDescription, Session, \
    TransportMask, SessionListener, AboutProxy, ProxyBusObject, \
    Message, BusListener, BusAttachment, MsgArgHandle, QStatus

from numpy.ctypeslib import ndpointer
import ctypes as C


class TestAboutDataMethods(unittest.TestCase):

    def setUp(self):
        self.alljoyn = AllJoyn()

    def test_DefaultLanguageNotSpecified(self):
        aboutData = AboutData.AboutData.CreateFromEmpty()

        self.assertRaises(QStatusException, aboutData.SetDeviceName, "Device Name", None)

        self.assertRaises(QStatusException, aboutData.SetAppName, "Application Name", None)

        self.assertRaises(QStatusException, aboutData.SetManufacturer, "Manufacturer Name", None)

        self.assertRaises(QStatusException, aboutData.SetDescription, "A description of the application.", None)

        del aboutData


    def test_SetAppId_using_uuid_string(self):
        aboutData = AboutData.AboutData(language="en")

        # Not a hex digit
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "g00102030405060708090a0b0c0d0e0f")

        # Odd number of characters parsing error
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "00102030405060708090a0b0c0d0e0f")

        # Too few characters
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "0102030405060708090a0b0c0d0e0f")

        # Too many characters
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "000102030405060708090a0b0c0d0e0f10")

        # Not valid uuid parsing error
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "000102030405-060708090A0B-0C0D0E0F10")

        # Not valid uuid parsing error
        self.assertRaises(QStatusException, aboutData.SetAppIdFromString, "00010203-04050607-0809-0A0B-0C0D0E0F")

        status = aboutData.SetAppIdFromString("000102030405060708090a0b0c0d0e0f")
        self.assertEqual(QStatus.ER_OK, status)

        appId = aboutData.GetAppId()
        self.assertEqual(appId, range(0,16))

        aboutData2 = AboutData.AboutData(language="en")

        status = aboutData2.SetAppIdFromString("000102030405060708090A0B0C0D0E0F")
        self.assertEqual(QStatus.ER_OK, status)

        appId = aboutData2.GetAppId()
        self.assertEqual(appId, range(0,16))

        # Use capital hex digits UUID as per RFC 4122
        aboutData3 = AboutData.AboutData(language="en")

        status = aboutData3.SetAppIdFromString("00010203-0405-0607-0809-0A0B0C0D0E0F")
        self.assertEqual(QStatus.ER_OK, status)

        appId = aboutData3.GetAppId()
        self.assertEqual(appId, range(0,16))


        # Use lowercase hex digits UUID as per RFC 4122 
        aboutData4 = AboutData.AboutData(language="en")

        status = aboutData4.SetAppIdFromString("00010203-0405-0607-0809-0a0b0c0d0e0f")
        self.assertEqual(QStatus.ER_OK, status)

        appId = aboutData4.GetAppId()
        self.assertEqual(appId, range(0,16))

        del aboutData
        del aboutData2
        del aboutData3
        del aboutData4


    def test_CreateFromXml(self):
        status = QStatus.ER_FAIL
        aboutData = AboutData.AboutData()
        xml = "<AboutData>" \
                "  <AppId>000102030405060708090A0B0C0D0E0C</AppId>" \
                "  <DefaultLanguage>en</DefaultLanguage>" \
                "  <DeviceName>My Device Name</DeviceName>" \
                "  <DeviceName lang = 'es'>Nombre de mi dispositivo</DeviceName>" \
                "  <DeviceId>baddeviceid</DeviceId>" \
                "  <AppName>My Application Name</AppName>" \
                "  <AppName lang = 'es'>Mi Nombre de la aplicación</AppName>" \
                "  <Manufacturer>Company</Manufacturer>" \
                "  <Manufacturer lang = 'es'>Empresa</Manufacturer>" \
                "  <ModelNumber>Wxfy388i</ModelNumber>" \
                "  <Description>A detailed description provided by the application.</Description>" \
                "  <Description lang = 'es'>Una descripción detallada proporcionada por la aplicación.</Description>" \
                "  <DateOfManufacture>2014-01-08</DateOfManufacture>" \
                "  <SoftwareVersion>1.0.0</SoftwareVersion>" \
                "  <HardwareVersion>1.0.0</HardwareVersion>" \
                "  <SupportUrl>www.example.com</SupportUrl>" \
                "  <UserDefinedTag>Can only accept strings anything other than strings must be done using the AboutData Class SetField method</UserDefinedTag>" \
                "  <UserDefinedTag lang='es'>Sólo se puede aceptar cadenas distintas de cadenas nada debe hacerse utilizando el método AboutData Clase SetField</UserDefinedTag>" \
                "</AboutData>"
        status = aboutData.CreateFromXML(xml)
        self.assertEqual(QStatus.ER_OK, status)

        # OriginalAppId is the string 000102030405060708090A0B0C0D0E0C converted to an array of bytes
        appId = aboutData.GetAppId()
        self.assertEqual(appId, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12])

        language = aboutData.GetDefaultLanguage()
        self.assertEqual("en", language)

        deviceName = aboutData.GetDeviceName()
        self.assertEqual("My Device Name", deviceName)

        deviceName = aboutData.GetDeviceName(language="es")
        self.assertEqual("Nombre de mi dispositivo", deviceName)

        deviceId = aboutData.GetDeviceId()
        self.assertEqual("baddeviceid", deviceId)

        appName = aboutData.GetAppName()
        self.assertEqual("My Application Name", appName)

        appName = aboutData.GetAppName(language="es")
        self.assertEqual("Mi Nombre de la aplicación", appName)

        manufacturer = aboutData.GetManufacturer()
        self.assertEqual("Company", manufacturer)

        manufacturer = aboutData.GetManufacturer(language="es")
        self.assertEqual("Empresa", manufacturer)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        description = aboutData.GetDescription()
        self.assertEqual("A detailed description provided by the application.", description)

        description = aboutData.GetDescription(language="es")
        self.assertEqual("Una descripción detallada proporcionada por la aplicación.", description)

        model = aboutData.GetModelNumber()
        self.assertEqual("Wxfy388i", model)

        date_of_manufacture = aboutData.GetDateOfManufacture()
        self.assertEqual("2014-01-08", date_of_manufacture)

        software_version = aboutData.GetSoftwareVersion()
        self.assertEqual("1.0.0", software_version)

        aj_software_version = aboutData.GetAJSoftwareVersion()
        print "AJ Software Version", aj_software_version

        hardware_version = aboutData.GetHardwareVersion()
        self.assertEqual("1.0.0", hardware_version)

        support_url = aboutData.GetSupportURL()
        self.assertEqual("www.example.com", support_url)

        del aboutData



    def test_caseInsensitiveLanguageTag(self):
        status = QStatus.ER_FAIL
        aboutData = AboutData.AboutData()

        language = aboutData.GetDefaultLanguage()
        self.assertEqual("en", language)

        status = aboutData.SetDeviceName("Device", "en");
        self.assertEqual(QStatus.ER_OK, status)

        status = aboutData.SetDeviceName("dispositivo", "es");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        status = aboutData.SetDeviceName("Device", "EN");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        status = aboutData.SetDeviceName("Device", "eN");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        status = aboutData.SetDeviceName("dispositivo", "ES");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        status = aboutData.SetDeviceName("dispositivo", "Es");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        status = aboutData.SetDeviceName("dispositivo", "es");
        self.assertEqual(QStatus.ER_OK, status)

        languages = aboutData.GetSupportedLanguages()
        self.assertEqual(['en', 'es'], languages)

        deviceName = aboutData.GetDeviceName(language="EN")
        self.assertEqual("Device", deviceName)

        deviceName = aboutData.GetDeviceName(language="En")
        self.assertEqual("Device", deviceName)

        deviceName = aboutData.GetDeviceName(language="eN")
        self.assertEqual("Device", deviceName)

        deviceName = aboutData.GetDeviceName(language="ES")
        self.assertEqual("dispositivo", deviceName)

        deviceName = aboutData.GetDeviceName(language="Es")
        self.assertEqual("dispositivo", deviceName)

        deviceName = aboutData.GetDeviceName(language="eS")
        self.assertEqual("dispositivo", deviceName)

        del aboutData


if __name__ == '__main__':
    unittest.main()
