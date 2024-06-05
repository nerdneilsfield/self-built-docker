#!/usr/bin/env python3

import argparse
import os

import requests as rq

GHCR_TOKEN = ""


def get_repo_tag(namespace: str, repository: str, tag_name: str = "") -> str:
    url = ""
    if tag_name == "":
        url = f"https://api.github.com/repos/{namespace}/{repository}/releases/latest"
    else:
        url = f"https://api.github.com/repos/{namespace}/{repository}/releases"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28",
    }

    if GHCR_TOKEN != "":
        headers["Authorization"] = f"Bearer {GHCR_TOKEN}"

    resp = rq.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"Failed to get github tag with code: {resp.status_code} and err: {resp.text}"
        )

    if tag_name == "":
        return resp.json()["tag_name"]
    else:
        for release in resp.json():
            if release["tag_name"] == tag_name:
                return release["tag_name"]
        raise Exception(f"Failed to find tag: {tag_name} in releases")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser(
        description="Get the latest version of a github repository",
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
        "--tag",
        type=str,
        default="",
        help="The tag of the image",
    )

    args = args_parser.parse_args()

    if os.getenv("GHCR_TOKEN") is not None:
        GHCR_TOKEN = os.getenv("GHCR_TOKEN")

    repo_tag = get_repo_tag(args.namespace, args.repo, args.tag)
    print(repo_tag)
