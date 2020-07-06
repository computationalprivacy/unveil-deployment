"""Production settings file."""
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# Change this key
SECRET_KEY = 'l@yif+i_t1de$xe2y&vizech@b@)xfea3o@-k$l8()gpew18+0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

# optout details
# Change this to your sheet and range
OPTOUT_SPREADSHEET_ID = 'spreadsheet ID'
OPTOUT_RANGE_NAME = 'spreadsheet range'

# Database details
# Don't change if using standard deployment
MONGO_DB = dict(
    host='mongodb',
    port=27017,
    db_name='wifi',
    password='WiFiUnveIL',
    username='wifi'
)

# Wigle data for fetching probe requests.
# Enter your credentials for Wigle API
WIGLE = dict(
    user='user',
    key='key',
    email='email'
)


# Setup security of the system
class DEMO_SECURITY:
    """Security parameters with Subnet that should be allowed to connect."""

    # Frontend IP range that will only be allowed to query the APIs, last 3 bits should be unset
    allowed_ips = '172.20.0.0/16'
    security_check_required = True  # Do not set False in production
    pin = '1234' #  Numberical Pin to check security of the system


class DEMO_CONSTANTS:
    demo_time = 120 * 60  # session active time in seconds
    active_pi_threshold = 30  # Fetch Pi with status in recent X seconds
    session_time = 5400  # session time for data collection in seconds
    probe_time = 600  # Probe request gathering time in seconds.
    use_hashing = True
    salt = 'ba2f3d2e7f8e55b987cd30f640a97374adecb9ebe50bde6c' # salt for hashing MAC addresses


# Change the password as per Docker compose file.
RQ_QUEUES = {
    'data': {
        'HOST': 'redis',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '12345678',
        'DEFAULT_TIMEOUT': 36000,
    },
    'instructions': {
        'HOST': 'redis',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': '12345678',
        'DEFAULT_TIMEOUT': 36000,
    }
}