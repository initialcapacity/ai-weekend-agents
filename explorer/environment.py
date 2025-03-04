import os
from dataclasses import dataclass


@dataclass
class Environment:
    open_ai_key: str
    github_token: str
    root_log_level: str
    httpx_log_level: str
    explorer_log_level: str

    @classmethod
    def from_env(cls) -> 'Environment':
        return cls(
            open_ai_key=require_env('OPEN_AI_KEY'),
            github_token=require_env('GITHUB_TOKEN'),
            root_log_level=os.environ.get('ROOT_LOG_LEVEL', 'INFO'),
            httpx_log_level=os.environ.get('HTTPX_LOG_LEVEL', 'WARN'),
            explorer_log_level=os.environ.get('EXPLORER_LOG_LEVEL', 'INFO'),
        )

def require_env(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise Exception(f'Unable to read {name} from the environment')
    return value
