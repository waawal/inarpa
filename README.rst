
inarpa (ipv4)
==========================

The module exposes the ``create`` function which takes a ipv4-address and optionally a suffix.

Example
-------
::

    >>> import inarpa
    
    >>> inarpa.create('192.168.0.1')
    '1.0.168.192.in-addr.arpa'
    >>> inarpa.create('192.168.0.1', 'ix.dnsbl.manitu.net')
    '1.0.168.192.ix.dnsbl.manitu.net'

Installation
-----------------------------

Install inarpa with ``pip install inarpa`` or just `download inarpa.py <http://pypi.python.org/pypi/inarpa>`_ and place it in your project directory.

License
-------
`BSD <http://www.linfo.org/bsdlicense.html>`_
