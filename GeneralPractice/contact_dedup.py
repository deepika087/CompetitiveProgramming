__author__ = 'deepika'
contacts = {
    "C1" : ["E1", "E2"],
    "C2" : ["E3"],
    "C3" : ["E2", "E4"],
    "C4" : ["E4"],
    "C5" : ["E3"],
    "C6" : ["E5"]
}

def dfs(edges, contact, seen, found=None):
    found = found or []
    if contact not in seen:
        seen.add(contact)
        found.append(contact)
        emails = contacts[contact]
        for email in emails:
            for other in edges[email]:
                dfs(edges, other, seen, found)

    return found

def deduplication(contacts):
    by_email = {}
    for contact in contacts:
        emails = contacts[contact]
        for email in emails:
            if email not in by_email:
                by_email[email] = []
            by_email[email].append(contact)

    print("by_email : ", by_email)


    seen = set()
    print filter(None, [dfs(by_email, contact, seen) for contact in contacts]);


deduplication(contacts)