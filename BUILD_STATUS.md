# Build status

Status: `configured_not_built_not_device_tested`

Target: OnePlus Ace 5 PKG110, stock ColorOS 16, SM8650, android14-6.1.141.
Official source commit message: PKG110_16.0.9.400(CN01).

No workflow has been dispatched for this repository. No kernel artifact or device boot result is claimed.

Prior upstream report: WildKernels release notes report boot failures for Ace 5 COS 16 / 6.1.141. Official issue #36 names ROM 16.0.7.200; this repository pins newer 16.0.9.400 sources. Whether this pinned revision is affected remains unverified. Source/config validation is not a boot qualification.
Issue: https://github.com/OnePlusOSS/android_kernel_common_oneplus_sm8650/issues/36
Source: https://github.com/WildKernels/OnePlus_KernelSU_SUSFS/releases

After a future build, retain the Actions run URL, built Git commit, source-manifest.xml, actual and embedded configs, receipt.json and archive SHA256 before updating this status. Device testing requires separate authorization and matching private recovery material.

Local checks passed: source pins and defaults, YAML parsing, syntax of all 46 workflow shell steps, Python syntax, exact dispatch defaults, and seven rejection cases (wrong model, KPM, KernelSU pin drift, disabled SUSFS, disabled BBG, suffix and build-time shell injection). No remote CI or kernel build was run.
