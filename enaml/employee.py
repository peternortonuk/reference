#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from __future__ import print_function

import datetime

from atom.api import Atom, Unicode, Range, Bool, Value, Int, Tuple, observe
import enaml
from enaml.qt.qt_application import QtApplication


class Person(Atom):

    last_name = Unicode()
    first_name = Unicode()
    age = Range(low=0)
    dob = Value(datetime.date(1970, 1, 1))
    debug = Bool(False)

    @observe('age')
    def debug_print(self, change):
        """ Prints out a debug message whenever the person's age changes.

        """
        if self.debug:
            templ = "{first} {last} is {age} years old."
            s = templ.format(
                first=self.first_name, last=self.last_name, age=self.age,
            )
            print(s)

    @observe('dob')
    def update_age(self, change):
        """ Update the person's age whenever their date of birth changes

        """
        # grab the current date time
        now = datetime.datetime.utcnow()
        # estimate the person's age within one year accuracy
        age = now.year - self.dob.year
        # check to see if the current date is before their birthday and
        # subtract a year from their age if it is
        if now.month >= self.dob.month and now.day > self.dob.day:
            age -= 1
        # set the persons age
        self.age = age


class Employer(Person):

    company_name = Unicode()


class Employee(Person):

    boss = Value(Employer)
    phone = Tuple(Int())

    @observe('phone')
    def _phone_changed(self, val):
        print('received new phone number for %s: %s' % (self.first_name, val['value']))


def main():
    boss_john = Employer(
        first_name='John', last_name='Paw', company_name="Packrat's Cats",
    )
    employee_mary = Employee(
        first_name='Mary', last_name='Sue', boss=boss_john,
        phone=(555, 555, 5555),
    )

    with enaml.imports():
        from employee_view import EmployeeView

    app = QtApplication()
    view = EmployeeView(employee=employee_mary)
    view.show()

    app.start()

if __name__ == '__main__':
    main()
