# Build status

Status: `built_and_config_verified_not_device_tested`

Target: OnePlus Ace 5 PKG110, stock ColorOS 16, SM8650, android14-6.1.141.
Official source commit message: PKG110_16.0.9.400(CN01).

## Verified build

- Run: https://github.com/LIghtJUNction/ace5-kernelsu-next-susfs/actions/runs/38772621861
- Built source commit: `25feb02543d68df2fc1b0a096dc5b0d30c4409fb`.
- Result: success on the first attempt. Kernel compilation took 11 minutes 40 seconds; the complete workflow took about 17 minutes 33 seconds.
- Kernel: `6.1.141-android14-ace5-ksun-susfs`.
- KernelSU-Next: pinned pershoot/dev-susfs integration, driver version `33380`; not an unmodified official release tag.
- SUSFS: `v2.3.0`.
- Image: 36,493,824 bytes; SHA256 `23f0c074425a636b8b739e355747894b7feea0c42b2a161d490bf8544a10f929`.

## Artifact verification

Both GitHub artifact ZIP files were downloaded and matched the GitHub SHA256 digests. ZIP CRC checks and all 13 packaged file hashes passed. The Image's gzip-embedded configuration was extracted independently and matched the actual build configuration exactly. Kernel banner, source-manifest commits, receipt and built Git commit matched.

Required settings present: `CONFIG_KSU=y`, `CONFIG_KSU_SUSFS=y`, `CONFIG_KSU_SUSFS_SPOOF_CMDLINE_OR_BOOTCONFIG=y`, `CONFIG_BBG=y`, `CONFIG_IKCONFIG=y`, `CONFIG_KPROBES=y`. `CONFIG_KPM=y` is absent. The installer rejects non-PKG110 devices and non-Android-16 systems before loading the installer core.

| Archive | SHA256 |
| --- | --- |
| AnyKernel3_KernelSU-Next_33380_OnePlusAce5_Android16.0.0(6.1.141)_BBG_ILH.zip | `6352587c2c5189fa351ebe0eeeec10ea85f142e13e1646fcba1229279febda1b` |
| ace5-build-evidence-38772621861.zip | `b773e398e49a181e64ab1909d7946b850079fe8f14c1cc57a5689dc857d2a855` |

The receipt, configuration, pinned source manifest, archive checksums and local verification report are committed under `builds/38772621861/`. Full downloaded archives and build logs are retained locally under `.artifacts/build-38772621861/` (ignored by Git).

## Device qualification remains open

No phone was flashed, rebooted or modified. Build success does not establish that the kernel boots or that Root/SUSFS works on hardware.

Prior upstream report: WildKernels release notes report boot failures for Ace 5 COS 16 / 6.1.141. Official issue #36 names ROM 16.0.7.200; this repository pins newer 16.0.9.400 sources. Whether this pinned revision is affected remains unverified.

- Issue: https://github.com/OnePlusOSS/android_kernel_common_oneplus_sm8650/issues/36
- Source: https://github.com/WildKernels/OnePlus_KernelSU_SUSFS/releases

Local pre-build checks passed: source pins and workflow defaults, YAML parsing, all 46 workflow shell steps, Python syntax, dispatch defaults and seven invalid-input rejection cases. This run was the requested kernel artifact build; no separate automated CI was triggered.
