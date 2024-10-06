from typing import List
from ..domain.models import Auth
import requests
from ..domain.interfaces.auth_repository import AuthRepository
from ..infrastructure.mappers import AuthnMapper
import uuid
from datetime import datetime
from ..utils import Logger
from  config import Config

class AuthService:
    def __init__(self, auth_repository: AuthRepository=None):
        self.log = Logger()
        self.auth_repository=auth_repository

    