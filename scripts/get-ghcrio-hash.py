#!/usr/bin/env python3

import argparse
import os

import requests as rq

GHCR_TOKEN = ""


def get_image_hash(namespace: str, repository: str, tag: str, is_org: bool) -> str:
    url = ""
    if is_org:
        url = f"https://api.github.com/orgs/{namespace}/packages/container/{repository}/versions"
    else:
        url = f"https://api.github.com/users/{namespace}/packages/container/{repository}/versions"
    headers = {
        "Authorization": f"Bearer {GHCR_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-Github-Api-Version": "2022-11-28",
    }
        
    resp = rq.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"Failed to get image hash with code: {resp.status_code} and err: {resp.text}"
        )
        
    for image in resp.json():
        if tag in image["metadata"]["container"]["tags"]:
            return image["name"]
    raise Exception(
        f"No image found for the given tag {tag}"
    )
        


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
        "--tag",
        type=str,
        default="latest",
        help="The tag of the image",
    )
    args_parser.add_argument(
        "--org", action="store_true", help="If the image is in an organization"
    )

    args = args_parser.parse_args()

    if os.getenv("GHCR_TOKEN") is not None:
        GHCR_TOKEN = os.getenv("GHCR_TOKEN")

    image_hash = get_image_hash(args.namespace, args.repo, args.tag, args.org)
    print(image_hash)
