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
    context.load_state("RegisteredState")
    context.change_state()

State
=====
Each state is modeled as a JSON document with two set of strategies (create_study and change_state) that dictates a set of behaviors.

The existing states need to be passed to the context. Here is an example:

.. code-block:: json

    {
        "name" : "RegisteredState",
        "strategies_create_study" : [ 
            {
                "name" : "expression",
                "value" : "len(kwargs.get('datasets', [])) > 0",
                "state_if_true" : "DatasetState"
            }
        ],
        "strategies_change_state" : [ 
            {
                "name" : "expression",
                "value" : "len(kwargs.get('datasets', [])) > 0",
                "state_if_true" : "DatasetState"
            }
        ]
    }
