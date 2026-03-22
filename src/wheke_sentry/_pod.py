from wheke import Pod, ServiceConfig

from ._service import SentryService, sentry_service_factory

sentry_pod = Pod(
    "sentry",
    services=[
        ServiceConfig(
            SentryService,
            sentry_service_factory,
            is_singleton=True,
        ),
    ],
)
