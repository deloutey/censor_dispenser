# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_word(word, email):
    if word in email:
        email_censored = email.replace(word, '-')
    else:
        email_censored = email
    return email_censored

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
testemail = """
Good Morning, Board of Investors,

Lots of updates this week. """

def censor_list(list, email):
    for word in list:
        if word in email:
            result = email.replace(word, '-')
        else:
            return email
    return result2

testlist = ["Morning", "updates"]
censor_list(testlist, testemail)
