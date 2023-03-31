import asreviewlib
import inspect


def list_members(pkg):
    r = list()
    members = inspect.getmembers(pkg)
    for name, value in members:
        if inspect.isbuiltin(value) or name.endswith('__'):
            continue
        r.append(f"{pkg.__name__}.{name}")
        if inspect.ismodule(value):
            r += list_members(value)
    return r


def main():
    members = list_members(asreviewlib)
    for i, member in enumerate(members):
        print(f"{i + 1:-3d}. {member}")


if __name__ == '__main__':
    main()
