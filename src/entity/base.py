class Base:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{attr}={getattr(self, attr)!r}" for attr in vars(self) if not attr.startswith('_'))

        return f"{class_name}({attributes})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return all(getattr(self, attr) == getattr(other, attr) for attr in vars(self) if not attr.startswith('_'))

        return False

    def __hash__(self):
        # Implement a custom hash method for instances of this class
        return hash(tuple(sorted(self.__dict__.items())))
