from typing import ClassVar

from wheke import FeatureSettings


class SentrySettings(FeatureSettings):
    __feature_name__: ClassVar[str] = "sentry"

    dsn: str = "https://ingest.url.sentry.io/projectcode"
