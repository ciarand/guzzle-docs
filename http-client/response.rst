======================
Using Response objects
======================

Sending a request will return a ``Guzzle\Http\Message\Response`` object. You can view the HTTP response message by
casting the Response object to a string. Casting the response to a string will return the entity body of the response
as a string too, so this might be an expensive operation if the entity body is stored in a file or network stream. If
you only want to see the response headers, you can call ``getRawHeaders()``.

The Response object contains helper methods for retrieving common response headers. These helper methods normalize the
variations of HTTP response headers.

.. code-block:: php

    $response->getContentMd5();
    $response->getEtag();
    $response->getCacheControl();
    $response->getHeader('Content-Length');
    // ... There are methods for every known response header

The entity body object of a response can be retrieved by calling ``$response->getBody()``. The response EntityBody can
be cast to a string, or you can pass ``true`` to this method to retrieve the body as a string.

JSON Responses
^^^^^^^^^^^^^^

You can easily parse and use a JSON response as an array using the ``json()`` method of a response. This method will
always return an array if the response is valid JSON or if the response body is empty. You will get an exception if you
call this method and the response is not valid JSON.

.. code-block:: php

    $data = $response->json();
    echo gettype($data);
    // >>> array

XML Responses
^^^^^^^^^^^^^

You can easily parse and use a XML response as SimpleXMLElement object using the ``xml()`` method of a response. This
method will always return a SimpleXMLElement object if the response is valid XML or if the response body is empty. You
will get an exception if you call this method and the response is not valid XML.

.. code-block:: php

    $xml = $response->xml();
    echo $xml->foo;
    // >>> Bar!
