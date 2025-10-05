import os
import environ
from pathlib import Path
from django.http import JsonResponse
from rest_framework.decorators import api_view

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
print("BASE_DIR: ", BASE_DIR)

env_file_path = os.path.join(BASE_DIR, '.env')
print("env_file_path: ", env_file_path)


@api_view(['GET'])
def fetch_environment_variables(request):
    env_variables = {}
    env.read_env(env_file=env_file_path)

    with open(env_file_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            print(line)
            if line and not line.startswith('#'):
                key, value = line.split('=', maxsplit=1)
                print(f"key: {key}, value: {value}")
                env_variables[key] = value
                print()
    print("env_variables: ", env_variables)
    return JsonResponse(env_variables)


# fetch_environment_variables()
