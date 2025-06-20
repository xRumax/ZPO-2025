class Memento:
    _states: list
    _i : int

    def __init__(self) -> None:
        self._states = []
        self._i = -1

    def save_state(self, state: str) -> None:
        if self._i != len(self._states) -1:
            self._states = self._states[:self._i + 1]
        
        self._states.append(state)
        self._i += 1

    def undo(self) -> None:
        if self._i > 0:
            self._i -= 1
        else:
            self._i =-1

    def redo(self) -> None:
        if self._i < len(self._states) -1:
            self._i += 1

    def read_state(self) -> str:
        if not self._states or self._i < 0:
            return ""
        return self._states[self._i]
    
