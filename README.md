OpenTapioca
===========
[![Documentation Status](https://readthedocs.org/projects/opentapioca/badge/?version=latest)](https://opentapioca.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://github.com/wetneb/opentapioca/workflows/CI/badge.svg)](https://github.com/wetneb/opentapioca/actions) [![Coverage Status](https://coveralls.io/repos/github/wetneb/opentapioca/badge.svg)](https://coveralls.io/github/wetneb/opentapioca)

OpenTapioca is a simple and fast [Named Entity Linking system](https://en.wikipedia.org/wiki/Entity_linking) for [Wikidata](https://www.wikidata.org/). It is kept synchronous with Wikidata in real time, encouraging users to improve the results of their entity linking
tasks by contributing back to Wikidata.

A live instance is running at https://opentapioca.org/. To run it on a server that is powerful enough, I would need 50€/month: [please help fund the service if you can](https://en.liberapay.com/OpenTapioca).

A [NIF endpoint](https://github.com/dice-group/gerbil/wiki/How-to-create-a-NIF-based-web-service) is available at:
* https://opentapioca.org/api/nif (only exposing the matches that are deemed good enough)
* https://opentapioca.org/api/nif?only_matching=false (also exposing all the other matches regardless of their score)

See [the docs](https://opentapioca.readthedocs.io/en/latest/) for more information about how it works and how to run it. See [the paper](https://arxiv.org/abs/1904.09131) for some more motivation about the design of the system.

OpenTapioca is released under the Apache-2.0 license.
--------------------------------------

When working in a virtual environment, it's common to have your Python dependencies and project-specific files contained within that virtual environment. To save your work and be able to continue it later, you have a few options:
Option 1: Saving the Entire Virtual Environment

    Freeze Requirements:
        While your virtual environment is active, you can freeze the installed Python packages to a requirements.txt file. Run the following command in your virtual environment:

        bash

    pip freeze > requirements.txt

Save the Entire Virtual Environment:

    Copy the entire virtual environment folder to a safe location. This includes the venv directory (or whatever you named it).

Restore the Virtual Environment:

    To continue your work later, you can create a new virtual environment and install the dependencies using the requirements.txt file:

    bash

python -m venv venv
venv\Scripts\activate  # Activate the virtual environment
pip install -r requirements.txt

