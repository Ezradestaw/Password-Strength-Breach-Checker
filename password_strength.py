"""Password strength analysis module."""

from __future__ import annotations

import re
from dataclasses import dataclass

from utils import calculate_entropy


COMMON_PATTERNS = {
    "123456",
    "password",
    "qwerty",
    "admin",
    "letmein",
    "iloveyou",
    "welcome",
}


@dataclass
class PasswordStrengthChecker:
    """Analyze password strength and produce a 0-100 score."""

    def analyze(self, password: str) -> dict[str, int | str]:
        score = 0
        length = len(password)

        if length >= 8:
            score += 20
        if length >= 12:
            score += 10
        if length >= 16:
            score += 10

        if re.search(r"[A-Z]", password):
            score += 15
        if re.search(r"[a-z]", password):
            score += 15
        if re.search(r"\d", password):
            score += 15
        if re.search(r"[^A-Za-z0-9]", password):
            score += 15

        lowered = password.lower()
        if any(pattern in lowered for pattern in COMMON_PATTERNS):
            score -= 25
        if re.search(r"(.)\1{2,}", password):
            score -= 10
        if re.search(r"(?:0123|1234|2345|3456|4567|5678|6789)", password):
            score -= 10

        score = max(0, min(100, score))

        if score < 45:
            label = "Weak"
        elif score < 75:
            label = "Medium"
        else:
            label = "Strong"

        return {"score": score, "label": label}

    def entropy(self, password: str) -> float:
        return calculate_entropy(password)
