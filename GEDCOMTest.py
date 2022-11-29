# -*- coding: utf-8 -*- 
# @Time : 11/20/2022 2:31 PM
# @Author : Harshith Roopa Manjunath, CWID: 20005252
# @File : GEDCOMTest.py
# @Description : Test the class and its functions in GEDCOMExtract

import unittest
import GEDCOMExtract as Extract


class TestExtract(unittest.TestCase):
    def testStoreBirthAndDeathDate(self):
        """
        Written by HRM
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15") #Random date testing
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
                                     "2070-10-10") #Example gedcom
        self.assertEqual(person1.birth_date, [9, 10, 1877])
        self.assertEqual(person1.death_date, [15, 6, 1952])
        self.assertEqual(person2.birth_date, [5, 6, 1945])
        self.assertEqual(person2.death_date, [10, 10, 2070])
    
    def testBirthBeforeMarry(self):
        """
        Written by NM - Done
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "1900-3-25", "1950-5-4",
                                     "1925-10-10")
    
        self.assertTrue(person1.isBirthBeforeMarry())
        self.assertFalse(person2.isBirthBeforeMarry())
    
    def testBirthBeforeDeath(self):
        """
        Written by NM - Done
        :return:
        """
        person1 = Extract.Person("I13", "F4", "Sirius", "Black", 74, "1877-10-9", "1998-8-20", "2028-6-12",
                                     "1952-6-15")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
                                     "1900-10-10")
    
        self.assertTrue(person1.isBirthBeforeDeath())
        self.assertFalse(person2.isBirthBeforeDeath())
    
    def testMarryBeforeDeath(self):
        """
        Written by KR - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Oliver", "Black", 92, "929-5-18", "1955-2-27", "NA", "1995-9-7")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 11, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
        print(person2.isMarryBeforeDeath())
        self.assertTrue(person1.isMarryBeforeDeath())
        self.assertFalse(person2.isMarryBeforeDeath())
    
    def testDivorceBeforeDeath(self):
        """
        Written by KR - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Reagan", "Black", 91, "1906-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    
        self.assertTrue(person1.isDivorceBeforeDeath())
        self.assertFalse(person2.isDivorceBeforeDeath())
    
    def testMarryBeforeDivorce(self):
        """
        Written by SK - Done
        :return:
        """
        person1 = Extract.Person("I1", "F1", "Reagan", "Black", 91, "1906-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        person2 = Extract.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    
        self.assertTrue(person1.isMarryBeforeDivorce())
        self.assertFalse(person2.isMarryBeforeDivorce())

if __name__ == '__main__':
    unittest.main()
