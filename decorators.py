"""A place that all my future decorators will live
"""

from icecream import ic


def frozen(cla):
    """A class decorator that freezes the class.  An error is raised if an attribute is assigned
    outside of __init__
    """
    cla.__frozen = False
    def frozen_setattr(self, key, value):
        if self.__frozen and not hasattr(self, key):
            raise TypeError(f'{self} is frozen, attributes cannot be added.')
        else:
            object.__setattr__(self, key, value)

    def init_wrapper(init):
        def frozen_init2(self):
            init(self)
            self.__frozen = True
        return frozen_init2

    cla.__setattr__ = frozen_setattr
    cla.__init__ = init_wrapper(cla.__init__)
    return cla


if __name__ == '__main__':
    # Example use case
    @frozen
    class data():
        def __init__(self):
            self.x = [1,2,3]
            self.y = 5

    x = data()
    y = data()
    x.y = 6
    x.z = 6  # Raises error
    breakpoint()
