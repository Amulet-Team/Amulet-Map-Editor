from pip._internal.operations import freeze


def main():
    with open("requirements.txt") as f:
        requirements = [r.strip() for r in f.readlines()]
    first_party = {
        "amulet-core",
        "amulet-nbt",
        "pymctranslate",
        "minecraft-resource-pack",
    }
    installed = {r.split("==")[0].lower(): r for r in freeze.freeze() if "==" in r}
    for index, r in enumerate(requirements):
        if r[0] != "#" and "~=" in r:
            req = r.split("~=")[0]
            if req in first_party and req in installed:
                requirements[index] = installed[req]
    with open("requirements.txt", "w") as f:
        f.write("\n".join(requirements))


if __name__ == "__main__":
    main()
