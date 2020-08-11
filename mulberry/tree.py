from .backends.numpy_backend import NumpyBackend

class Tree:
    def __init__(self, backend=NumpyBackend):
        self._backend= backend

        self._keys = set()  # Set of all keys
        self._parents = {}  # Dictionary {child key -> parent key}
        self._transforms = {}  # Dictionary {(from key, to key) -> 4x4 np.array}

    def setTransform(self, transform, from_key, to_key):
        if (from_key, to_key) in self._transforms or (to_key, from_key) in self._transforms:
            self._transforms.pop((to_key, from_key), None)
            self._transforms[(from_key, to_key)] = transform
        else:
            has_from_key = from_key in self._keys
            has_to_key = to_key in self._keys
            if has_from_key and has_to_key:
                # Ensure they're not in the same tree
                raise NotImplementedError  # TODO
            elif has_from_key:
                self._keys.add(to_key)
                self._parents[to_key] = from_key
                self._transforms[(from_key, to_key)] = transform
            elif has_to_key:
                self._keys.add(from_key)
                self._parents[from_key] = to_key
                self._transforms[(from_key, to_key)] = transform

    def _getDirectTransform(self, from_key, to_key):
        ret = self._transforms.get((from_key, to_key), None)
        if ret is not None:
            return ret

        ret = self._transforms.get((to_key, from_key), None)
        if ret is not None:
            return self._backend.invert(ret)

        return None

    def getTransform(self, from_key, to_key):
        ret = _getDirectTransform(from_key, to_key)
        if ret is not None:
            return ret

        raise NotImplementedError  # TODO

