# Security Patterns Service Installation

In this wiki page we describe how the Security Patterns Service can be installed.

## Installation using Anaconda

In this section, we provide instructions on how the user can build the python Flask server of the Security Patterns Service from scratch, using the Anaconda virtual environment. The Security Patterns Service is developed to run on Windows systems with python 3.6.* installed. We suggest installing python via the Anaconda distribution as it provides an easy way to create a virtual environment and install dependencies. The configuration steps needed, are described below:

- **Step 1**: Download the latest [Anaconda distribution](https://www.anaconda.com/products/individual) and follow the installation steps described in the [Anaconda documentation](https://docs.anaconda.com/anaconda/install/windows/).

- **Step2**: Open Anaconda cmd. Running Anaconda cmd activates the base environment. We need to create a specific environment to run the Security Patterns Service. Create a new python 3.6.4 environment by running the following command:

```
conda create --name security_patterns python=3.6.4
```

This command will result in the creation of a conda environment named security_patterns. In order to activate the new environment, execute the following command:

```
conda activate security_patterns
```

- **Step 3**: Now that the environment is activated, install the required libraries:

```
conda install -c anaconda flask flask-cors pymongo waitress dnspython
```

- **Step 4**: Clone the latest Security Patterns version that can be found in the present Github repository of the Security Patterns Service and navigate to the root directory.

- **Step 5**: To start the server, use the command promt inside the active environment and execute the following command:


# Security Patterns Service Usage

In this wiki page we describe how the Security Patterns Service can be used. 
Given a problem statement and a set of forces acting on the system, design patterns instruct its stakeholders on how to build this system. Patterns in the information technology environment provide information system architects with a technique for creating reusable solutions to design challenges. In this document, we describe the main functionality of the Security Patterns web service and how it can be put in practice in order to provide the user with useful information regarding Security Requirements (e.g. Authentication, Authorization, etc.) Security Patterns (e.g. Authenticator, Cryptographic), Security Control Technologies (e.g. OAuth2.0, Two Factor Authentication, etc.) and Security Libraries in Java or Python that utilize the aforementioned technologies. As part of the SmartCLIDE platform, the current service is an attempt to assist developers in selecting the most suitable security patterns and implementing them in their software. Detailed description and indicative examples of the usage of the Security Patterns web service are provided, to facilitate better understanding.
The Security Patterns web service provides the user with valuable information on the security domain as mentioned earlier. All information regarding this service is stored in a mongo database and the information of interest will be extracted and presented to the user when requested. This is achieved through a dedicated API exposed by the RESTful web server, which is, in fact, a simple HTTP GET request. The inputs that need to be provided as parameters to this request are listed below:
|   Parameter  |                           Description                           | Required |                                                                                                                                                                Valid Inputs                                                                                                                                                               |
|:------------:|:---------------------------------------------------------------:|:--------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| requirement      | The main security category that the user is interested in.        |    Yes   | A string value acting as security requirement (e.g. Authentication, Authorization, etc.). |
| pattern | The security pattern that the user is interested in.     |    No    | A string acting as security pattern (e.g. Authenticator, Cryptographic, etc.). Default value is None.                      |
| technology | The security control technology that the user is interested in.      |    No    | A string acting as security control Technology (e.g. Authenticator, Cryptographic, etc.). Default value is None.                                                                                                                                                     |
| language | The programming language that the user is interested in employing for their purpose.    |    No    | One of the following string values: Java, Python. Default value is None.                                                                                                                                                                          |

The output of the Security Patterns web service is a JSON file containing the information that the user requested. The JSON file contains the security requirement, the security pattern(s) of the aforementioned requirement, the security control technology(ies) of the corresponding security pattern(s) and the corresponding libraries all accompanied by descriptions, characteristics, online resources and other useful information. It should be noted that the requirement parameter is necessary. Thus, it should be provided by the user otherwise no results will be returned. If no values are given for all the rest of the parameters, all results related to that particular requirement will be presented. The produced files are usually very long especially for the case that the user selects a requirement without specifying any other parameter. By setting the value of the language parameter to ”Java” or “Python” the user narrows down the libraries that will be returned to those designed only for Java or Python respectively.

For better understanding, an example is presented demonstrating how the Security Patterns web service can be invoked through a curl command. In the given example, we set the following parameters:

- **requirement**: Authentication

- **pattern**: Authenticator

- **technology**: OAuth2.0

- **language**: Java

Hence, the following HTTP GET Request needs to be submitted:

```
http://160.40.53.132:5000/DataBase?requirement=Authentication&pattern=Authenticator&technology=OAuth2.0&language=Java
```

After submitting the request, the Security Patterns service is invoked. In brief, the service selects the “Authentication” security requirement, the “Authenticator” security pattern, the “OAuth2.0” security control technology and “Java” programming language and returns all the relevant information. After the successful execution of the analysis, a JSON report with the results is produced and sent as a response to the user. The produced JSON for the above example is presented below.

```
{
   "requirement name":"Authentication",
   "_id":"61dd5c88c43a7d33907484b2",
   "description":"The system must validate the identity of its externals before interacting with them. Customers' identities must be authenticated in order to prevent unauthorized access.",
   "standard":"ISO 27001",
   "patterns":{
      "pattern name":"Authenticator",
      "_id":"61dd5cefc43a7d33907484b7",
      "description":"The Authenticator pattern describes a general mechanism for providing identification and authentication to a server from a client. It has the added feature of allowing protocol negotiation to take place using the same procedures. The pattern operates by offering an authentication negotiation object which then provides the protected object only after authentication is successful.",
      "pattern type":"design pattern",
      "technologies":[
         {
            "_id":"61dd5d46c43a7d33907484c2",
            "technology name":"OAuth2.0",
            "description":"OAuth 2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity while providing specific authorization flows for web applications, desktop applications, mobile phones, and living room devices. This specification and its extensions are being developed within the IETF OAuth Working Group.",
            "strength":"",
            "related_security_libraries":[
               {
                  "_id":"61dd5e10c43a7d33907484c9",
                  "library name":"Spring Security",
                  "language":"Java",
                  "resource":[
                     "https://spring.io/projects/spring-security",
                     "https://github.com/spring-projects/spring-security"
                  ],
                  "guidelines":[
                     "https://google",
                     "https://youtube"
                  ],
                  "code examples":[
                     
                  ]
               },
               {
                  "_id":"61dd5e10c43a7d33907484ca",
                  "library name":"Google Auth",
                  "language":"Java",
                  "resource":[
                     "https://github.com/googleapis/google-auth-library-java"
                  ],
                  "guidelines":[
                     "https://google",
                     "https://youtube"
                  ],
                  "code examples":[
                     {
                        "description":"This example shows how you can add the \u2026",
                        "code":"public void \u2026.\n \n"
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

As can be seen above, the JSON object consists of five main elements, which are listed below:

- **requirement name**: which is the main security requirement that the user is interested in (in this case “Authentication”).

- **id**: which is the id number of this particular requirement as it is stored in the mongo database (in this case “61dd5c88c43a7d33907484b2”).

- **description**: which is the requirement’s basic description (in this case “The system must validate the identity of its externals before interacting with them. Customers' identities must be authenticated in order to prevent unauthorized access.”).

- **standard**: which is the standard that the requirement has been extracted from (in this case "ISO 27001"). 

- **patterns**: which contains all related security patterns to that specific security requirement or the specific security pattern that the user requested (in this case “Authenticator”).

Accordingly to the requirement, the information regarding the patterns, technologies and libraries can be seen in the JSON file.

Another example is presented below where only two parameters are specified in case the user is interested in a particular requirement that will be processed in a specific programming language. In this case, the user needs to be informed of all potential security patterns and control technologies that can be put in practice. The parameters for this example are shown below:

- **requirement**: Authentication

- **language**: Java

The following HTTP GET Request needs to be submitted:

```
http://160.40.53.132:5000/DataBase?requirement=Authentication&language=Java
```

After submitting the request, the Security Patterns service returns the following JSON report with the results: 

```
{
   "requirement name":"Authentication",
   "_id":"61dd5c88c43a7d33907484b2",
   "description":"The system must validate the identity of its externals before interacting with them. Customers' identities must be authenticated in order to prevent unauthorized access.",
   "standard":"ISO 27001",
   "patterns":[
      {
         "pattern name":"Authenticator",
         "_id":"61dd5cefc43a7d33907484b7",
         "description":"The Authenticator pattern describes a general mechanism for providing identification and authentication to a server from a client. It has the added feature of allowing protocol negotiation to take place using the same procedures. The pattern operates by offering an authentication negotiation object which then provides the protected object only after authentication is successful.",
         "pattern type":"design pattern",
         "technologies":[
            {
               "_id":"61dd5d46c43a7d33907484c0",
               "technology name":"Basic Authentication",
               "description":"",
               "strength":"",
               "related_security_libraries":[
                  {
                     "_id":"61dd5e10c43a7d33907484c9",
                     "library name":"Spring Security",
                     "language":"Java",
                     "resource":[
                        "https://spring.io/projects/spring-security",
                        "https://github.com/spring-projects/spring-security"
                     ],
                     "guidelines":[
                        "https://www.youtube.com/watch?v=her_7pa0vrg&ab_channel=Amigoscode"
                     ],
                     "code examples":[
                        
                     ]
                  }
               ]
            },
            {
               "_id":"61dd5d46c43a7d33907484c1",
               "technology name":"OAuth1.0",
               "description":"OAuth 2.1 is an in-progress effort to consolidate and simplify the most commonly used features of OAuth 2.0.",
               "strength":"",
               "related_security_libraries":[
                  {
                     "_id":"61dd5e10c43a7d33907484c9",
                     "library name":"Spring Security",
                     "language":"Java",
                     "resource":[
                        "https://spring.io/projects/spring-security",
                        "https://github.com/spring-projects/spring-security"
                     ],
                     "guidelines":[
                        "https://www.youtube.com/watch?v=her_7pa0vrg&ab_channel=Amigoscode"
                     ],
                     "code examples":[
                        
                     ]
                  }
               ]
            },
            {
               "_id":"61dd5d46c43a7d33907484c2",
               "technology name":"OAuth2.0",
               "description":"OAuth 2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity while providing specific authorization flows for web applications, desktop applications, mobile phones, and living room devices. This specification and its extensions are being developed within the IETF OAuth Working Group.",
               "strength":"",
               "related_security_libraries":[
                  {
                     "_id":"61dd5e10c43a7d33907484c9",
                     "library name":"Spring Security",
                     "language":"Java",
                     "resource":[
                        "https://spring.io/projects/spring-security",
                        "https://github.com/spring-projects/spring-security"
                     ],
                     "guidelines":[
                        "https://www.youtube.com/watch?v=her_7pa0vrg&ab_channel=Amigoscode"
                     ],
                     "code examples":[
                        
                     ]
                  },
                  {
                     "_id":"61dd5e10c43a7d33907484ca",
                     "library name":"Google Auth",
                     "language":"Java",
                     "resource":[
                        "https://github.com/googleapis/google-auth-library-java"
                     ],
                     "guidelines":[
                        "https://google",
                        "https://youtube"
                     ],
                     "code examples":[
                        {
                           "description":"This example shows how you can add the \u2026",
                           "code":"public void \u2026.\n \n"
                        }
                     ]
                  }
               ]
            },
            {
               "_id":"61dd5d46c43a7d33907484c4",
               "technology name":"Two Factor Authentication",
               "description":"",
               "strength":"",
               "related_security_libraries":[
                  {
                     "_id":"61dd5e10c43a7d33907484c9",
                     "library name":"Spring Security",
                     "language":"Java",
                     "resource":[
                        "https://spring.io/projects/spring-security",
                        "https://github.com/spring-projects/spring-security"
                     ],
                     "guidelines":[
                        "https://www.youtube.com/watch?v=her_7pa0vrg&ab_channel=Amigoscode"
                     ],
                     "code examples":[
                        
                     ]
                  }
               ]
            }
         ]
      }
   ]
}
```

As can be seen above, in this case all security patterns and control technologies related to Authentication are presented to the user, along with all the corresponding detailed information. In addition, all libraries associated with the aforementioned control technologies are presented but only those supported by Java programming language, as the user requested.

Please note that the database containing all the information that the Security Patterns service extracts, is continuously updated and enriched. Fields that are currently empty will be gradually filled in the near future. 





