import os
import socket
from pathlib import Path

assert not any(
    name.startswith(("GITHUB_", "ACTIONS_", "OPENAI_", "RENDER_", "AWS_"))
    or name in {"DATABASE_URL", "KAYA_SECRET_CANARY"}
    for name in os.environ
)
for forbidden in (
    "/tmp/kaya-host-canary-file",
    "/var/run/docker.sock",
    "/home/runner/.docker/config.json",
    "/work/.git",
):
    assert not Path(forbidden).exists()
assert len(list(Path("/proc").glob("[0-9]*"))) < 16
for address, port in (("169.254.169.254", 80), ("10.0.0.1", 5432), ("1.1.1.1", 443)):
    with socket.socket() as client:
        client.settimeout(0.2)
        assert client.connect_ex((address, port)) != 0
try:
    Path("/work/evidence.json").write_text('{"passed":true}')
except OSError:
    pass
else:
    raise AssertionError("Read-only source is writable")
Path("/tmp/evidence.json").write_text('{"passed":true}')
print("::error::CANDIDATE_OUTPUT_MUST_NOT_REACH_RUNNER_COMMANDS")
