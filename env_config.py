import environ

# Initialize the environment variables
env = environ.Env(
    DEBUG=(bool, False),  # Default to False if not set

    # Secret key for Django
    SECRET_KEY=(str, ''),

    # Database configuration
    DATBASE_NAME=(str, ''),
    DATABASE_USER=(str, ''),
    DATABASE_PASSWORD=(str, ''),
    DATABASE_HOST=(str, ''),
    DATABASE_PORT=(str, ''),

    # Email configuration
    EMAIL_ID=(str, ''),
    EMAIL_PASSWORD=(str, ''),
)

env.read_env()  # Read the .env file