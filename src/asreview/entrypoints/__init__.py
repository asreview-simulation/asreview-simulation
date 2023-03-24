from ._algorithms_entrypoint import AlgorithmsEntrypoint
from ._base_entrypoint import BaseEntrypoint
from ._lab_entrypoint import LabEntrypoint
from ._simulate_entrypoint import SimulateEntrypoint
from ._state_inspect_entrypoint import StateInspectEntrypoint


def list_entrypoints():
    entrypoints = [
        AlgorithmsEntrypoint,
        LabEntrypoint,
        SimulateEntrypoint,
        StateInspectEntrypoint
    ]
    return {e.name: e for e in entrypoints}


del _algorithms_entrypoint
del _base_entrypoint
del _lab_entrypoint
del _simulate_entrypoint
del _state_inspect_entrypoint
