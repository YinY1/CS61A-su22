import re


# Q1: Email Domain Validator
def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    # Alternate, elegant solution
    domains_list = "|".join([domain.replace(".", "\.") for domain in domains])
    return bool(re.search(rf"^\w+@({domains_list})$", email))
    # solution
    pattern = r"^\w+@("
    for domain in domains:
        if domain == domains[-1]:
            pattern += domain[:-4] + r"\." + domain[-3:] + r")$"
        else:
            pattern += domain[:-4] + r"\." + domain[-3:] + r"|"
    return bool(re.search(pattern, email))


# Q2: Basic URL Validation
def match_url(text):
    """
    >>> match_url("https://cs61a.org/resources/#regular-expressions")
    True
    >>> match_url("https://pythontutor.com/composingprograms.html")
    True
    >>> match_url("https://pythontutor.com/should/not.match.this")
    False
    >>> match_url("https://link.com/nor.this/")
    False
    >>> match_url("http://insecure.net")
    True
    >>> match_url("htp://domain.org")
    False
    """
    scheme = r'^(https?:\/\/)?'
    domain = r'\w+\.\w{3}'
    path = r'(\/\w+)*(\.\w+)?'  # bug: http://a.com.html will be True
    anchor = r'(\/#[\w-]+)?$'
    full_string = scheme + domain + path + anchor
    return bool(re.match(full_string, text))
