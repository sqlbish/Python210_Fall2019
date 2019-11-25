#!/usr/bin/env python3
"""
Created on Sat Nov  2 14:12:38 2019

@author: Bishal.Gupta
"""

def menu_selection(prompt,dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "exit menu":
                break
        except KeyError:
            print('Please select a valid response.')
            continue
        
def quit():
    print("Quitting this menu Now")
    return "exit menu"
        

dict_donations = {'Bill Gates': [4590.45, 300.00, 45670.90],
                   'Jeff Bezos': [5600.89,4500.90],
                   'Satya Nadella': [300.00,670.90,2000,00],
                   'Paul Allen': [1090.90,4509.45],
                   'Howard Shultz': [3456.90]
                   }


def list_donors():
    """Prints a list of all donors in list using list comprehension"""
    spacer = '-' * 25
    donors_list = [donor for donor in dict_donations.keys()]
    print("\nList of all {} donors:\n".format(len(dict_donations)), spacer, '\n', '\n '.join(donors_list), '\n', spacer)
    
    
def add_donations():
# Set up while loop to iterate
    while True:
        #print('Enter a Donorname, type quit to quit out of this menu anytime')
        try:
            donorname = str(input('Enter a Donorname, type quit to quit out of this menu anytime '))
        # Assign to donorname variable            
                #You can quit anytime if response is to quit
            if donorname == "quit":
                break
            elif donorname == 'list':
                list_donors()
            elif type(donorname) == int:
                break
            # Check whether name is in the dictionary and print feedback
            elif donorname in dict_donations:
                print(str(dict_donations[donorname]) + ' is the donation of ' + str(donorname))
                
                check = input(f'Do you want to add donation for donor ' + str(donorname) + '?\n'
                              + 'Please respond "y", "n", or "q" to quit back to main menu: ')
                if check == 'q':
                    break
                elif check != 'y':
                    break
                elif check == 'n':
                    break
                else:
                    #add error handling
                    try:
                        donationamount = int(input(f'Enter donation amount'))
                    except ValueError:
                        print(f'\nYou did not enter a number, Try again.')
                        continue
                    if donationamount == 'q':
                        break
                    dict_donations[donorname].append(float(donationamount))
            
        # If the name is not in the dictionary...
            elif donorname not in dict_donations:
    
                # Provide feedback        
                # Take in a new donation for the associated name
                ##add error handling
                try:
                    donationamount = int(input(f'I don\'t have ' + str(donorname) + '\'s donation, what is it?'))
                except ValueError:
                    print('f\nYou did not enter a number, Try again.')
                    continue
                if donationamount == 'q':
                    break
                # Assign donation value to donaryname key
                #dict_donations[donorname] = donationamount
                dict_donations.update({donorname: [float(donationamount)]})
                
        
                # Print feedback that the data was updated
                print('Data updated.')
                
            else:
                break
        except ValueError:
            print(f"\nYou enter only numbers, Try again.")
            continue
            
        
def send_thankyou():
    """Add a new donation to the database and print a thank you email for the donor"""
    
    response = 'list'
    # get donor name from user, display donor list if asked
    while response == 'list':
        response = input('\nWhat is the full name of the donor to whom you '
                         + 'would like to send a thank you?\nAlternatively, '
                         + 'type "list" for a list of current donors '
                         + 'or "q" to quit back to main menu.\n>>> ')
        if response == 'list':
            for _ in dict_donations.keys():
                print(_)
        elif response == 'q':
            break
        else:
            check = input(f'Is "{response.title()}" the correct donor name?\n'
                          + 'Please respond "y", "n", or "q" to quit back to main menu: ')
            if check == 'q':
                break
            elif check != 'y':
                response = 'list'
    name = response.title()
    # add donor and new donation to database under donor name
    if name in dict_donations.keys():
        amount = []
        amount = dict_donations[name]
        last_donation = str(amount[-1:])
        total_donation = sum(amount)
        line1 = 'Dear Mr/Mrs {},\n\n' \
          + 'Thank you so much for your recent donation of ${}!'
        line2 = 'This brings your total lifetime donations to ${}!'
        line3 = 'We here at ABC Corp appreciate it!\n\n' \
          + 'Sincerely,\n\nBishal Gupta, Founder ABC Corp\n'
        if len(amount) > 1:
            thank_you_message = '\n'.join([line1, line2, line3])
            print(thank_you_message.format(name,last_donation,total_donation))
        else:
            thank_you_message = '\n'.join([line1, line3])
            print(thank_you_message.format(name,last_donation))

    else:
        print("The donor doesn't exist in the db, please go to main to add donors")
    # format an email thank you and print to the terminal


def create_report():
    #print the header for the report
    print(f'{"Donor Name": <20}{"Total Donation":20}{"Number of Gifts":20}{"Average Donation":20}')
    print('_'*80)
    #loop through the dictionary of items and print the names and the donations
    for n,d in dict_donations.items():
        print(f'{n:20} {sum(d):{10}.2f} {len(d):10} {(sum(d)/len(d)):{25}.2f}') 
    
def send_letters_toall():
    #loop through the dictionary of items
    for n,d in dict_donations.items():
        #print the message to seperate files by donor
        try:
            with open(f'{n}.txt', 'w') as file:
                file.write(f'Subject: Thank You for you Donation \n\nDear {n}, \n We greatly appreciate your donation of ${sum(d):.2f} \n\nSincerely,\n\nBishal Gupta, Founder ABC Corp')
        except IOError:
            print('error writing to file')
    
main_prompt = ("\You are in the main menu now!!!\n"
                "What do you want to do?\n"
                "Type 1 to add donors and donations.\n"
                "Type 2 to Send a Thank You to a Single Donor.\n"
                "Type 3 to Create a Report.\n"
                "Type 4 to Send letters to all donors.\n"
                " or q to exit >> "
                )

main_dispatch = {"1":add_donations,
                 "2":send_thankyou,
                 "3":create_report,
                 "4":send_letters_toall,
                 "q":quit,
                 }
        
        
if __name__ ==  "__main__":
    menu_selection(main_prompt,main_dispatch)
    
        
