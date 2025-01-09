:layout: landing
:description: Falco is an opinionated toolkit for a modern Django development experience.

.. container::
    :name: home-head

    .. image:: /_static/falco-logo.svg
        :alt: Falco
        :width: 350
    

    .. container::

        .. raw:: html

            <h1>Falco</h1>
            <h2>An opinionated toolkit for building web apps faster with Django</h2>

        .. container:: badges
           :name: badges

           .. image:: https://badge.fury.io/py/falco-app.svg
              :alt: PyPI Version

           .. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json
              :alt: UV

           .. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
              :alt: Ruff Version

           .. image:: https://img.shields.io/badge/license-MIT-blue.svg
              :alt: MIT License

           .. image:: https://img.shields.io/pypi/pyversions/falco-app
              :alt: Supported Python Versions

           .. image:: https://img.shields.io/pypi/frameworkversions/django/falco-app
              :alt: Supported Django Versions

           .. image:: https://img.shields.io/pypi/dm/falco-cli
              :alt: PyPI Downloads

           .. image:: https://readthedocs.org/projects/falco-site/badge/?version=latest&style=flat
              :alt: Documentation Status

.. rst-class:: lead

    Falco is your Django toolkit for faster prototyping and deployment of your Django projects. It offers commands for `project generation <https://github.com/falcopackages/falco-cli#start-project>`_,
    `CRUD view generation <https://falco-app.readthedocs.com/crud>`_, :doc:`guides <guides/index>` that address common web development challenges tailored to Django and much more.

.. container:: buttons

    `Getting Started <https://template.falcoproject.com/en/latest/getting_started.html>`_
    `GitHub <https://github.com/falcopackages>`_

.. grid:: 1 1 2 3
    :class-row: surface
    :padding: 0
    :gutter: 2

    .. grid-item-card:: :octicon:`terminal` CLI
      :link: https://github.com/falcopackages/falco-cli

      The documentation for the falco command line interface (CLI).

    .. grid-item-card:: :octicon:`repo-template` Starter Template
      :link: https://template.falcoproject.com

      The starter template for new Django projects using Falco.

    .. grid-item-card:: :octicon:`package` Application
      :link: https://app.falcoproject.com

      Set of custom commands and utilities to improve your developer experience.

    .. grid-item-card:: :octicon:`book` Guides
      :link: guides/index
      :link-type: doc

      A collection of guides on common web development topics and how to address them in django.

    .. grid-item-card:: :octicon:`comment-discussion` Discussion
      :link: https://github.com/tobi-de/falco/discussions

      Provide suggestions for improving the guides and share new ideas.

    .. grid-item-card:: :octicon:`people` Contributing
      :link: contributing
      :link-type: doc

      Learn how to contribute to the Falco project.

-----

.. raw:: html

    <h2>Contributors</h2>

.. include:: ../README.md
    :parser: myst_parser.sphinx_
    :start-after: <!-- contributors:start -->
    :end-before: <!-- contributors:end -->

.. toctree::
    :caption: Getting started
    :hidden:

    quickstart
    Template <https://template.falcoproject.com>
    App <https://app.falcoproject.com>
    CLI <https://github.com/falcopackages/falco-cli>
    guides/index

.. toctree::
    :caption: Development
    :hidden:

    contributing
    codeofconduct
    license
    changelog
