"""Functions to generate Collatz sequences"""

from typing import Dict, List, Optional

import networkx as nx


class CollatzSequences:
    # pylint: disable=too-few-public-methods
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring

    def __init__(self, start: int, end: int) -> None:
        if start < 1:
            raise ValueError("Start must be positive!")
        if not start < end:
            raise ValueError("End must be greater than or equal to start!")

        self._start = start
        self._end = end
        self._next_cached: Dict[int, int] = {1: 4, 4: 2, 2: 1}
        self._sequences: Dict[int, List[int]] = {}
        self._graph: Optional[nx.DiGraph] = None
        self._compute_pairs()
        self._compute_sequences()

    @property
    def sequences(self) -> Dict[int, list]:
        return self._sequences

    @property
    def graph(self) -> nx.DiGraph:
        return self._as_graph()

    @staticmethod
    def _next(n: int) -> int:
        return n * 3 + 1 if n % 2 == 1 else n // 2

    def _compute_pairs(self):
        for initial_value in range(self._start, self._end):
            n = initial_value
            while True:
                if n in self._next_cached:
                    # NOTE: if n is already in self._next_cached, the rest of this path has
                    #       already been computed and cached in self._next_cached
                    break
                next_value = self._next(n)
                self._next_cached[n] = next_value
                n = next_value

    def _sequence(self, initial_value: int) -> List[int]:
        n = initial_value
        sequence = [n]
        while n != 1:
            n = self._next_cached[n]
            if n in self._sequences:
                # NOTE: if a sequence starting from n is already in self._sequences,
                #       the rest could be just copied from there.
                return sequence + self._sequences[n]
            sequence.append(n)
        return sequence

    def _compute_sequences(self):
        for n in range(self._start, self._end):
            self._sequences[n] = self._sequence(n)

    def _as_graph(self) -> nx.DiGraph:
        if self._graph is None:
            self._graph = nx.DiGraph()
            for key, value in self._next_cached.items():
                self._graph.add_edge(key, value)
        return self._graph
