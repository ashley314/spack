# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import os
import sys

from spack import *

class JediMpasEnv(BundlePackage):
    """Development environment for mpas-bundle"""

    homepage = "https://github.com/JCSDA/mpas-bundle"
    git      = "https://github.com/JCSDA/mpas-bundle.git"

    maintainers = ['climbfuji', 'rhoneyager']

    version('main')

    depends_on('base-env',          type='run')
    depends_on('jedi-base-env',     type='run')

    # Anything missing?
