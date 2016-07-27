Upload
======

A web application that allows users to upload a file to the server. This is obviously a bad idea for a whole host of reasons.

Usage
=====

Requirements
------------

* flask
* flask-wtf

Configuration
-------------

You'll need to create a `config.py` file. A sample configuration file can be found at `sample_config.py`.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To make the server world-accessible or for other options, see `run.py -h`.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

* Form validation (like the password) is done post-upload and waiting to upload only to be defeated by a typo is terrible.

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
