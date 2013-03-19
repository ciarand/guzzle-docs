============
Installation
============

Requirements
------------

#. PHP 5.3.3+ compiled with the cURL extension
#. A recent version of cURL 7.16.2+ compiled with OpenSSL and zlib

Installing Guzzle
-----------------

Composer
~~~~~~~~

The recommneded way to install Guzzle is with `Composer <http://getcomposer.org>`_. Composer is a dependency
management tool for PHP that allows you to declare the dependencies your project needs and installs them into your
project. In order to use Guzzle with Composer, you must do the following:

#. Add ``"guzzle/guzzle"`` as a dependency in your project's ``composer.json`` file.

   .. code-block:: js

       {
           "require": {
               "guzzle/guzzle": "3.3.*"
           }
       }

#. Download and install Composer.

   .. code-block:: sh

       curl -s "http://getcomposer.org/installer" | php

#. Install your dependencies.

   .. code-block:: sh

       php composer.phar install

#. Require Composer's autoloader.

   Composer also prepares an autoload file that's capable of autoloading all of the classes in any of the libraries
   that it downloads. To use it, just add the following line to your code's bootstrap process.

   .. code-block:: php

       require __DIR__ . '/vendor/autoload.php';

You can find out more on how to install Composer, configure autoloading, and other best-practices for defining
dependencies at `getcomposer.org <http://getcomposer.org>`_.

During your development, you can keep up with the latest changes on the master branch by setting the version
requirement for Guzzle to ``dev-master``.

.. code-block:: js

   {
      "require": {
         "guzzle/guzzle": "dev-master"
      }
   }

PEAR
~~~~

Guzzle can be installed through PEAR:

.. code-block:: bash

    pear channel-discover guzzlephp.org/pear
    pear install guzzle/guzzle

You can install a specific version of Guzzle by providing a version number suffix:

.. code-block:: bash

    pearch install guzzle/guzzle-3.3.1

Contributing to Guzzle
----------------------

In order to contribute, you'll need to checkout the source from GitHub and install Guzzle's dependencies using
Composer:

.. code-block:: bash

    git clone https://github.com/guzzle/guzzle.git
    cd guzzle && curl -s http://getcomposer.org/installer | php && ./composer.phar install --dev

Guzzle is unit tested with PHPUnit. You will need to create your own phpunit.xml file in order to run the unit tests
(or just copy phpunit.xml.dist to phpunit.xml). Run the tests using the vendored PHPUnit binary:

.. code-block:: bash

    vendor/bin/phpunit

You'll need to install node.js v0.5.0 or newer in order to test the cURL implementation.

Framework integrations
----------------------

Using Guzzle with Symfony
~~~~~~~~~~~~~~~~~~~~~~~~~

A `Guzzle Symfony2 bundle <https://github.com/ddeboer/GuzzleBundle>`_ is available on github thanks to
`ddeboer <https://github.com/ddeboer>`_

Using Guzzle with Silex
~~~~~~~~~~~~~~~~~~~~~~~

A `Guzzle Silex service provider <https://github.com/guzzle/guzzle-silex-extension>`_ is available on github.
