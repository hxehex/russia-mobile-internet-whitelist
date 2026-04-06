import sys
import re
import argparse


class ModeConfig:
    file = None
    
    def sort_key(self, entry: str) -> tuple:
        raise NotImplementedError
    
    def validate(self, entry: str) -> bool:
        raise NotImplementedError

    def sort(self, entries: list[str]) -> list[str]:
        return sorted(
            {e for e in entries if e},
            key=self.sort_key,
        )

    def insert(self, new_entries: list[str], address_list: list[str]) -> list[str]:
        normalized = [e.strip() for e in [*address_list, *new_entries] if e.strip()]
        return self.sort(normalized)


class DomainMode(ModeConfig):
    file = "whitelist.txt"

    def sort_key(self, domain: str) -> tuple:
        labels = domain.split(".")
        without_tld = labels[:-1]
        return tuple(label.lower() for label in reversed(without_tld))

    def validate(self, domain: str) -> bool:
        pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        return bool(re.match(pattern, domain.strip()))


class IpMode(ModeConfig):
    file = "ipwhitelist.txt"

    def sort_key(self, ip: str) -> tuple:
        return tuple(int(octet) for octet in ip.strip().split("."))

    def validate(self, ip: str) -> bool:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)


class CidrMode(IpMode):
    file = "cidrwhitelist.txt"

    def sort_key(self, cidr: str) -> tuple:
        ip, mask = cidr.split("/")
        return (*super().sort_key(ip), int(mask))

    def validate(self, cidr: str) -> bool:
        if "/" not in cidr:
            return False
        ip, mask = cidr.split("/", 1)
        return super().validate(ip) and mask.isdigit() and 0 <= int(mask) <= 32


MODES: dict[str, ModeConfig] = {
    "domain": DomainMode(),
    "ip":     IpMode(),
    "cidr":   CidrMode(),
}

def setup_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Insert whitelisted address entries.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python whitelist-utils.py domain yandex.ru"
    )

    parser.add_argument(
        "mode",
        choices=MODES.keys(),
        help="Operation mode"
    )

    parser.add_argument(
        "addr",
        nargs="*",
        help="Address entries (leave empty to sort the file)"
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    config = MODES[args.mode]

    invalid = [a for a in args.addr if not config.validate(a)]
    if invalid:
        for entry in invalid:
            print(f"Invalid {args.mode}: {entry}")
        sys.exit(1)

    try:
        with open(config.file, 'a+') as file:
            file.seek(0)
            address_list = file.readlines()
            file.seek(0)
            file.write("\n".join(config.insert(args.addr, address_list)))
            file.truncate()
    except OSError as e:
        print(f"File error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main(setup_args())
