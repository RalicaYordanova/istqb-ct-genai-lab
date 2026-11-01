
from symbolic_rules import has_signature_evidence


def test_signed_jewelry():
    assert has_signature_evidence(
        "Vintage earrings signed MONET"
    ) is True


def test_unsigned_jewelry():
    assert has_signature_evidence(
        "Vintage Dior-style earrings, unsigned"
    ) is False


def test_no_signature_information():
    assert has_signature_evidence(
        "Vintage gold-tone earrings"
    ) is False

def test_contradictive_information():
    assert has_signature_evidence(
         "Signed, but Expert said it is fake"
    ) is False
