#!/usr/bin/python

from Crypto.Cipher import AES
from os import urandom
import random
from string import hexdigits
import subprocess

KEY = urandom(16)
cipher = AES.new(key=KEY, mode=AES.MODE_ECB)
balance = 10
bank_accounts = [urandom(16) for _ in range(4)]
user_account = bank_accounts[0]
used = {}

def encrypt_transaction(sender, receiver, amount):
    amt = '0'*(16 - len(str(amount))) + str(amount)
    return cipher.encrypt(sender + receiver + amt).encode('hex')

def max_amount_transaction():
    sender = random.choice(bank_accounts[1:])
    remaining = [_ for _ in bank_accounts[1:] if not _ == sender]
    receiver = random.choice(remaining)
    amount = 500
    return encrypt_transaction(sender, receiver, amount)

def generate_transactions():
    transactions = []

    sender = bank_accounts[1]
    receiver = bank_accounts[2]
    amount = 200
    transactions.append(encrypt_transaction(sender, receiver, amount))

    sender = bank_accounts[3]
    receiver = bank_accounts[2]
    amount = 250
    transactions.append(encrypt_transaction(sender, receiver, amount))

    for _ in range(8):
        sender = random.choice(bank_accounts[1:])
        remaining = [_ for _ in bank_accounts[1:] if not _ == sender]
        receiver = random.choice(remaining)
        amount = random.randint(1, 500)
        transactions.append(encrypt_transaction(sender, receiver, amount))

    return transactions

def check_transaction(ciphertext):
    if not len(ciphertext) == 96:
        print "Invalid Length"
        print "Transaction Format:"
        print "sender account number(16 bytes)+receiver account number(16 bytes)+amount(prepended appropraitely to 16 bytes)\n"
        print "'+' represents concatenation"
        return 0 
    
    for i in ciphertext:
        if i not in hexdigits:
            print "Non-hex characters found in the ciphertext"
            return 0

    plaintext = cipher.decrypt(ciphertext.decode('hex'))
    transaction = [plaintext[i:16 + i] for i in range(0, 48, 16)]

    if transaction[0] == transaction[1]:
        print "Invalid Transaction."
        return 0

    try:
        amount = int(transaction[2])

    except:
        print "Invalid amount value"
        return 0

    if amount > 500 or amount < 1:
        print "Amount is not within the specified bounds."
        return 0

    if transaction[0] == user_account:
        if amount > balance:
            print "You don't have enough balance."
            return 0

        else:
            print "Transaction successful."
            return (-amount)

    else:
        if transaction[1] == user_account:
            print "Transaction successful."
            return amount

        else:
            print "Transaction successful."
            return 0

def menu_1():
    print 'Max transfers = 10'
    print 'More choices become available after finishing all transfers.\n'
    print '1. Transfer money.'
    print 'Enter your choice:'
    choice = raw_input()

    if not choice == '1':
        exit()

    return int(choice)

def menu_2():
    print "2. See today's transactions(encrypted)"
    print '3. See special transaction(encrypted)'
    print '4. Provide encrypted transactions.'
    print '5. Get flag.'
    print 'Enter your choice:'
    choice = raw_input()

    if choice not in ['2', '3', '4', '5']:
        exit()

    return int(choice)

def title():
    print '''\n
                     Extra Careful Bank
We use advanced encryption standard to encrypt our transactions
'''

count = 0
today = generate_transactions()

while True:
    title()
    print '\nBALANCE: ${}'.format(balance)
    print 'NUMBER OF TRANSFERS DONE: {}\n'.format(count)
    if count < 10:
        choice = menu_1()

    else:
        choice = menu_2()

    if choice == 1:
        print "Enter the receiver id(1, 2 or 3):"
        recv_id = raw_input()
        if recv_id not in ['1', '2', '3']:
            print 'Invalid receiver id'

        else:
            print "Enter amount(min = $1, max = $500):"
            amt = raw_input()

            try:
                amount = int(amt)

            except:
                "Invalid amount value"

            if amount < 1 or amount > 500:
                print "Amount is not within the specified bounds."

            else:
                if amount > balance:
                    print "You don't have enough balance."

                else:
                    count += 1
                    balance -= amount
                    today.append(encrypt_transaction(user_account, bank_accounts[int(recv_id)], amount))
                    print "Transfer made successfully."

    elif choice == 2:
        for _ in range(3):
            random.shuffle(today)

        for t in today:
            print t

    elif choice == 3:
        print "This is an encrypted transaction involving a transfer of $500:"
        print max_amount_transaction()

    elif choice == 4:
        print 'Since the Extra Careful Bank uses such a secure encryption, we are sure that no one can forge encrypted transactions.'
        print 'If you think you can, provide me with three valid encrypted transactions and they will be processed.'
        print 'First encrypted transaction:'
        t = raw_input()
        if t not in used:
            balance += check_transaction(t)
            used[t] = 1
        
        else:
            print 'You have already used this one.'

        print 'Second encrypted transaction:'
        t = raw_input()
        if t not in used:
            balance += check_transaction(t)
            used[t] = 1
        
        else:
            print 'You have already used this one.'
        
        print 'Third encrypted transaction:'
        t = raw_input()
        if t not in used:
            balance += check_transaction(t)
            used[t] = 1
        
        else:
            print 'You have already used this one.'

    else:
        if balance >= 1500:
            with open("flag.txt") as flag:
                print "Here is your flag: " + flag.read()

        else:
            print 'You need a balance greater than or equal to $1500 to get the flag.'    