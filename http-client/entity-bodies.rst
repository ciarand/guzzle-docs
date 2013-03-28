===========================
Request and response bodies
===========================

`Entity body <http://www.w3.org/Protocols/rfc2616/rfc2616-sec7.html>`_ is the term used for the body of an HTTP
message. The entity body of requests and responses is inherently a
`PHP stream <http://php.net/manual/en/book.stream.php>`_ in Guzzle. The body of the request can be either a string or
a PHP stream which are converted into a ``Guzzle\Http\EntityBody`` object using its factory method. When using a
string, the entity body is stored in a `temp PHP stream <http://www.php.net/manual/en/wrappers.php.php>`_. The use of
temp PHP streams helps to protect your application from running out of memory when sending or receiving large entity
bodies in your messages. When more than 2MB of data is stored in a temp stream, it automatically stores the data on
disk rather than in memory.

EntityBody objects provide a great deal of functionality: compression, decompression, calculate the Content-MD5,
calculate the Content-Length (when the resource is repeatable), guessing the Content-Type, and more. Guzzle doesn't
need to load an entire entity body into a string when sending or retrieving data; entity bodies are streamed when
being uploaded and downloaded.

Here's an example of gzip compressing a text file then sending the file to a URL:

.. code-block:: php

    use Guzzle\Http\EntityBody;

    $body = EntityBody::factory(fopen('/path/to/file.txt', 'r'));
    $body->compress();
    $response = $client->put('http://localhost:8080/uploads', null, $body)->send();

The body of the request can be specified in the ``Client::put()`` or ``Client::post()``  method, or, you can specify
the body of the request by calling the ``setBody()`` method of any
``Guzzle\Http\Message\EntityEnclosingRequestInterface`` object.

The entity body received from a response is stored in a temp stream by default. If you need the entity body of a
response to use a destination other than a temporary stream (e.g. FTP, HTTP, a specific file, an open stream), you can
set the entity body object that will be used to hold the response body by calling ``setResponseBody()`` on any request
object.
