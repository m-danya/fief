from enum import Enum


class ErrorCode(str, Enum):
    ACCOUNT_DB_CONNECTION_ERROR = "ACCOUNT_DB_CONNECTION_ERROR"
    AUTH_INVALID_CLIENT_ID = "AUTH_INVALID_CLIENT_ID"
    AUTH_INVALID_AUTHORIZATION_CODE = "AUTH_INVALID_AUTHORIZATION_CODE"
    AUTH_INVALID_CLIENT_ID_SECRET = "AUTH_INVALID_CLIENT_ID_SECRET"
    AUTH_REDIRECT_URI_MISMATCH = "AUTH_REDIRECT_URI_MISMATCH"
