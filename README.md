# RISC-V: development platform for [PlatformIO](http://platformio.org)
[![Build Status](https://travis-ci.org/platformio/platform-riscv.svg?branch=develop)](https://travis-ci.org/platformio/platform-riscv)
[![Build status](https://ci.appveyor.com/api/projects/status/bg71nvtdwpy989n9/branch/develop?svg=true)](https://ci.appveyor.com/project/ivankravets/platform-riscv/branch/develop)

RISC-V is an open, free ISA enabling a new era of processor innovation through open standard collaboration. Born in academia and research, RISC-V ISA delivers a new level of free, extensible software and hardware freedom on architecture, paving the way for the next 50 years of computing design and innovation.

* [Home](http://platformio.org/platforms/riscv) (home page in PlatformIO Platform Registry)
* [Documentation](http://docs.platformio.org/page/platforms/riscv.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = riscv
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-riscv.git
board = ...
...
```

# Configuration

Please navigate to [documentation](http://docs.platformio.org/page/platforms/riscv.html).
