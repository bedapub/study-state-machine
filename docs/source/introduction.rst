===============
Getting Started
===============

The State Machine is used to implement a workflow. Through a transition you change from one state to another. The
current state determines the behavior.

Context
=======
The :class:`~state_machine.context.Context` serves as an interface between the state machine and the client . It
delegates a request from the client to the current state. Depending on the current state, the request results in a
different behavior.

The following example shows how to create a context and load a state by its name:

.. code-block:: python

    from state_machine.context import Context

    context = Context()
    context.load_state("BiokitUploadState")
    context.change_state()

State
=====
Each state is modeled as a class and implements a set of behaviors. All states inherit from the abstract
:class:`~state_machine.interfaces.IState`.

A list with all existing states can be obtained as follows:

.. code-block:: python

    from state_machine.context import Context

    context = Context()
    name, cls = context.available_states

Study States
============
A Study state must be inherited from :class:`~state_machine.interfaces.IStudyState` instead of IState. All study states
are implemented in the package :py:mod:`~state_machine.study_states`.

**Note**: The name of a state is derived from its class name (see :py:mod:`state_machine.study_states.__init__`).
Therefore, it can lead to an exception if the class name of a state is changed.
