shares = {}

def submit_share(party_id, share):
    shares[party_id] = share
    return len(shares)

def compute_result():
    if len(shares) < 3:
        return None
    return sum(shares.values())
