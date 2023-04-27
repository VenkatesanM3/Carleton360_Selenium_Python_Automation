Feature: Carleton 360 Login

  Background: Open Form Authentication page
    Given I have navigated to the "Carleton 360 login" page

  Scenario: Validating_the_Carleton_360_login_home_page
    Then I should see the login page title with icon "Carleton 360"
    And I should see the correct opening text "Please select the appropriate login for you."
    And I should see the option "Have a Carleton360 account?" with text "You have created an account but have not yet submitted an application to Carleton."
    And I should see the button for the option "Have a Carleton360 account?" with "Log in here with your email →"
    And I should see the option "Already have a MyCarletonOne (MC1) account?" with text "You have previously submitted an application, or are a student, staff or faculty member."
    And I should see the button for the option "Already have a MyCarletonOne (MC1) account?" with "Log in here with your MC1 credentials →"
    And I should see the option "No Account?" with text "No Account?"
    And I should see the button for the option "No Account?" with "Register for Carleton360"

  Scenario: Validating the CARLETON 360 LOGIN page
    Then I should be able to click the button for the option "Have a Carleton360 account?" with "Log in here with your email →"
    And should navigate to the "CARLETON 360 LOGIN" page see the Carleton360 login page title with icon "Carleton 360"
    And I should see the "← Back" button on the "CARLETON 360 LOGIN" page
    And I should see the "Carleton 360 Login" panel title
    And I should see the "Username" input box on the "CARLETON 360 LOGIN" page
    And I should see the "Password" input box on the "CARLETON 360 LOGIN" page
    And I should see the "Log in" button on the "CARLETON 360 LOGIN" page
    And I should see the "Forgot password?" button on the "CARLETON 360 LOGIN" page

  Scenario: Validating the CARLETON 360 LOGIN buttons navigation
    Then I should be able to click the button for the option "Have a Carleton360 account?" with "Log in here with your email →"
    And should navigate to the "CARLETON 360 LOGIN" page see the Carleton360 login page title with icon "Carleton 360"
    And I should be able to click "← Back" button on the "CARLETON 360 LOGIN" page
    And I should see the login page title with icon "Carleton 360"
    And I should see the correct opening text "Please select the appropriate login for you."
    And I should be able to click the button for the option "Have a Carleton360 account?" with "Log in here with your email →"
    And should navigate to the "CARLETON 360 LOGIN" page see the Carleton360 login page title with icon "Carleton 360"
    And I should be able to click "Forgot password?" button on the "CARLETON 360 LOGIN" page
    And should redirected to the correct link page "https://360.carleton.ca/urd/sits.urd//run/siw_pqs.forgot?"
    And should validate the text "FORGOT PASSWORD?" "Please enter your account details in order to reset your Carleton360 Password." "Important!" "MC1 Accounts and Passwords"
    And I should see the "Account Verification" panel title
    And I should see the "Username" input box on the "Forgot password" page
    And I should see the "Surname" input box on the "Forgot password" page
    And I should see the "Date of birth" input box on the "Forgot password" page
    And I should be able to click "MC1 Accounts and Passwords" link text on the "Forgot password" page
    And should validate the redirected page "https://carleton.ca/its/help-centre/accounts-and-passwords/"

  Scenario: Failed Carleton360 login
    Then I should be able to click the button for the option "Have a Carleton360 account?" with "Log in here with your email →"
    And should navigate to the "CARLETON 360 LOGIN" page see the Carleton360 login page title with icon "Carleton 360"
    And I should see an empty "Username" input box on the "CARLETON 360 LOGIN" page
    And I should see an empty "Password" input box on the "CARLETON 360 LOGIN" page
    And I should be able to click "Log in" button on the "CARLETON 360 LOGIN" page
    And I should see a "Username Not Provided" error message "In order to login, you must provide a username."
    And I should be able to enter "Venkat" in "Username" input box on the "CARLETON 360 LOGIN" page
    And I should see an empty "Password" input box on the "CARLETON 360 LOGIN" page
    And I should be able to click "Log in" button on the "CARLETON 360 LOGIN" page
    And I should see a "Password Not Provided" error message "In order to login, you must provide a password."
    And I should be able to enter "Venkat" in "Password" input box on the "CARLETON 360 LOGIN" page
    And I should be able to click "Log in" button on the "CARLETON 360 LOGIN" page
    And I should see a "Username and/or password Invalid" error message "The user name or password you supplied are invalid. Please try again."

  Scenario: Validating the Carleton SSO Federated Portal page
    Then I should be able to click the button for the option "Already have a MyCarletonOne (MC1) account?" with "Log in here with your MC1 credentials →"
    And should navigate to the "Carleton SSO Federated Portal" page see the "Sign In" page title
    And I should validate the login message "Welcome to the Carleton SSO Federated Portal. " "MyCarletonOne"
    And I should see the "Username" input box on the "Carleton SSO Federated Portal" page
    And I should see the "Password" input box on the "Carleton SSO Federated Portal" page
    And I should see the "Sign In" button on the "Carleton SSO Federated Portal" page
    And I should see the "Forgot password?" button on the "Carleton SSO Federated Portal" page
    And I should be able to click "Password" link text on the "Carleton SSO Federated Portal" page
    And should validate the redirected page "https://carleton.ca/its/help-centre/confirm-account-registration/"
#    And I should be able to click "MyCarletonOne" link text on the "Carleton SSO Federated Portal" page
#    And should validate the redirected page "https://carleton.ca/its/help-centre/confirm-account-registration/"

  Scenario: Failed Carleton SSO login
    Then I should be able to click the button for the option "Already have a MyCarletonOne (MC1) account?" with "Log in here with your MC1 credentials →"
    And should navigate to the "Carleton SSO Federated Portal" page see the "Sign In" page title
    And I should see an empty "Username" input box on the "Carleton SSO Federated Portal" page
    And I should see an empty "Password" input box on the "Carleton SSO Federated Portal" page
    And I should be able to click "Sign In" button on the "Carleton SSO Federated Portal" page
    And I should see a "Enter your MyCarletonOne username in the format "cunet\username" or "username@cunet.carleton.ca"." error message for "Username Not Provided"
    And I should be able to enter "Venkat" in "Username" input box on the "Carleton SSO Federated Portal" page
    And I should see an empty "Password" input box on the "Carleton SSO Federated Portal" page
    And I should be able to click "Sign In" button on the "Carleton SSO Federated Portal" page
    And I should see a "Enter your current MyCarletonOne password." error message for "Password Not Provided"
    And I should be able to enter "Venkat" in "Password" input box on the "Carleton SSO Federated Portal" page
    And I should be able to click "Sign In" button on the "Carleton SSO Federated Portal" page
    And I should see a "Incorrect user ID or password. Type the correct user ID and password, and try again." error message for "Username and/or password Invalid"

  Scenario: Validating the Carleton 360 Registration page
    Then I should be able to click the button for the option "No Account?" with "Register for Carleton360"
    And should navigate to the "Carleton 360 Registration" page see the Carleton360 login page title with icon "Carleton 360"
    And I should see the "Thank you for your interest in Carleton University" panel title
    And I should validate the message "Please fill in the details below to sign up for Carleton360 so we can provide you with the information you're looking for." "If you have previously signed up for a Carleton360 account,  " "login here"
#    And I should see the "login here" link text on the "Carleton 360 Registration" page
    And I should see the input labels on the Carleton 360 Registration page
      | label                                       |
      | First Name                                  |
      | Middle Name(s)                              |
      | Last Name                                   |
      | Email Address                               |
      | Verify Email Address                        |
      | Date of Birth                               |
      | In which level of study are you interested? |
    And I should be able to click "In which level of study are you interested?" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "In which level of study are you interested? options"
      | options               |
      | Undergraduate Studies |
      | Graduate Studies      |
    And I select "Undergraduate Studies" from the dropdown list for the "In which level of study are you interested? options"
    And I should see the input labels on the Carleton 360 Registration page
      | label                               |
      | Country of Residence                |
      | Select your program(s) of interest* |
    And I should be able to click "Country of Residence" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Country of Residence options"
      | country                         |
      | Canada                          |
      | Afghanistan                     |
      | Aland Islands                   |
      | Albania                         |
      | American Samoa                  |
      | Algeria                         |
      | Andorra                         |
      | Angola                          |
      | Anguilla                        |
      | Antarctica                      |
      | Antigua and Barbuda             |
      | Argentina                       |
      | Armenia                         |
      | Aruba                           |
      | Australia                       |
      | Austria                         |
      | Azerbaijan                      |
      | Bahamas                         |
      | Bahrain                         |
      | Bangladesh                      |
      | Barbados                        |
      | Belarus                         |
      | Belgium                         |
      | Belize                          |
      | Benin                           |
      | Bermuda                         |
      | Bhutan                          |
      | Bolivia                         |
      | Bonaire, St Eust & Saba         |
      | Bosnia                          |
      | Botswana                        |
      | Bouvet Island                   |
      | Brazil                          |
      | British Indian Ocean Territory  |
      | Brunei                          |
      | Bulgaria                        |
      | Burkina Faso                    |
      | Burundi                         |
      | Cabo Verde                      |
      | Cambodia                        |
      | Cameroon                        |
      | Cayman Islands                  |
      | Central African Republic        |
      | Chad                            |
      | Chile                           |
      | China                           |
      | Christmas Island                |
      | Cocos Islands                   |
      | Colombia                        |
      | Comoros                         |
      | Congo                           |
      | Congo, Dem  Rep of the (Zaire)  |
      | Cook Islands                    |
      | Costa Rica                      |
      | Croatia                         |
      | Cuba                            |
      | Curacao                         |
      | Cyprus                          |
      | Czech Republic                  |
      | Denmark                         |
      | Djibouti                        |
      | Dominica                        |
      | Dominican Republic              |
      | East Timor                      |
      | Ecuador                         |
      | Egypt                           |
      | El Salvador                     |
      | England                         |
      | Equatorial Guinea               |
      | Eritrea                         |
      | Estonia                         |
      | Ethiopia                        |
      | Eswatini                        |
      | Ethiopia                        |
      | Falkland Islands (Malvinas)     |
      | Faroe Islands                   |
      | Fiji                            |
      | Finland                         |
      | France                          |
      | French Guiana                   |
      | French Polynesia                |
      | French Southern Territories     |
      | Gabon                           |
      | Gambia                          |
      | Georgia                         |
      | Germany                         |
      | Ghana                           |
      | Gibraltar                       |
      | Greece                          |
      | Greenland                       |
      | Grenada                         |
      | Guadeloupe                      |
      | Guam                            |
      | Guatemala                       |
      | Guernsey                        |
      | Guinea                          |
      | Guinea-Bissau                   |
      | Guyana                          |
      | Haiti                           |
      | Heard and McDonald Islands      |
      | Honduras                        |
      | Hong Kong                       |
      | Hungary                         |
      | Iceland                         |
      | India                           |
      | Indonesia                       |
      | Iran                            |
      | Iraq                            |
      | Ireland                         |
      | Isle Of Man                     |
      | Israel                          |
      | Italy                           |
      | Ivory Coast                     |
      | Jamaica                         |
      | Japan                           |
      | Jersey                          |
      | Jordan                          |
      | Kazakhstan                      |
      | Kenya                           |
      | Kiribati                        |
      | Korea,(D.P.R.)                  |
      | Korea,(Rep.of)                  |
      | Kosovo                          |
      | Kuwait                          |
      | Kyrgyzstan                      |
      | Laos                            |
      | Latvia                          |
      | Lebanon                         |
      | Lesotho                         |
      | Liberia                         |
      | Libya                           |
      | Liechtenstein                   |
      | Lithuania                       |
      | Luxembourg                      |
      | Macau                           |
      | Macedonia                       |
      | Madagascar                      |
      | Malawi                          |
      | Malaysia                        |
      | Maldives                        |
      | Mali                            |
      | Malta                           |
      | Marshall Islands                |
      | Martinique                      |
      | Mauritania                      |
      | Mauritius                       |
      | Mayotte                         |
      | Mexico                          |
      | Micronesia, Federated States of |
      | Moldova, Rep. of                |
      | Monaco                          |
      | Mongolia                        |
      | Montenegro                      |
      | Montserrat                      |
      | Morocco                         |
      | Mozambique                      |
      | Myanmar                         |
      | Namibia                         |
      | Nauru                           |
      | Nepal                           |
      | Netherlands                     |
      | New Caledonia                   |
      | New Zealand                     |
      | Nicaragua                       |
      | Niger                           |
      | Nigeria                         |
      | Niue                            |
      | Norfolk Island                  |
      | Northern Ireland                |
      | Northern Mariana Islands        |
      | Norway                          |
      | Oman                            |
      | Pakistan                        |
      | Palau                           |
      | Palestine                       |
      | Panama                          |
      | Papua New Guinea                |
      | Paraguay                        |
      | Peru                            |
      | Philippines                     |
      | Pitcairn                        |
      | Poland                          |
      | Portugal                        |
      | Puerto Rico                     |
      | Qatar                           |
      | Reunion                         |
      | Romania                         |
      | Russia                          |
      | Rwanda                          |
      | Saint Barthelemy                |
      | Saint Helena                    |
      | Saint Kitts and Nevis           |
      | Saint Lucia                     |
      | Saint Martin (French Pt)        |
      | Saint Pierre & Miquelon         |
      | Samoa                           |
      | San Marino                      |
      | Sao Tome and Principe           |
      | Sark                            |
      | Saudi Arabia                    |
      | Scotland                        |
      | Senegal                         |
      | Serbia                          |
      | Seychelles                      |
      | Sierra Leone                    |
      | Singapore                       |
      | Sint Maarten (Dutch Pt)         |
      | Slovak Republic                 |
      | Slovenia                        |
      | Solomon Islands                 |
      | Somalia                         |
      | South Africa                    |
      | South Georgia & S. Sandwich Is  |
      | South Sudan                     |
      | Spain                           |
      | Sri Lanka                       |
      | St. Vincent and The Grenadines  |
      | Sudan                           |
      | Suriname                        |
      | Svalbard & Jan Mayen Islands    |
      | Swaziland                       |
      | Sweden                          |
      | Switzerland                     |
      | Syria                           |
      | Taiwan                          |
      | Tajikistan                      |
      | Tanzania                        |
      | Thailand                        |
      | Togo                            |
      | Tokelau                         |
      | Tonga                           |
      | Trinidad & Tobago               |
      | Tunisia                         |
      | Turkey                          |
      | Turkmenistan                    |
      | Turks & Caicos Islands          |
      | Tuvalu                          |
      | U.S. Minor Outlying Islands     |
      | Uganda                          |
      | Ukraine                         |
      | United Arab Emirates            |
      | United Kingdom                  |
      | United States                   |
      | Uruguay                         |
      | Uzbekistan                      |
      | Vanuatu                         |
      | Vatican City State              |
      | Venezuela                       |
      | Vietnam                         |
      | Vatican City State              |
      | Virgin Islands (U.S.)           |
      | Wales                           |
      | Wallis & Futuna                 |
      | Western Sahara                  |
      | Yemen                           |
      | Zambia                          |
      | Zimbabwe                        |
    And I select "India" from the dropdown list for the "Country of Residence options"
    And I should be able to click "Select your program(s) of interest*" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Select your program(s) of interest* options"
      | option                                           |
      | Bachelor of Architectural Studies                |
      | Bachelor of Arts                                 |
      | Bachelor of Cognitive Science                    |
      | Bachelor of Commerce                             |
      | Bachelor of Communication and Media Studies      |
      | Bachelor of Computer Science                     |
      | Bachelor of Economics                            |
      | Bachelor of Engineering                          |
      | Bachelor of Global and International Studies     |
      | Bachelor of Health Sciences                      |
      | Bachelor of Humanities (Great Books)             |
      | Bachelor of Industrial Design                    |
      | Bachelor of Information Technology               |
      | Bachelor of International Business               |
      | Bachelor of Journalism                           |
      | Bachelor of Journalism and Humanities            |
      | Bachelor of Mathematics                          |
      | Bachelor of Media Production and Design          |
      | Bachelor of Music                                |
      | Bachelor of Public Affairs and Policy Management |
      | Bachelor of Science                              |
      | Bachelor of Social Work                          |
    And I select "Bachelor of Engineering" from the dropdown list for the "Select your program(s) of interest* options"
    And I should be able to click "Expected Entry Term" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Expected Entry Term options"
      | option         |
      | September 2023 |
      | January 2024   |
      | September 2024 |
      | September 2025 |
      | September 2026 |
    And I select "September 2023" from the dropdown list for the "Expected Entry Term options"
    And I should be able to click "In which level of study are you interested?" input on the "Carleton 360 Registration" page
    And I select "Graduate Studies" from the dropdown list for the "In which level of study are you interested? options"
    And I should see the input labels on the Carleton 360 Registration page
      | label                                                   |
      | In which graduate level(s) of study are you interested? |
      | Country of Residence                                    |
      | Country of Citizenship                                  |
      | Is your most recent degree from a Canadian institution? |
      | Current or highest level of education                   |
    And I should be able to click "In which graduate level(s) of study are you interested?" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "In which graduate level(s) of study are you interested? options"
      | option                 |
      | Master's Programs      |
      | PhD Programs           |
      | Collaborative Programs |
      | Graduate Diplomas      |
## I commented the some of the steps because it will take more time to execute
#    And I select "Master's Programs" from the dropdown list for the "In which graduate level(s) of study are you interested? options"
#    And I should be able to click "Master's Programs" input on the "Carleton 360 Registration" page
#    And the dropdown contains the following "Master's Programs options"
#      | option                                                                |
#      | Accounting (Master's)                                                 |
#      | Aerospace Engineering (Master's)                                      |
#      | Anthropology (Master's)                                               |
#      | Applied Business Analytics: TIM (Master's)                            |
#      | Applied Linguistics and Discourse Studies (Master's)                  |
#      | Architectural Studies (Master's)                                      |
#      | Architecture (Master's)                                               |
#      | Art & Architectural  History (Master's)                               |
#      | Biology (Master's)                                                    |
#      | Biomedical Engineering (Master's)                                     |
#      | Building Engineering (Master's)                                       |
#      | Canadian Studies (Master's)                                           |
#      | Chemistry (Master's)                                                  |
#      | Civil Engineering (Master's)                                          |
#      | Cognitive Science (Master's)                                          |
#      | Communication (Master's)                                              |
#      | Computer Science (Master's)                                           |
#      | Data Science, Analytics, and AI (Master's)                            |
#      | Design (Master's)                                                     |
#      | Earth Sciences (Master's)                                             |
#      | Economics (Master's)                                                  |
#      | Electrical and Computer Engineering (Master's)                        |
#      | Engineering Practice (Master's)                                       |
#      | English (Master's)                                                    |
#      | Entrepreneurship (Master's)                                           |
#      | Environmental Engineering (Master's)                                  |
#      | European, Russian and Eurasian Studies (Master's)                     |
#      | Film Studies (Master's)                                               |
#      | Finance (Master's)                                                    |
#      | French and Francophone Studies (Master's)                             |
#      | Geography (Master's)                                                  |
#      | Health Sciences (Master's)                                            |
#      | Health: Science, Technology and Policy (Master's)                     |
#      | History (Master's)                                                    |
#      | Human-Computer Interaction (Master's)                                 |
#      | Information Technology (Digital Media, Network Technology) (Master's) |
#      | Infrastructure Protection and International Security (Master's)       |
#      | International Affairs (Master's)                                      |
#      | International Affairs / Juris Doctor (Master's)                       |
#      | Journalism (Master's)                                                 |
#      | Legal Studies (Master's)                                              |
#      | Linguistics (Master's)                                                |
#      | MBA (Business Administration) (Master's)                              |
#      | MBA in Bogotá (Business Administration) (Master's)                    |
#      | MBA in Shanghai (Business Administration) (Master's)                  |
#      | Management (Master's)                                                 |
#      | Materials Engineering (Master's)                                      |
#      | Mathematics and Statistics (Master's)                                 |
#      | Mechanical Engineering (Master's)                                     |
#      | Migration and Diaspora Studies (Master's)                             |
#      | Music and Culture (Master's)                                          |
#      | Neuroscience (Master's)                                               |
#      | Northern Studies (Master's)                                           |
#      | Philanthropy and Nonprofit Leadership (Master's)                      |
#      | Philosophy (Master's)                                                 |
#      | Physics (Master's)                                                    |
#      | Political Economy (Master's)                                          |
##      | Political Management (Master's)                                       |
##      | Political Science (Master's)                                          |
##      | Psychology (Master's)                                                 |
##      | Public History (Master's)                                             |
##      | Public Policy and Administration (Master's)                           |
##      | Religion and Public Life (Master's)                                   |
##      | Social Work (Master's)                                                |
##      | Sociology (Master's)                                                  |
##      | Sustainable Energy (Master's)                                         |
##      | Technology Innovation Management (Master's)                           |
##      | Women's and Gender Studies (Master's)                                 |
#    And I select "Collaborative Programs" from the dropdown list for the "In which graduate level(s) of study are you interested? options"
#    And I should be able to click "Collaborative Programs" input on the "Carleton 360 Registration" page
#    And the dropdown contains the following "Collaborative Programs options"
#      | option                                                         |
#      | Accessibility (Collaborative Master's)                         |
#      | African Studies (Collaborative Master's)                       |
#      | Biochemistry (Collaborative Master's)                          |
#      | Biochemistry (Collaborative PhD)                               |
#      | Bioinformatics (Collaborative Master's)                        |
#      | Biostatistics (Collaborative Master's)                         |
#      | Chemical and Environmental Toxicology (Collaborative Master's) |
#      | Chemical and Environmental Toxicology (Collaborative PhD)      |
#      | Cybersecurity (Collaborative Master's)                         |
#      | Data Science (Collaborative Master's)                          |
#      | Digital Humanities (Collaborative Master's)                    |
#      | Latin American & Caribbean Studies (Collaborative Master's)    |
#      | Political Economy (Collaborative PhD)                          |
#    And I select "Graduate Diplomas" from the dropdown list for the "In which graduate level(s) of study are you interested? options"
#    And I should be able to click "Graduate Diplomas" input on the "Carleton 360 Registration" page
#    And the dropdown contains the following "Graduate Diplomas options"
#      | option                                                                  |
#      | Architectural Conservation (Graduate Diploma)                           |
#      | Conflict Resolution (Graduate Diploma)                                  |
#      | Curatorial Studies (Graduate Diploma)                                   |
#      | Economic Policy (Graduate Diploma)                                      |
#      | Ethics and Public Affairs (Graduate Diploma)                            |
#      | European Integration Studies (Graduate Diploma)                         |
#      | Health Policy (Graduate Diploma)                                        |
#      | Health: Science, Technology and Policy (Graduate Diploma)               |
#      | Indigenous Policy and Administration (Graduate Diploma)                 |
#      | Infrastructure Protection and International Security (Graduate Diploma) |
#      | Linguistics (Graduate Diploma)                                          |
#      | Migration and Diaspora Studies (Graduate Diploma)                       |
#      | Northern Studies (Graduate Diploma)                                     |
#      | Philanthropy and Nonprofit Leadership (Graduate Diploma)                |
#      | Public Management (Graduate Diploma)                                    |
#      | Public Policy and Program Evaluation (Graduate Diploma)                 |
#      | Social Stats & Data Analysis (Graduate Diploma)                         |
#      | Sustainable Development (Graduate Diploma)                              |
#      | Work and Labour (Graduate Diploma)                                      |
#    And I select "Electrical and Computer Engineering (Master's)" from the dropdown list for the "Master's Programs options"
    And I should be able to click "Expected Entry Term1" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Expected Entry Term options"
      | option      |
      | Winter 2023 |
      | Summer 2023 |
      | Fall 2023   |
      | Winter 2024 |
      | Summer 2024 |
      | Fall 2024   |
      | Winter 2025 |
#    And I select "Fall 2023" from the dropdown list for the "Expected Entry Term options"
    And I should be able to click "Expected Entry Term1" input on the "Carleton 360 Registration" page
    And I should be able to click "Country of Citizenship" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Country of Citizenship options"
      | country        |
      | Canada         |
      | Afghanistan    |
      | Aland Islands  |
      | Albania        |
      | American Samoa |
#      | Algeria                         |
#      | Andorra                         |
#      | Angola                          |
#      | Anguilla                        |
#      | Antarctica                      |
#      | Antigua and Barbuda             |
#      | Argentina                       |
#      | Armenia                         |
#      | Aruba                           |
#      | Australia                       |
#      | Austria                         |
#      | Azerbaijan                      |
#      | Bahamas                         |
#      | Bahrain                         |
#      | Bangladesh                      |
#      | Barbados                        |
#      | Belarus                         |
#      | Belgium                         |
#      | Belize                          |
#      | Benin                           |
#      | Bermuda                         |
#      | Bhutan                          |
#      | Bolivia                         |
#      | Bonaire, St Eust & Saba         |
#      | Bosnia                          |
#      | Botswana                        |
#      | Bouvet Island                   |
#      | Brazil                          |
#      | British Indian Ocean Territory  |
#      | Brunei                          |
#      | Bulgaria                        |
#      | Burkina Faso                    |
#      | Burundi                         |
#      | Cabo Verde                      |
#      | Cambodia                        |
#      | Cameroon                        |
#      | Cayman Islands                  |
#      | Central African Republic        |
#      | Chad                            |
#      | Chile                           |
#      | China                           |
#      | Christmas Island                |
#      | Cocos Islands                   |
#      | Colombia                        |
#      | Comoros                         |
#      | Congo                           |
#      | Congo, Dem  Rep of the (Zaire)  |
#      | Cook Islands                    |
#      | Costa Rica                      |
#      | Croatia                         |
#      | Cuba                            |
#      | Curacao                         |
#      | Cyprus                          |
#      | Czech Republic                  |
#      | Denmark                         |
#      | Djibouti                        |
#      | Dominica                        |
#      | Dominican Republic              |
#      | East Timor                      |
#      | Ecuador                         |
#      | Egypt                           |
#      | El Salvador                     |
#      | England                         |
#      | Equatorial Guinea               |
#      | Eritrea                         |
#      | Estonia                         |
#      | Ethiopia                        |
#      | Eswatini                        |
#      | Ethiopia                        |
#      | Falkland Islands (Malvinas)     |
#      | Faroe Islands                   |
#      | Fiji                            |
#      | Finland                         |
#      | France                          |
#      | French Guiana                   |
#      | French Polynesia                |
#      | French Southern Territories     |
#      | Gabon                           |
#      | Gambia                          |
#      | Georgia                         |
#      | Germany                         |
#      | Ghana                           |
#      | Gibraltar                       |
#      | Greece                          |
#      | Greenland                       |
#      | Grenada                         |
#      | Guadeloupe                      |
#      | Guam                            |
#      | Guatemala                       |
#      | Guernsey                        |
#      | Guinea                          |
#      | Guinea-Bissau                   |
#      | Guyana                          |
#      | Haiti                           |
#      | Heard and McDonald Islands      |
#      | Honduras                        |
#      | Hong Kong                       |
#      | Hungary                         |
#      | Iceland                         |
#      | India                           |
#      | Indonesia                       |
#      | Iran                            |
#      | Iraq                            |
#      | Ireland                         |
#      | Isle Of Man                     |
#      | Israel                          |
#      | Italy                           |
#      | Ivory Coast                     |
#      | Jamaica                         |
#      | Japan                           |
#      | Jersey                          |
#      | Jordan                          |
#      | Kazakhstan                      |
#      | Kenya                           |
#      | Kiribati                        |
#      | Korea,(D.P.R.)                  |
#      | Korea,(Rep.of)                  |
#      | Kosovo                          |
#      | Kuwait                          |
#      | Kyrgyzstan                      |
#      | Laos                            |
#      | Latvia                          |
#      | Lebanon                         |
#      | Lesotho                         |
#      | Liberia                         |
#      | Libya                           |
#      | Liechtenstein                   |
#      | Lithuania                       |
#      | Luxembourg                      |
#      | Macau                           |
#      | Macedonia                       |
#      | Madagascar                      |
#      | Malawi                          |
#      | Malaysia                        |
#      | Maldives                        |
#      | Mali                            |
#      | Malta                           |
#      | Marshall Islands                |
#      | Martinique                      |
#      | Mauritania                      |
#      | Mauritius                       |
#      | Mayotte                         |
#      | Mexico                          |
#      | Micronesia, Federated States of |
#      | Moldova, Rep. of                |
#      | Monaco                          |
#      | Mongolia                        |
#      | Montenegro                      |
#      | Montserrat                      |
#      | Morocco                         |
#      | Mozambique                      |
#      | Myanmar                         |
#      | Namibia                         |
#      | Nauru                           |
#      | Nepal                           |
#      | Netherlands                     |
#      | New Caledonia                   |
#      | New Zealand                     |
#      | Nicaragua                       |
#      | Niger                           |
#      | Nigeria                         |
#      | Niue                            |
#      | Norfolk Island                  |
#      | Northern Ireland                |
#      | Northern Mariana Islands        |
#      | Norway                          |
#      | Oman                            |
#      | Pakistan                        |
#      | Palau                           |
#      | Palestine                       |
#      | Panama                          |
#      | Papua New Guinea                |
#      | Paraguay                        |
#      | Peru                            |
#      | Philippines                     |
#      | Pitcairn                        |
#      | Poland                          |
#      | Portugal                        |
#      | Puerto Rico                     |
#      | Qatar                           |
#      | Reunion                         |
#      | Romania                         |
#      | Russia                          |
#      | Rwanda                          |
#      | Saint Barthelemy                |
#      | Saint Helena                    |
#      | Saint Kitts and Nevis           |
#      | Saint Lucia                     |
#      | Saint Martin (French Pt)        |
#      | Saint Pierre & Miquelon         |
#      | Samoa                           |
#      | San Marino                      |
#      | Sao Tome and Principe           |
#      | Sark                            |
#      | Saudi Arabia                    |
#      | Scotland                        |
#      | Senegal                         |
#      | Serbia                          |
#      | Seychelles                      |
#      | Sierra Leone                    |
#      | Singapore                       |
#      | Sint Maarten (Dutch Pt)         |
#      | Slovak Republic                 |
#      | Slovenia                        |
#      | Solomon Islands                 |
#      | Somalia                         |
#      | South Africa                    |
#      | South Georgia & S. Sandwich Is  |
#      | South Sudan                     |
#      | Spain                           |
#      | Sri Lanka                       |
#      | St. Vincent and The Grenadines  |
#      | Sudan                           |
#      | Suriname                        |
#      | Svalbard & Jan Mayen Islands    |
#      | Swaziland                       |
#      | Sweden                          |
#      | Switzerland                     |
#      | Syria                           |
#      | Taiwan                          |
#      | Tajikistan                      |
#      | Tanzania                        |
#      | Thailand                        |
#      | Togo                            |
#      | Tokelau                         |
#      | Tonga                           |
#      | Trinidad & Tobago               |
#      | Tunisia                         |
#      | Turkey                          |
#      | Turkmenistan                    |
#      | Turks & Caicos Islands          |
#      | Tuvalu                          |
#      | U.S. Minor Outlying Islands     |
#      | Uganda                          |
#      | Ukraine                         |
#      | United Arab Emirates            |
#      | United Kingdom                  |
#      | United States                   |
#      | Uruguay                         |
#      | Uzbekistan                      |
#      | Vanuatu                         |
#      | Vatican City State              |
#      | Venezuela                       |
#      | Vietnam                         |
#      | Vatican City State              |
#      | Virgin Islands (U.S.)           |
#      | Wales                           |
#      | Wallis & Futuna                 |
#      | Western Sahara                  |
#      | Yemen                           |
#      | Zambia                          |
#      | Zimbabwe                        |
    And I select "India" from the dropdown list for the "Country of Citizenship options"
    And I should be able to click "Is your most recent degree from a Canadian institution?" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Is your most recent degree from a Canadian institution? options"
      | option |
      | Yes    |
      | No     |
    And I select "No" from the dropdown list for the "Is your most recent degree from a Canadian institution? options"
    And I should be able to click "Current or highest level of education" input on the "Carleton 360 Registration" page
    And the dropdown contains the following "Current or highest level of education options"
      | option               |
      | Bachelor's           |
      | Doctoral             |
      | Graduate Certificate |
      | Graduate Diploma     |
      | Master's             |
    And I select "Master's" from the dropdown list for the "Current or highest level of education options"
    And I should see the "SUBMIT" button on the "Carleton 360 Registration" page

#  We can add multiple scenarios related to Carleton 360 like Successful Login here

#  Scenario: Successful login
#    Given I am on the login page
#    When I enter valid credentials
#    Then I should be logged in successfully
#
#  Scenario: Successful Carleton360 login
#    Given I am on the login page
#    When I click on the Carleton360 login option
#    And I enter valid Carleton360 email and password
#    Then I should be redirected to the Carleton360 home page

