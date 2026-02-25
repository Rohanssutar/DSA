# Problem Statement
# A valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

# For example, in "alice@neetcode.io", "alice" is the local name, and "neetcode.io" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@neetcode.io" and "alicez@neetcode.io" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
# You are given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

def unique_Emails(emails: list[str]) -> int:
    mails = set()

    for i in emails:
        local, domain = i.split("@")
        local = local.split("+")[0]
        local = local.replace(".", ")")
        mails.add((local, domain))
    return len(mails)

if __name__ == "__main__":
    emails = ["test.email+alex@neetcode.com","test.e.mail+bob.cathy@neetcode.com","testemail+david@nee.tcode.com"]
    print(unique_Emails(emails))
