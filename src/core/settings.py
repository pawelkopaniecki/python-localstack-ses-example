from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """

    This class contains all environment variables required by the application.

    Attributes:
        ENVIRONMENT (str): Environment in which the application is launched
        AWS_ENDPOINT_URL (str): AWS endpoint URL
        AWS_ACCESS_KEY_ID (str | None): AWS Access Key ID (provided in local development for LocalStack)
        AWS_SECRET_ACCESS_KEY (str | None): AWS Secret Access Key (provided in local development for LocalStack)
        AWS_REGION (str | None): AWS Regino where application is deployed
        SENDER_EMAIL_ADDRESS (str): Email address from which messages will be sent
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    ENVIRONMENT: str
    AWS_ENDPOINT_URL: str
    AWS_ACCESS_KEY_ID: str | None
    AWS_SECRET_ACCESS_KEY: str | None
    AWS_REGION: str | None
    SENDER_EMAIL_ADDRESS: str


settings = Settings()  # type: ignore[call-arg]
