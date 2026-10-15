"""Check the maintained target, immutable source pins and dispatch inputs."""
import json
import os
import pathlib
import re
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / "sources.lock.json").read_text())
workflow = (ROOT / ".github/workflows/ace5.yml").read_text()
manifest = ET.parse(ROOT / "manifests/oneplus_ace5_b.xml")
projects = {p.get("name"): p for p in manifest.findall("project")}
for name, sha in lock["kernel_projects"].items():
    assert projects[name].get("revision") == sha, name
    assert projects[name].get("upstream") == "oneplus/sm8650_b_16.0.0_ace_5", name
for p in projects.values():
    assert re.fullmatch(r"[0-9a-f]{40}", p.get("revision", "")), p.get("name")
for key in ("upstream_workflow", "kernelsu", "kernelsu_base", "susfs", "manifest", "anykernel3", "baseband_guard"):
    assert re.fullmatch(r"[0-9a-f]{40}", lock[key]), key
for key in ("kernelsu", "kernelsu_base", "susfs", "manifest", "anykernel3", "baseband_guard"):
    assert lock[key] in workflow, f"Workflow pin drift: {key}"
assert lock["kernelsu_repository"] == "pershoot/KernelSU-Next"
assert lock["kernelsu_branch"] == "dev-susfs"
assert "https://github.com/pershoot/KernelSU-Next.git" in workflow
assert "CPUD=pineapple" in workflow and "CPU=sm8650" in workflow
assert "MANIFEST_BRANCH=oneplus/sm8650" in workflow
expected = {
    "FILE": "oneplus_ace5_b", "KPM": "N/A", "SUSFS_META": lock["susfs"],
    "KSU_META": "dev/dev-susfs/" + lock["kernelsu"], "SUSFS_CI": "N/A",
    "DYNAMIC_REPO": "Numbersf", "BUILD_TIME": "F", "ZRAM": "0/lz4kd/8589934592",
    "SUFFIX": "ace5-ksun-susfs", "RESUBLEVEL": "", "FAST_BUILD": True,
    "LSM_BBG": True, "BUILD_NOCACHE": True,
}
for key in ("LZ4_UPDATE", "NETFILTER", "CCM", "UNICODE_BYPASS", "SCHED_HMBIRD", "DROID_SPACES", "RE_KERNEL", "SUSFS_DEV", "SPACE_NOCLEAN"):
    expected[key] = False
# Parse defaults without requiring third-party packages on the Actions runner.
blocks = re.findall(r"^      ([A-Z0-9_]+):\n(.*?)(?=^      [A-Z0-9_]+:|^jobs:)", workflow, re.M | re.S)
defaults = {}
for key, body in blocks:
    match = re.search(r"^        default: ?(.*)$", body, re.M)
    assert match, f"Missing default: {key}"
    raw = match.group(1).strip()
    defaults[key] = raw.strip('"')
def normalize(value):
    return str(value).lower() if isinstance(value, bool) else str(value)
assert defaults == {k: normalize(v) for k, v in expected.items()}, "Workflow defaults drifted"
if os.environ.get("GITHUB_EVENT_PATH"):
    event = json.loads(pathlib.Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    inputs = event.get("inputs", {})
    assert set(inputs) <= set(expected), "Unknown input"
    for key, value in expected.items():
        assert normalize(inputs.get(key, "")) == normalize(value), f"Unsupported input: {key}"
print("Ace 5 source pins, workflow defaults and baseline inputs verified")
