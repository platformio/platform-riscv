# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Freedom E RISC-V SDK

Open Source Software for Developing on the Freedom E Platform

https://github.com/sifive/freedom-e-sdk
"""

from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-freedom-e-sdk")
assert FRAMEWORK_DIR and isdir(FRAMEWORK_DIR)

env.SConscript("_bare.py", exports="env")

env.Append(
    CCFLAGS=[
        "-include", "sys/cdefs.h"
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "drivers"),
        join(FRAMEWORK_DIR, "include"),
        join(FRAMEWORK_DIR, "env"),
        join(FRAMEWORK_DIR, "env", "$BOARD")
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "env", "$BOARD"),
    ]
)

#
# Target: Build Core Library
#

libs = [
    env.BuildLibrary(
        join("$BUILD_DIR", "sdk-libwrap"),
        join(FRAMEWORK_DIR, "libwrap")),

    env.BuildLibrary(
        join("$BUILD_DIR", "sdk-driver"),
        join(FRAMEWORK_DIR, "drivers", "plic")),

    env.BuildLibrary(
        join("$BUILD_DIR", "sdk-env"),
        join(FRAMEWORK_DIR, "env"),
        src_filter=env.subst("+<start.S> +<entry.S> +<$BOARD/init.c>"))
]

env.Prepend(LIBS=libs)
