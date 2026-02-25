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