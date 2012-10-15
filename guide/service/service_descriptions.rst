====================
Service Descriptions
====================

Guzzle allows you to create commands for your web service client based on a document called a service description. As seen in :doc:`Building Web Service Clients </tour/building_services>`, Guzzle web service clients execute commands on a web service. Service descriptions make it easy to define a web service that can be consumed directly by a Guzzle client or used to produce documentation. Service description based clients are encouraged over creating concrete commands for every web service operation.

Creating a service description
------------------------------

Service descriptions can be representing using a PHP array or JSON document. Guzzle's service descriptions are heavily inspired by `Swagger <http://swagger.wordnik.com/>`_.

Let's say you're interacting with a web service called 'Foo' that allows for the following routes and methods::

    GET/POST   /users
    GET/DELETE /users/:id

The following JSON service description implements this simple web service:

.. code-block:: javascript

    {
        "name": "Foo",
        "apiVersion": "2012-10-14",
        "baseUrl": "http://api.foo.com",
        "description": "Foo is an API that allows you to Baz Bar",
        "operations": {
            "GetUsers": {
                "httpMethod": "GET",
                "uri": "/users",
                "summary": "Gets a list of users",
                "responseClass": "GetUsersOutput"
            },
            "CreateUser": {
                "httpMethod": "POST",
                "uri": "/users",
                "summary": "Creates a new user",
                "responseClass": "CreateUserOutput",
                "parameters": {
                    "name": {
                        "location": "json",
                        "type": "string"
                    },
                    "age": {
                        "location": "json",
                        "type": "integer"
                    }
                }
            },
            "GetUser": {
                "httpMethod": "GET",
                "uri": "/users/{id}",
                "summary": "Retrieves a single user",
                "responseClass": "GetUserOutput",
                "parameters": {
                    "id": {
                        "location": "uri",
                        "description": "User to retrieve by ID",
                        "required": "true"
                    }
                }
            },
            "DeleteUser": {
                "httpMethod": "DELETE",
                "uri": "/users/{id}",
                "summary": "Deletes a user",
                "responseClass": "DeleteUserOutput",
                "parameters": {
                    "id": {
                        "location": "uri",
                        "description": "User to delete by ID",
                        "required": "true"
                    }
                }
            }
        },
        "models": {
            "GetUsersOutput": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "location": "json",
                            "type": "string"
                        },
                        "age": {
                            "location": "json",
                            "type": "integer"
                        }
                    }
                }
            },
            "CreateUserOutput": {
                "type": "object",
                "properties": {
                    "id": {
                        "location": "json",
                        "type": "string"
                    },
                    "location": {
                        "location": "header",
                        "sentAs": "Location",
                        "type": "string"
                    }
                }
            },
            "GetUserOutput": {
                "type": "object",
                "properties": {
                    "name": {
                        "location": "json",
                        "type": "string"
                    },
                    "age": {
                        "location": "json",
                        "type": "integer"
                    }
                }
            },
            "DeleteUserOutput": {
                "type": "object",
                "properties": {
                    "status": {
                        "location": "statusCode",
                        "type": "integer"
                    }
                }
            }
        }
    }

If you attach this service description to a client, you would completely configure the client to interact with the Foo web service and provide valuable response models for each operation.

.. code-block:: php

    use Guzzle\Service\Description\ServiceDescription;

    $description = ServiceDescription::factory('/path/to/client.json');
    $client->setDescription($description);

    $command = $client->getCommand('DeleteUser', array('id' => 123));
    $responseModel = $client->execute($command);
    echo $responseModel['status'];

.. note::

    You can add the service description to your client's factory method or constructor.

Service description attributes
------------------------------

Service descriptions are comprised of the following top-level attributes:

+------------------+-----------------------------------------------------------------------------------------------------------------------+
| Attribute        | Description                                                                                                           |
+==================+=======================================================================================================================+
| name             | (optional) Name of the web service                                                                                    |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| apiVersion       | (optional) Version identifier that the service description is compatible with                                         |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| baseUrl/basePath | (optional) base URL of the service. Any relative URI in an operation will extend from the baseUrl                     |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| description      | Short summary of the web service                                                                                      |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| operations       | Hash of operations of the service. The key is the name of the operation and value is the attributes of the operation. |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| models           | Hash of models used by the service represented in JSON Schema format                                                  |
+------------------+-----------------------------------------------------------------------------------------------------------------------+

baseUrl
~~~~~~~

The ``baseUrl`` attribute, aliased also as ``basePath``, can be used to add a custom baseUrl to a client when the service description is associated with the client. Some clients require custom logic to determine the baseUrl. In those cases, it is best to not include a baseUrl in the service description, but rather allow the factory method of the client to configure the client's baseUrl.

Any operation using a relative URI (e.g. /foo, baz/bar) will generate a URL that extends from the baseUrl attribute of the service description.

operations
~~~~~~~~~~

Operations are the actions that can be taken on a service. Each operation has a distinct endpoint and HTTP method. Operations are created and referenced by name. For example, if an API has a ``DELETE /users/:id`` operation, a satisfactory operation name might be ``DeleteUser`` with a parameter of ``id`` that is inserted into the URI.

Operations are comprised of the following attributes:

+------------------+-----------------------------------------------------------------------------------------------------------------------+
| Attribute        | Description                                                                                                           |
+==================+=======================================================================================================================+
| httpMethod       | (string) HTTP method used with the operation (e.g. GET, POST, PUT, DELETE, PATCH, etc)                                |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| uri              | (string) URI of the operation. The uri attribute can contain URI templates. The variables of the URI template are     |
|                  | parameters of the operation with a location value of ``uri``                                                          |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| class            | (string) Custom class to instantiate instead of the default ``Guzzle\Service\Command\OperationCommand``               |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| responseClass    | (string) This is what is returned from the method. Can be a primitive, PSR-0 compliant class name, or model name.     |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| responseNotes    | (string) Information about the response returned by the operation                                                     |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| responseType     | (string) One of 'primitive', 'class', 'model', or 'documentation'. If not specified, this value will be automatically |
|                  | inferred based on whether or not there is a model matching the name, if a matching PSR-0 compliant class name is      |
|                  | found, or set to 'primitive' by default.                                                                              |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| deprecated       | (bool) Set to true if this is a deprecated operation                                                                  |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| errorResponses   | (array) Errors that could occur when executing the command. Array of hashes, each with a 'code' (the HTTP response    |
|                  | code), 'phrase' (response reason phrase or description of the error), and 'class' (a custom exception class that      |
|                  | would be thrown if the error is encountered).                                                                         |
+------------------+-----------------------------------------------------------------------------------------------------------------------+
| data             | (array) Any extra data that might be used to help build or serialize the operation                                    |
+------------------+-----------------------------------------------------------------------------------------------------------------------+

parameters
^^^^^^^^^^

Parameters in both operations and models are represented using the `JSON schema <http://tools.ietf.org/id/draft-zyp-json-schema-03.html>`_ syntax.


models
~~~~~~

Models are used in service descriptions to provide valuable output to an operation or to share snippets of JSON schemas throughout the service description.
