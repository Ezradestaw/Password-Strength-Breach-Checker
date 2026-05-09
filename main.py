"""Entry point for Password Strength & Breach Checker CLI tool."""

from __future__ import annotations

from colorama import Fore, Style, init

from breach_checker import BreachChecker
from generator import PasswordGenerator
from password_strength import PasswordStrengthChecker
from utils import explain_entropy, log_result


class CyberCLI:
    """Menu-based interface for password checks and generation."""

    def __init__(self) -> None:
        init(autoreset=True)
        self.strength_checker = PasswordStrengthChecker()
        self.breach_checker = BreachChecker()
        self.generator = PasswordGenerator()

    @staticmethod
    def banner() -> None:
        """Display startup banner."""
        print(Fore.CYAN + r"""
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 

   Strength & Breach Checker :: Cybersecurity CLI
""")

    @staticmethod
    def _ask_yes_no(prompt: str) -> bool:
        while True:
            answer = input(prompt).strip().lower()
            if answer in {"y", "yes"}:
                return True
            if answer in {"n", "no"}:
                return False
            print(Fore.YELLOW + "Please enter yes/y or no/n.")

    @staticmethod
    def _ask_length() -> int:
        while True:
            value = input("Enter desired length (8-128): ").strip()
            if value.isdigit() and 8 <= int(value) <= 128:
                return int(value)
            print(Fore.YELLOW + "Length must be a number between 8 and 128.")

    def check_strength(self) -> None:
        password = input("Enter password to analyze: ").strip()
        result = self.strength_checker.analyze(password)
        entropy = self.strength_checker.entropy(password)
        entropy_text = explain_entropy(entropy)

        color = Fore.RED if result["label"] == "Weak" else Fore.YELLOW if result["label"] == "Medium" else Fore.GREEN
        print(color + f"Score: {result['score']}/100")
        print(color + f"Label: {result['label']}")
        print(Style.BRIGHT + f"Entropy: {entropy:.2f} bits")
        print(Style.DIM + f"{entropy_text}")

        breach_result = self.breach_checker.check_password(password)
        print(Fore.MAGENTA + breach_result)

        log_result(score=result["score"], breach_result=breach_result)

    def check_breach(self) -> None:
        password = input("Enter password to check breach status: ").strip()
        breach_result = self.breach_checker.check_password(password)
        print(Fore.MAGENTA + breach_result)

        result = self.strength_checker.analyze(password)
        log_result(score=result["score"], breach_result=breach_result)

    def generate_password(self) -> None:
        length = self._ask_length()
        include_numbers = self._ask_yes_no("Include numbers? (y/n): ")
        include_symbols = self._ask_yes_no("Include symbols? (y/n): ")

        password = self.generator.generate(
            length=length,
            include_numbers=include_numbers,
            include_symbols=include_symbols,
        )

        result = self.strength_checker.analyze(password)
        entropy = self.strength_checker.entropy(password)

        print(Fore.GREEN + f"Generated Password: {password}")
        print(Fore.GREEN + f"Score: {result['score']}/100 ({result['label']})")
        print(Style.BRIGHT + f"Entropy: {entropy:.2f} bits")

        breach_result = self.breach_checker.check_password(password)
        print(Fore.MAGENTA + breach_result)

        log_result(score=result["score"], breach_result=breach_result)

    def run(self) -> None:
        self.banner()

        while True:
            print(Fore.CYAN + "\n=== Main Menu ===")
            print("1) Check password strength")
            print("2) Check breach status")
            print("3) Generate secure password")
            print("4) Exit")

            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                self.check_strength()
            elif choice == "2":
                self.check_breach()
            elif choice == "3":
                self.generate_password()
            elif choice == "4":
                print(Fore.CYAN + "Stay secure. Goodbye!")
                break
            else:
                print(Fore.YELLOW + "Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    CyberCLI().run()
