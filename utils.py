"""Utility helpers for entropy analysis and logging."""

from __future__ import annotations

import datetime as dt
import math


def calculate_entropy(password: str) -> float:
    """Calculate Shannon-like brute-force entropy estimate in bits."""
    if not password:
        return 0.0

    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(not c.isalnum() for c in password):
        charset_size += 32

    if charset_size == 0:
        return 0.0
    return len(password) * math.log2(charset_size)


def explain_entropy(entropy: float) -> str:
    """Return security explanation for entropy value."""
    if entropy < 28:
        return "Very low entropy: easily guessable password."
    if entropy < 36:
        return "Low entropy: vulnerable to common attacks."
    if entropy < 60:
        return "Moderate entropy: acceptable for low-risk use cases."
    if entropy < 80:
        return "High entropy: strong for most accounts."
    return "Very high entropy: excellent resistance to brute force."


def log_result(score: int, breach_result: str, filename: str = "logs.txt") -> None:
    """Append timestamped result data to log file."""
    timestamp = dt.datetime.now().isoformat(timespec="seconds")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] score={score} breach='{breach_result}'\n")
