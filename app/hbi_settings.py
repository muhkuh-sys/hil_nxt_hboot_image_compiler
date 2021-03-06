# -*- coding: utf-8 -*-

# ***************************************************************************
# *   Copyright (C) 2019 by Hilscher GmbH                                   *
# *   netXsupport@hilscher.com                                              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU General Public License for more details.                          *
# *                                                                         *
# *   You should have received a copy of the GNU General Public License     *
# *   along with this program; if not, write to the                         *
# *   Free Software Foundation, Inc.,                                       *
# *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
# ***************************************************************************
import os
import sys
import platform


file_path = os.path.realpath(__file__)


if file_path.endswith(".py"):
    hbi_sources = os.path.dirname(os.path.dirname(file_path))
elif file_path.endswith(".pyc"):
    hbi_sources = os.path.dirname(file_path)

path_patch_tables = os.path.join(hbi_sources, "patch_tables")

cwd_ = os.path.dirname(hbi_sources)

plat = platform.system()
if plat == "Windows":
    elf_compiler_dir = os.path.join(hbi_sources, 'elf_compiler', 'arm-none-eabi-gcc', '4.9.3', 'bin')
    OBJCPY = os.path.join(elf_compiler_dir, 'arm-none-eabi-objcopy')
    OBJDUMP = os.path.join(elf_compiler_dir, 'arm-none-eabi-objdump')
    READELF = os.path.join(elf_compiler_dir, 'arm-none-eabi-readelf')
elif plat == "linux":
    OBJCPY = "objcopy"
    OBJDUMP = "objdump"
    READELF = "readelf"
else:
    OBJCPY = "objcopy"
    OBJDUMP = "objdump"
    READELF = "readelf"

# print(OBJCPY)
# print(OBJDUMP)
# print(READELF)

hbi_path = cwd_
sys.path.insert(0, hbi_path)
