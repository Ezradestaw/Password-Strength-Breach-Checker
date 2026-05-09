"""Secure password generation module."""

from __future__ import annotations

import secrets
import string


class PasswordGenerator:
    """Generate strong random passwords with configurable options."""

    def generate(self, length: int = 16, include_numbers: bool = True, include_symbols: bool = True) -> str:
        if length < 8:
            raise ValueError("Password length should be at least 8")

        alphabet = string.ascii_letters
        required_sets = [string.ascii_lowercase, string.ascii_uppercase]

        if include_numbers:
            alphabet += string.digits
            required_sets.append(string.digits)
        if include_symbols:
            alphabet += "!@#$%^&*()-_=+[]{};:,.?/"
            required_sets.append("!@#$%^&*()-_=+[]{};:,.?/")

        # Ensure complexity by pre-selecting at least one char from each required set.
        password_chars = [secrets.choice(charset) for charset in required_sets]
        password_chars.extend(secrets.choice(alphabet) for _ in range(length - len(password_chars)))

        secrets.SystemRandom().shuffle(password_chars)
        return "".join(password_chars)
