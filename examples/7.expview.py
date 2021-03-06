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
import sys
sys.path.insert(0,"../")
from thexp import __VERSION__
print(__VERSION__)

from thexp.frame import ExperimentViewer
from datetime import timedelta
import pprint as pp
expview = ExperimentViewer()
pp.pprint(expview.list())
pp.pprint(expview.recent(timedeltaobj=timedelta(minutes=20)))
pp.pprint(expview.backtracking("ckpt"))
# pp.pprint(expview.exp_code("20-03-08121413"))
# pp.pprint(expview.exp_info("20-03-08122447"))