from crypto_intel.security.redact import redact

def test_redact_wif():
    text = "secret 5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ"
    assert "[REDACTED]" in redact(text)
