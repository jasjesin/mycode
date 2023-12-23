"""
This file just contains blocklist of JWT tokens. It will be imported by app and
logout resource so that tokens can be added to blocklist, when user logs out
"""

BLOCKLIST = set()  # prefer to use DB or Redis, cuz each app restart is going to
# wipe off this data. This is persistent data, and shouldn't be tampered with.
