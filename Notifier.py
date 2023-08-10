"""
Desktop notification application
Modules - time, plyer
The notification includes Title, Message, Icon, Timeout
"""

import time
from plyer import notification

#We want to run this in background for anytime
while True:
    notification.notify(
        title = "Sleep NOW",
        message = "Restorative moments await! Give yourself the gift of rejuvenation. Tap here to embrace the tranquility of sleep now. Sweet dreams!",
        app_icon = "notification_icon.ico",
        timeout = 15
    )

    time.sleep(10)