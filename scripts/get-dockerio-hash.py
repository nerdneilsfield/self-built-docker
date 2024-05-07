#!/usr/bin/env python3

import argparse
import os

import requests as rq

DOCKER_TOKEN = ""


def get_image_hash(
    namespace: str, repository: str, tag: str, arch: str, system_os: str
) -> str:
    url = f"https://hub.docker.com/v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}"
    headers = {"Authorization": f"Bearer {DOCKER_TOKEN}"}
    resp = rq.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f"Failed to get image hash with code: {resp.status_code} and err: {resp.text}"
        )

    for image in resp.json()["images"]:
        if image["os"] == system_os and image["architecture"] == arch:
            return image["digest"]
    raise Exception(
        f"No image found for the given architecture {arch} and os {system_os}"
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
        "--arch",
        type=str,
        default="amd64",
        help="The architecture of the image",
    )
    args_parser.add_argument(
        "--os",
        type=str,
        default="linux",
        help="The operating system of the image",
    )

    args = args_parser.parse_args()

    if os.getenv("DOCKER_TOKEN") is not None:
        DOCKER_TOKEN = os.getenv("DOCKER_TOKEN")

    image_hash = get_image_hash(args.namespace, args.repo, args.tag, args.arch, args.os)
    print(image_hash)
