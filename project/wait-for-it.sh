#!/usr/bin/env bash
# Use this script to wait for a given host and port to become available

set -e

host="$1"
shift
port="$1"
shift

echo "Waiting for ${host}:${port}..."

while ! nc -z "${host}" "${port}"; do
  sleep 1
done

echo "Connected to ${host}:${port}"

exec "$@"
