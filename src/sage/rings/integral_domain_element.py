"""
Base class for integral domain elements
"""

#*****************************************************************************
#       Copyright (C) 2005 William Stein <wstein@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.structure.element import IntegralDomainElement

def is_IntegralDomainElement(x):
    """
    Check if ``x`` is an element of :class:`IntegralDomainElement`.

    EXAMPLES::

        sage: sage.rings.integral_domain_element.is_IntegralDomainElement(ZZ(2))
        True
    """
    return isinstance(x, IntegralDomainElement)
