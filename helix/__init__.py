"""
This module contains the Client class required for applications to connect and
interact with the Wind River Helix Device Cloud 2.Next.
"""

from logging import CRITICAL as LOGCRITICAL
from logging import ERROR as LOGERROR
from logging import DEBUG as LOGDEBUG
from logging import INFO as LOGINFO
from logging import NOTSET as LOGNOTSET
from logging import WARNING as LOGWARNING

from helix._core.client import Client
from helix._core.handler import status_string

from helix._core.constants import DEFAULT_CONFIG_DIR
from helix._core.constants import DEFAULT_CONFIG_FILE
from helix._core.constants import DEFAULT_KEEP_ALIVE
from helix._core.constants import DEFAULT_LOOP_TIME
from helix._core.constants import DEFAULT_THREAD_COUNT

from helix._core.constants import STATUS_SUCCESS
from helix._core.constants import STATUS_INVOKED
from helix._core.constants import STATUS_BAD_PARAMETER
from helix._core.constants import STATUS_BAD_REQUEST
from helix._core.constants import STATUS_EXECUTION_ERROR
from helix._core.constants import STATUS_EXISTS
from helix._core.constants import STATUS_FILE_OPEN_FAILED
from helix._core.constants import STATUS_FULL
from helix._core.constants import STATUS_IO_ERROR
from helix._core.constants import STATUS_NO_MEMORY
from helix._core.constants import STATUS_NO_PERMISSION
from helix._core.constants import STATUS_NOT_EXECUTABLE
from helix._core.constants import STATUS_NOT_FOUND
from helix._core.constants import STATUS_NOT_INITIALIZED
from helix._core.constants import STATUS_OUT_OF_RANGE
from helix._core.constants import STATUS_PARSE_ERROR
from helix._core.constants import STATUS_TIMED_OUT
from helix._core.constants import STATUS_TRY_AGAIN
from helix._core.constants import STATUS_NOT_SUPPORTED
from helix._core.constants import STATUS_FAILURE

import helix.osal
import helix.ota_handler
import helix.relay

__all__ = ["Client",
           "status_string",
           "osal"
           "ota_handler",
           "relay",
           "DEFAULT_CONFIG_DIR",
           "DEFAULT_CONFIG_FILE",
           "DEFAULT_KEEP_ALIVE",
           "DEFAULT_LOOP_TIME",
           "DEFAULT_THREAD_COUNT",
           "LOGCRITICAL",
           "LOGERROR",
           "LOGDEBUG",
           "LOGINFO",
           "LOGNOTSET",
           "LOGWARNING",
           "STATUS_SUCCESS",
           "STATUS_INVOKED",
           "STATUS_BAD_PARAMETER",
           "STATUS_BAD_REQUEST",
           "STATUS_EXECUTION_ERROR",
           "STATUS_EXISTS",
           "STATUS_FILE_OPEN_FAILED",
           "STATUS_FULL",
           "STATUS_IO_ERROR",
           "STATUS_NO_MEMORY",
           "STATUS_NO_PERMISSION",
           "STATUS_NOT_EXECUTABLE",
           "STATUS_NOT_FOUND",
           "STATUS_NOT_INITIALIZED",
           "STATUS_OUT_OF_RANGE",
           "STATUS_PARSE_ERROR",
           "STATUS_TIMED_OUT",
           "STATUS_TRY_AGAIN",
           "STATUS_NOT_SUPPORTED",
           "STATUS_FAILURE"]
