#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
class Donor:
    def __init__(self,DonorName,ListInitialDonations=None):
      if type(ListInitialDonations)!='list':
          'Donorname'
          'DonationAmount'
          'Num of Donations'
          'Average Donations'
      self.DonorName=DonorName
      self.Donations=ListInitialDonations
    
    
    def AddDonation(self,Amount):
        self.Donations.append(Amount)
    
    def AverageDonation(self):
        return sum(self.Donations)/len(self.Donations)
    
    def SendEmailLatest(self):
        print ('Dear donor',self.DonorName,'the last donation is',self.Donations[-1])
    
    def TotalDonation(self):
        return sum(self.Donations)


class Charity:
    def __init__(self,Name):
        self.CharityName=Name
        self.Donors={}
    
    def AddDonor(self,DonorName,ListDonations):
        self.Donors[DonorName]=Donor(DonorName,ListDonations)    
    
    def PrintAllDonations(self):
        String=''
        for key, value in self.Donors.items():
            #
            #print(type(str(value.TotalDonation())))
            String+='Donor'+key+'total amount is'+str(value.TotalDonation())+'\n'
        print(String)
        
NewCharity=Charity("ABC Inc")
NewCharity.AddDonor("Satya Nadella",[10,20,30])
NewCharity.AddDonor("Howard Schultz",[40])