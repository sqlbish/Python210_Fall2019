# -*- coding: utf-8 -*-
"""
test for mailroom part IV
"""


#import pytest
import mailroom_pt4 as mpt4
import os
import shutil


def test_add_donor():
    """Testing for adding donation to the donor who is already in the database"""
    name = 'Paul Allen'
    amount = 3000.50
    mpt4.add_donations(name, amount)
    assert mpt4.donor_db['Paul Allen'] == [1090.90,4509.45,3000.50]

def test_create_report():
    report = mpt4.create_report()
    assert report[0] == 'Donor Name         | Total Donation | Number of Gifts | Average Donation'
    assert report[2] == 'Satya Nadella          $57893.31           3               $7311.77'
    assert len(report) == 5


def test_write_letters_to_all():
    mpt4.send_letters_toall()
    assert os.path.isdir(os.getcwd() + '\\letterstoall')
    assert os.path.isfile(os.getcwd() + '\\letterstoall\\Bill_Gates.txt')
    shutil.rmtree(os.getcwd() + '\\letterstoall')