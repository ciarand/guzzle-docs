======================
Plugin system overview
======================

Guzzle ships with a number of plugins that typically deal with the Guzzle\Http namespace.

Any event subscriber attached to the EventDispatcher of a ``Guzzle\Http\Client`` or ``Guzzle\Service\Client``
object will automatically be attached to all request objects created by the client. This allows you to attach, for
example, a HistoryPlugin to a client object, and from that point on, every request sent through that client will
utilize the HistoryPlugin.

Pre-Built plugins
-----------------

Guzzle provides easy to use request plugins that add behavior to requests based on signal slot event notifications
powered by the
`Symfony2 Event Dispatcher component <http://symfony.com/doc/2.0/components/event_dispatcher/introduction.html>`_.

.. include:: plugins-list.rst.inc
