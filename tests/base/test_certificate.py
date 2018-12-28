from tempfile import _TemporaryFileWrapper

import pytest
from PyNFSe.base.certificate import _create_temp_file, get_certificate


@pytest.fixture
def certificate_chain():
    return b'''-----BEGIN CERTIFICATE-----
MIIDhDCCAmygAwIBAgIKZCXL8wAAAAAStTANBgkqhkiG9w0BAQUFADAcMRowGAYD
VQQDExFQSUxPVE9JU1NDVVJJVElCQTAeFw0xNjExMTUwMjQ0MzVaFw0xNzExMTUw
MjU0MzVaMFExCzAJBgNVBAYTAkFBMQowCAYDVQQIEwFhMQowCAYDVQQHEwFhMQow
CAYDVQQLEwFhMQowCAYDVQQDEwFhMRIwEAYJKoZIhvcNAQkBFgNhQGEwgZ8wDQYJ
KoZIhvcNAQEBBQADgY0AMIGJAoGBAKWXY7Ed+tNB08Gk9XDs64ySfebqUj8GPSkN
5v0JbGoKsU28PZKJmdZGI32PzSRimpqJ8TtF+mlIYzPGOWaPQfQ0RIul22TLEBFV
/MTf9NtQ+XtrI3P+41Z1b7NUfvZAeJX37td4yzD6tytLDG+OsqBoEFE1fcvEFm6S
SXjnqg4JAgMBAAGjggEVMIIBETAOBgNVHQ8BAf8EBAMCBPAwEwYDVR0lBAwwCgYI
KwYBBQUHAwIwHQYDVR0OBBYEFKjFwEt26SdfbwOm5dfhVTwwpsLqMB8GA1UdIwQY
MBaAFMfsVZWz6ktjZvG/o306I++LnBhLMEcGA1UdHwRAMD4wPKA6oDiGNmZpbGU6
Ly9XRUJBUFBJU1NDV0IwNC9DZXJ0RW5yb2xsL1BJTE9UT0lTU0NVUklUSUJBLmNy
bDBhBggrBgEFBQcBAQRVMFMwUQYIKwYBBQUHMAKGRWZpbGU6Ly9XRUJBUFBJU1ND
V0IwNC9DZXJ0RW5yb2xsL1dFQkFQUElTU0NXQjA0X1BJTE9UT0lTU0NVUklUSUJB
LmNydDANBgkqhkiG9w0BAQUFAAOCAQEAcN1v1u/jyWoz54Py80QKc82ZfoYO12Ak
vw4hIc28BszeBO/cv1Idizu2jdqD0fG9mFrKqUd0LctOaumvr3tzSIEhH+oT3+8h
DBb4uhHBNAia1gcCYUZp+VMh/gsH5DKeziMCVEpb3NMu9GZ6rLdeTy4P7pymg1IC
Lud52TreMS6CXFZX7wD+uHJeLPEqQja1bT/1UDxq4h6fgI+y2N2h77vyt0NJkejV
DfKus4bPCxAVxnp4DREA+ZKlTuHFCrSQd21MDydE3sRgj9VDiJxFMoTWCTiYM63d
0SDKDuvm7gT9lhbDUFES8RCPOL3Pagr9bmpjALK0IBUISRXHRX9R0Q==
-----END CERTIFICATE-----
'''


@pytest.fixture
def certificate_key():
    return b'''-----BEGIN PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAKWXY7Ed+tNB08Gk
9XDs64ySfebqUj8GPSkN5v0JbGoKsU28PZKJmdZGI32PzSRimpqJ8TtF+mlIYzPG
OWaPQfQ0RIul22TLEBFV/MTf9NtQ+XtrI3P+41Z1b7NUfvZAeJX37td4yzD6tytL
DG+OsqBoEFE1fcvEFm6SSXjnqg4JAgMBAAECgYAJIy9Vu9QmUeq10+zUykgNsdw3
cKzw7B7WG/2n7xwPxm8F/XoO0t+9rJFjCXs+E6BZIH1ConAI3P0XY2vxsjxG/veC
hnYVU9NOk49Fa1mzWLH82zsDzSLkrewjcxC56kXfZ7c6kpc2/U6D/UQkOIS+TWhO
HmRlnhSMkrgKT1n+MQJBAObqfx+p+17jVzPyDsnpdzlFZlcOYj26XgT0RHuSlRyY
YPZGtF1FwK9mIFUNhqpL0EYRJ/o7hgkdzzrublFre1kCQQC3lEqOIaQK21FUjUP9
8zPbcDEhgYZecI9mwLEHlCIjTEfUgqkSLKeR9HTMGNZRAOXxX+tJL36wz1v1IvTl
zsIxAkBd7KnyljBxwyT4MxAC3tyoxeq/pFEfbIvLlhO488GFFRHzeoTon3OlpHOo
RM0uvZGkvlu1c7qsQJzHCq6CnaZZAkBvzt51oGGTxy3KrFsr0TLVRIh32rZm0HFW
aKepcPw1uWDKOmYUzqOkjlmQcNQe88gYcY4Qvd+QekqMi6TSTlIRAkA/suD5u5vF
NbqnpyPnDulvgtXE2B1UHl0wZJbLfDH+BFckz7B557Cz507YthsWWJmjVPVqJXLM
HFZwimKs65R9
-----END PRIVATE KEY-----
'''


def test_get_certificate(certificate_chain, certificate_key, certificate_file_path, certificate_password):
    cert, cert_file, key, key_file = get_certificate(certificate_file_path, certificate_password)

    assert cert == certificate_chain
    assert cert_file.read() == certificate_chain
    assert key == certificate_key
    assert key_file.read() == certificate_key


def test_create_temp_file(certificate_key):
    result = _create_temp_file(certificate_key)

    assert isinstance(result, _TemporaryFileWrapper)
    assert result.read() == certificate_key
