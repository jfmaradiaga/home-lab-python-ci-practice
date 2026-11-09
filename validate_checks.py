import json


def get_latest_checks(checks):
    latest_by_node = {}

    for node, attempt, status in checks:
        if node not in latest_by_node or attempt >= latest_by_node[node][0]:
            latest_by_node[node] = (attempt, status)

    return latest_by_node


def main():
    with open("checks.json", encoding="utf-8") as file:
        data = json.load(file)

    latest_by_node = get_latest_checks(data["checks"])
    has_errors = False

    for node in data["required_nodes"]:
        if node not in latest_by_node:
            print(f"MISSING {node}")
            has_errors = True
        elif latest_by_node[node][1] == "FAIL":
            print(f"FAIL {node}")
            has_errors = True

    if has_errors:
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
