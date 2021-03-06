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

from thexp.frame.meter import Meter,AvgMeter
import torch

def test_meter():
    m = Meter()
    am = AvgMeter()
    for j in range(100):
        for i in range(100):
            m = Meter()
            m.a = 1
            m.b = "2"
            m.c = torch.tensor(3)
            m.c = torch.tensor([4, 5])
            m.d = [4]
            m.e = {5: "6"}
        am.update(m)

