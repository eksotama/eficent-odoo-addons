# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent
#    (<http://www.eficent.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "HR Timesheet Analysis by WBS",
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
HR Timesheet Analysis by WBS
=====================================
This module will allow you to execute the timesheet analysis report being
able to:
* Group by the Parent Project
* Search by the Parent Project



Installation
============


Configuration
=============

Usage
=====

Known issues / Roadmap
======================

Credits
=======
* Eficent, www.eficent.com

Contributors
------------

* Jordi Ballester Alomar <jordi.ballester@eficent.com>
""",
    'author': "Eficent",
    'website': 'http://www.eficent.com',
    'license': 'AGPL-3',
    "depends": ['hr_timesheet_sheet', 'project_wbs'],
    "data": [
        'report/hr_timesheet_report_view.xml',
        'report/timesheet_report_view.xml',
    ],
    'test': [],
    "demo": [],
    "active": False,
    "installable": True
}
