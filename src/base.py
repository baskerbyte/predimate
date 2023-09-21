class Base:
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{attr}={getattr(self, attr)!r}" for attr in vars(self))

        return f"{class_name}({attributes})"