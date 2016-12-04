from invoke import task
import subprocess


@task
def serve(ctx):
    subprocess.call('python -m http.server 8000', shell=True)
