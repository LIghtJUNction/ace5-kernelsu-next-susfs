# Ace 5 · KernelSU-Next + SUSFS · Android 16

面向一加 Ace 5 **PKG110 / 原厂 ColorOS 16** 的个人维护仓库。以 [Numbersf/Action-Build 的 KernelSU-Next 分支](https://github.com/Numbersf/Action-Build/tree/KernelSU-Next)为基础，沿用 [ace2-kernelsu-susfs](https://github.com/LIghtJUNction/ace2-kernelsu-susfs) 的源码锁定、机型限制和产物核验方式。上游说明和许可证保留在 README.upstream.md 与 LICENSE。

## 构建目标

- 一加官方 `oneplus/sm8650_b_16.0.0_ace_5` 源码，发布说明对应 `PKG110_16.0.9.400(CN01)`，内核 **6.1.141 / android14-6.1**。Android 16 是手机系统版本，`android14-6.1` 是内核接口分支，两者不矛盾。
- [pershoot/KernelSU-Next 的 dev-susfs 分支](https://github.com/pershoot/KernelSU-Next/tree/dev-susfs)：这是 KernelSU-Next 的 SUSFS 集成分支，不是未修改的官方发行标签。驱动源码和计算版本号所需的基线均锁定提交。
- SUSFS **v2.3.0**，关键分区写入保护 BBG。无 KPM/KPN、额外调度器、网络调优、ZRAM 修改或管理器/模块自动安装。
- 仅适用于标准版 Ace 5；不适用于 Ace 5 Pro、竞速版、至尊版或 OnePlus 13R。

## 当前状态

**仓库配置已建立，尚未编译或通过真机验证，不能当作可用刷机包。**

[WildKernels 的发布说明](https://github.com/WildKernels/OnePlus_KernelSU_SUSFS/releases)曾报告 Ace 5 ColorOS 16 / 6.1.141 源码编译后不能启动；[官方仓库 issue #36](https://github.com/OnePlusOSS/android_kernel_common_oneplus_sm8650/issues/36)涉及 16.0.7.200。本仓库锁定的是较新的 16.0.9.400 源码，尚未确认该问题是否仍影响本次提交。即使构建通过，也必须维持“未验证启动”状态；详见 BUILD_STATUS.md。

## 使用与维护

1. 所有源码提交见 `sources.lock.json`，一加源码清单见 `manifests/oneplus_ace5_b.xml`。
2. 本地运行 `python3 scripts/validate_ace5.py` 检查默认参数及来源。维护分支为 `ace5-kernelsu-next-susfs`。
3. 在 Actions 手动运行 **Build Ace 5 - KernelSU-Next and SUSFS**。工作流仅手动触发，拒绝偏离固定来源、机型或基础配置的参数。
4. 构建将产出 AnyKernel3 和 `ace5-build-evidence`；后者记录实际配置、镜像内嵌配置、源码清单与文件 SHA256。只有核验通过才能标记为 `built_and_config_verified_not_device_tested`。

AnyKernel3 安装脚本会在写分区前检查 PKG110 和 Android 16。该检查不能证明与任意 ColorOS 16 版本兼容。仓库不自动刷机，不含设备备份，也没有执行过真机操作。维护时比较上游 **KernelSU-Next** 分支，避免合入默认 SukiSU-Ultra 分支。
