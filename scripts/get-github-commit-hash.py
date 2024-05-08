#!/usr/bin/env python3

import argparse
import os

import requests as rq

GHCR_TOKEN = ""


def get_commit_hash(namespace: str, repository: str, branch: str) -> str:

    url = f"https://api.github.com/repos/{namespace}/{repository}/branches/{branch}"
    headers = {
        "Authorization": f"Bearer {GHCR_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28",
    }

    resp = rq.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"Failed to get commit hash with code: {resp.status_code} and err: {resp.text}, check the give branch whether {branch} and repo {repository} exists in the given namespace {namespace}"
        )

    return resp.json()["commit"]["sha"]


if __name__ == "__main__":

    args_parser = argparse.ArgumentParser(
        description="Get the hash of a docker image from docker.io"
    )
    args_parser.add_argument(
        "--repo",
        type=str,
        required=True,
        default="helloworld",
        help="The repo to get the hash of",
    )
    args_parser.add_argument(
        "--namespace",
        type=str,
        default="library",
        help="The namespace of the image",
    )
    args_parser.add_argument(
        "--branch",
        type=str,
        default="main",
        help="The branch of the image",
    )

    args = args_parser.parse_args()

    if os.getenv("GHCR_TOKEN") is not None:
        GHCR_TOKEN = os.getenv("GHCR_TOKEN")
    else:
        raise Exception("GHCR_TOKEN not set")

    image_hash = get_commit_hash(args.namespace, args.repo, args.branch)
    print(image_hash)
