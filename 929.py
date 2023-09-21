class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set() # plan to have (uniquename,uniquedomain)
        for e in emails:
            full_name,full_domain = e.split("@")
            unique_domain = full_domain[0:-4]
            half_name = full_name.split("+")[0]
            unique_name = "".join(half_name.split("."))
            seen.add((unique_name,unique_domain))
        return len(seen)
