import sentry_sdk
from svcs import Container
from wheke import WhekeSettings, get_settings

from ._settings import SentrySettings


class SentryService:
    settings: SentrySettings

    def __init__(self, *, settings: SentrySettings) -> None:
        self.settings = settings
        sentry_sdk.init(dsn=settings.dsn, send_default_pii=True)


def sentry_service_factory(container: Container) -> SentryService:
    settings = get_settings(container, WhekeSettings).get_feature(SentrySettings)
    service = SentryService(settings=settings)

    return service
