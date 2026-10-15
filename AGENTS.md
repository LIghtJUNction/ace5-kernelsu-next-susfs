# Ace 5 maintenance rules

- Target only OnePlus Ace 5 PKG110, stock ColorOS 16, SM8650, android14-6.1.141. Pro, Racing, Ultra and 13R are separate targets.
- Use the locked pershoot/KernelSU-Next dev-susfs integration. Do not describe it as an unmodified official KernelSU-Next release.
- Read sources.lock.json before source changes. Preserve upstream licenses and attribution.
- Baseline: KernelSU-Next, SUSFS, critical-partition write protection. No KPM/KPN, network, scheduler, ZRAM or automatic APK/module installation.
- Run scripts/validate_ace5.py, parse YAML and check embedded shell syntax locally before pushing.
- Artifacts must pass scripts/verify_ace5_build.py. Keep actual and embedded config, source manifest, revision and SHA256 receipts.
- No successful build proves device compatibility. See BUILD_STATUS.md for the known upstream boot issue.
- Building does not authorize flashing, rebooting, installing modules or modifying ABL/efisp. Keep device backups private.
