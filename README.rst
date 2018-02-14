Lovely-rita is set of tools for reading, cleaning, and saving parking parking citation datasets.

Functionality
=============

- Load data
- Clean data (addresses and dates)
- Geocode (turn addresses into latitude/longitude coordinates)
- Save cleaned data to shapefiles for GIS analyses

Getting started
===============

.. code-block:: bash

git clone https://github.com/r-b-g-b/lovely-rita.git
cd lovely-rita
pip install . --user

  
Raw data format
===============

Raw data should be provided in a `.csv` with the column names (in any order):

- 'Ticket Issue Time'
- 'Ticket Number'
- 'Street Name'
- 'Violation External Code'
- 'street'
- 'Street No'
- 'Violation Desc Long'
- 'Ticket Issue Date'
- 'state'
- 'city'
- 'Street Suffix'
- 'Badge #'
- 'Fine Amount'


Reading the data
================



Analyses
========
1. Number of citations per zip code
2. Time-series, number of citations
3. Type of violation by zip code

Lovely-Rita: Insights from Oakland Citation Data
================================================

Detailed slides to share here: https://goo.gl/XiUvkB

One Paragraph of project description goes here

Getting Started
===============

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
-------------

What things you need to install the software and how to install them

```
Give examples
```

Reproducibility
---------------

A step by step series of examples that tell you have to get a development env running for reproducible notebooks

Python, Conda, blah blah

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

Running the tests
-----------------

Explain how to run the automated tests for this system

Break down into end to end tests
--------------------------------

Explain what these tests test and why

```
Give an example
```

And coding style tests
----------------------

Explain what these tests test and why

```
Give an example
```

Deployment
----------

Add additional notes about how to deploy this on a live system

Built With
----------

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

Contributing
------------

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

Versioning
----------

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

Authors
-------

* **Team member 1** - *github handlek* - [LinkedIn]()

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

License
-------

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

Acknowledgments
---------------

* Recognize Danielle & Oakland DoT
* etc