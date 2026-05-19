#  This file is part of SenkoGuardianModules
#  Copyright (c) 2025-2026 Senko
#  This software is released under the MIT License.
#  https://opensource.org/licenses/MIT

# scope heroku_min: 2.0.0
# meta banner: https://raw.githubusercontent.com/SenkoGuardian/SenkoGuardian.github.io/main/OfficialSenkoGuardianBanner.png
# meta pic: https://raw.githubusercontent.com/SenkoGuardian/SenkoGuardian.github.io/main/OfficialSenkoGuardianBanner.png

__version__ = ("6", "6", "0") 

"""￣へ￣"""

# meta developer: @SenkoGuardianModules cli by @SKBERRYXX

#  .------. .------. .------. .------. .------. .------.
#  |S.--. | |E.--. | |N.--. | |M.--. | |O.--. | |D.--. |
#  | :/\: | | :/\: | | :(): | | :/\: | | :/\: | | :/\: |
#  | :\/: | | :\/: | | ()() | | :\/: | | :\/: | | :\/: |
#  | '--'S| | '--'E| | '--'N| | '--'M| | '--'O| | '--'D|
#  `------' `------' `------' `------' `------' `------'

import re
import os
import io
import random
import socket
import base64
import uuid
import json
import asyncio
import logging
import tempfile
import time
import aiohttp
from markdown_it import MarkdownIt
import pytz
import httpx
import pytz

# New SDK Check
try:
    from google import genai
    from google.genai import types
    import google.api_core.exceptions as google_exceptions
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    google_exceptions = None

# Google OAuth2 (для Gemini CLI)
try:
    from google.oauth2 import credentials as google_oauth2_credentials
    from google.auth.transport.requests import Request as GoogleAuthRequest
    GOOGLE_OAUTH_AVAILABLE = True
except ImportError:
