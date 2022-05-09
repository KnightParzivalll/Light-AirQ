from LightAirQ import LightAirQ
from LightAirQ.exceptions import LightAirQException

from loguru import logger

config = {
    "handlers": [
        {
            "sink": "logs/debug.log",
            "level": "DEBUG",
            "rotation": "1 MB",
            "compression": "zip",
        },
    ],
}

logger.configure(**config)

# Latitude and longitude to find the nearest active post
ref_point = ("lat", "lon")
# API access token
TOKEN = "token"

airq = LightAirQ(TOKEN)

try:
    posts_list = airq.get_available_posts()
    posts_list = airq.sort_posts_in_order_of_increasing_distance(posts_list, ref_point)
    measurement = airq.get_last_measurement_from_post(posts_list[0]["id"])
    measurement["postInfo"] = posts_list[0]

    print(measurement)

except KeyboardInterrupt:
    exit(0)

except LightAirQException:
    logger.error("An error occurs during execution...")
    print("An error occurs during execution...")
