# 0-add_integer.txt
# linda shirasala <lindashirasala@gmail.com>

===========================
How to Use 0-add_integer.py
===========================

This module defines an integer addition function ``add_integer(a, b=98)``.

Usage
=====

``add_integer(...)``` returns the addition of its two :x
arguments. For numbers,
that value is equivalent to using the ``+`` operator.

::

    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(2, 3)
    5

    ::

        >>> add_integer(2, -3)
        -1

        The function also works with floating-point values.

        ::

            >>> add_integer(2.0, 3.0)
            5

            Note that floats are casted to ints before addition is performed.

            ::

                 >>> add_integer(2.9, 0.2)
                 2

                 ::

                      >>> add_integer(-2.9, -0.2)
                      -2

                      Floating and non-floating point values can be combined.

                      ::

                          >>> add_integer(2.3, -3)
                          -1

                          The second argument is optional - by default, it is 98.

