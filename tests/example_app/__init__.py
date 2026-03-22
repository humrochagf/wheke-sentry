from wheke import Wheke

from wheke_sentry import sentry_pod


def build_wheke() -> Wheke:
    wheke = Wheke()

    wheke.add_pod(sentry_pod)

    return wheke
