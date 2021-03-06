"""
    Copyright (C) 2020 Shandong University

    This program is licensed under the GNU General Public License 3.0 
    (https://www.gnu.org/licenses/gpl-3.0.html). 
    Any derivative work obtained under this license must be licensed 
    under the GNU General Public License as published by the Free 
    Software Foundation, either Version 3 of the License, or (at your option) 
    any later version, if this derivative work is distributed to a third party.

    The copyright for the program is owned by Shandong University. 
    For commercial projects that require the ability to distribute 
    the code of this program as part of a program that cannot be 
    distributed under the GNU General Public License, please contact 
            
            sailist@outlook.com
             
    to purchase a commercial license.
"""


from thexp.base_classes.trickitems import NoneItem,AvgItem
def test_none_item():
    none = NoneItem()
    assert none > 0
    assert none >= 0
    assert none < 0
    assert none <= 0
    assert none != 0
    assert none == None
    assert none is not None
    assert none/2 == 0.5
    assert none*2 == 2
    assert none+1 == 1
    assert none-1 == -1


def test_avg_item():
    avg = AvgItem()
    avg.update(4)
    avg.update(3)
    avg.update(2)
    assert avg._item == 2
    assert avg.avg == 3
