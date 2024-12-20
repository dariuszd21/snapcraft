.. _example-flutter-app:

Example Flutter app
===================

This how-to guide covers the steps, decisions, and implementation details that
are unique when crafting a snap of an app built using GTK4 and GNOME. We'll
work through the aspects unique to GTK4-based apps by examining an existing
recipe.


Example Flutter app recipe
--------------------------

The following code comprises the recipe of a simple Flutter project,
`my-flutter-app <https://github.com/snapcraft-docs/my-flutter-app>`_. This
project is merely a demonstration of a clicker window for GNOME.

.. collapse:: Flutter app recipe

  .. literalinclude:: ../code/craft-for-platforms/example-flutter-recipe.yaml
    :language: yaml
    :lines: 2-


Add an app written for Flutter
------------------------------

.. literalinclude:: ../code/craft-for-platforms/example-flutter-recipe.yaml
  :language: yaml
  :start-at: parts:
  :end-at: flutter-target: lib/main.dart

Flutter parts are built with the `flutter plugin
<https://snapcraft.io/docs/flutter-plugin>`_.

To add a Flutter part:

#. Declare the general part keys, such as ``source``, ``override-build``,
   ``build-packages``, and so on.
#. Set ``plugin: flutter``.
#. If the part is the main app, set ``flutter-target`` to the location of the
   project's ``main.dart`` file.
