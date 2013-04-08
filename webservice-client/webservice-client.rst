======================
The web service client
======================

The ``Guzzle\Service`` namespace contains various abstractions that help to make it easier to interact with a web
service API, including commands, service descriptions, and resource iterators.

In this chapter, we'll build a simple `Twitter API client <https://dev.twitter.com/docs/api/1.1>`_.

Creating a client
-----------------

A class that extends from ``Guzzle\Service\Client`` or implements ``Guzzle\Service\ClientInterface`` must implement a
``factory()`` method in order to be used with a :doc:`service builder <using-the-service-builder>`.

Factory method
~~~~~~~~~~~~~~

You can use the ``factory()`` method of a client directly if you do not need a service builder.

.. code-block:: php

    use mtdowling\TwitterClient;

    // Create a client and pass an array of configuration data
    $twitter = TwitterClient::factory(array(
        'consumer_key'    => '****',
        'consumer_secret' => '****',
        'token'           => '****',
        'token_secret'    => '****'
    ));

.. note::

    If you'd like to follow along, here's how to get your Twitter API credentials:

    1. Visit https://dev.twitter.com/apps
    2. Click on an application that you've created
    3. Click on the "OAuth tool" tab
    4. Copy all of the settings under "OAuth Settings"

Implementing a factory method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating a client and its factory method is pretty simple. You just need to implement ``Guzzle\Service\ClientInterface``
or extend from ``Guzzle\Service\Client``.

.. code-block:: php

    namespace mtdowling;

    use Guzzle\Common\Collection;
    use Guzzle\Plugin\Oauth\OauthPlugin;
    use Guzzle\Service\Client;
    use Guzzle\Service\Description\ServiceDescription;

    /**
     * A simple Twitter API client
     */
    class TwitterClient extends Client
    {
        public static function factory($config = array())
        {
            // Provide a hash of default client configuration options
            $default = array('base_url' => 'https://api.twitter.com/1.1');

            // The following values are required when creating the client
            $required = array(
                'base_url',
                'consumer_key',
                'consumer_secret',
                'token',
                'token_secret'
            );

            // Merge in default settings and validate the config
            $config = Collection::fromConfig($config, $default, $required);

            // Create a new Twitter client
            $client = new self($config->get('base_url'), $config);

            // Ensure that the OauthPlugin is attached to the client
            $client->addSubscriber(new OauthPlugin($config->toArray()));

            return $client;
        }
    }

Service Builder
~~~~~~~~~~~~~~~

A service builder is used to easily create web service clients, provides a simple configuration driven approach to
creating clients, and allows you to share configuration settings across multiple clients. You can find out more about
Guzzle's service builder in :doc:`using-the-service-builder`.

.. code-block:: php

    use Guzzle\Service\Builder\ServiceBuilder;

    // Create a service builder and provide client configuration data
    $builder = ServiceBuilder::factory('/path/to/client_config.json');

    // Get the client from the service builder by name
    $twitter = $builder->get('twitter');

The above example assumes you have JSON data similar to the following stored in "/path/to/client_config.json":

.. code-block:: json

    {
        "services": {
            "twitter": {
                "class": "mtdowling\TwitterClient",
                "params": {
                    "consumer_key": "****",
                    "consumer_secret": "****",
                    "token": "****",
                    "token_secret": "****"
                }
            }
        }
    }

.. note::

    A service builder becomes much more valuable when using multiple web service clients in a single application or
    if you need to utilize the same client with varying configuration settings (e.g. multiple accounts).

Commands
--------

Commands are a concept in Guzzle that helps to hide the underlying implementation of an API by providing an easy to use
parameter driven object for each action of an API. A command is responsible for accepting an array of configuration
parameters, serializing an HTTP request, and parsing an HTTP response. Following the
`command pattern <http://en.wikipedia.org/wiki/Command_pattern>`_, commands in Guzzle offer a greater level of
flexibility when implementing and utilizing a web service client.

Creating commands
~~~~~~~~~~~~~~~~~

Commands are created using either the ``getCommand()`` method of a client or a magic missing method of a client. Using
the ``getCommand()`` method allows you to create a command without executing it, allowing for customization of the
command or the request serialized by the command.

When a client attempts to create a command, it uses the client's ``Guzzle\Service\Command\Factory\FactoryInterface``.
By default, Guzzle will utilize a command factory that first looks for a concrete class for a particular command
(concrete commands) followed by a command defined by a service description (operation commands). We'll learn more about
concrete commands and operation commands later in this chapter.

.. code-block:: php

    // Get a command from the twitter client.
    $twitter->getCommand('get_mentions');

Unless you've skipped ahead, running the above code will throw an exception.

    PHP Fatal error:  Uncaught exception 'Guzzle\Common\Exception\InvalidArgumentException' with message
    'Command was not found matching get_mentions'

This exception was thrown because the "get_mentions" command has not yet been implemented. Let's implement one now.

Concrete commands
~~~~~~~~~~~~~~~~~



Operation commands
~~~~~~~~~~~~~~~~~~

Executing commands
~~~~~~~~~~~~~~~~~~

Sending commands in parallel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Special command options
~~~~~~~~~~~~~~~~~~~~~~~

Resource iterators
------------------

Advanced client configuration
-----------------------------

Default command parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~

Magic methods
~~~~~~~~~~~~~

Custom command factory
~~~~~~~~~~~~~~~~~~~~~~

Custom resource Iterator factory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
