===========
``alexapy``
===========

.. automodule:: alexapy

   .. contents::
      :local:


Submodules
==========

.. toctree::

   alexapy.alexaapi
   alexapy.alexahttp2
   alexapy.alexalogin
   alexapy.alexaproxy
   alexapy.alexawebsocket
   alexapy.const
   alexapy.errors
   alexapy.helpers

.. currentmodule:: alexapy


Functions
=========

- :py:func:`hide_email`:
  Obfuscate email.

- :py:func:`hide_serial`:
  Obfuscate serial.

- :py:func:`obfuscate`:
  Obfuscate email, password, and other known sensitive keys.


.. autofunction:: hide_email

.. autofunction:: hide_serial

.. autofunction:: obfuscate


Classes
=======

- :py:class:`AlexaLogin`:
  Class to handle login connection to Alexa. This class will not reconnect.

- :py:class:`AlexaAPI`:
  Class for accessing a specific Alexa device using rest API.

- :py:class:`AlexaProxy`:
  Class to handle proxy login connections to Alexa.

- :py:class:`HTTP2EchoClient`:
  HTTP2 Client Class for Echo Devices.

- :py:class:`WebsocketEchoClient`:
  WebSocket Client Class for Echo Devices.


.. autoclass:: AlexaLogin
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexaLogin
      :parts: 1

.. autoclass:: AlexaAPI
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexaAPI
      :parts: 1

.. autoclass:: AlexaProxy
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexaProxy
      :parts: 1

.. autoclass:: HTTP2EchoClient
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HTTP2EchoClient
      :parts: 1

.. autoclass:: WebsocketEchoClient
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WebsocketEchoClient
      :parts: 1


Exceptions
==========

- :py:exc:`AlexapyConnectionError`:
  Define an error related to invalid requests.

- :py:exc:`AlexapyLoginCloseRequested`:
  Define an error related to requesting access to API after requested close.

- :py:exc:`AlexapyLoginError`:
  Define an error related to no longer being logged in.

- :py:exc:`AlexapyPyotpInvalidKey`:
  Define an error related to invalid 2FA key.


.. autoexception:: AlexapyConnectionError

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexapyConnectionError
      :parts: 1

.. autoexception:: AlexapyLoginCloseRequested

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexapyLoginCloseRequested
      :parts: 1

.. autoexception:: AlexapyLoginError

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexapyLoginError
      :parts: 1

.. autoexception:: AlexapyPyotpInvalidKey

   .. rubric:: Inheritance
   .. inheritance-diagram:: AlexapyPyotpInvalidKey
      :parts: 1
