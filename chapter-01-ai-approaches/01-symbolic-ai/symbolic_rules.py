
def has_signature_evidence(description: str) -> bool:
    text = description.lower()

    if "unsigned" in text:
        return False

    if "signed" in text:
        return True

    return False

