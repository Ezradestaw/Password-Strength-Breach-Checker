"""Module for checking password against local breach data."""

from __future__ import annotations

import hashlib


class BreachChecker:
    """Simulated breach checker with local SHA-1 hash dataset."""

    def __init__(self) -> None:
        compromised_passwords = {
            "password",
            "123456",
            "qwerty",
            "letmein",
            "admin",
            "welcome",
            "monkey",
            "abc123",
        }
        self.breached_hashes = {self._sha1(pw) for pw in compromised_passwords}

    @staticmethod
    def _sha1(password: str) -> str:
        return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    def check_password(self, password: str) -> str:
        candidate_hash = self._sha1(password)
        if candidate_hash in self.breached_hashes:
            return "Password found in leaked database"
        return "Password not found in known breaches"
