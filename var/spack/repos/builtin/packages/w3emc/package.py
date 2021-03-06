# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install w3emc
#
# You can edit this file again by typing:
#
#     spack edit w3emc
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class W3emc(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    git      = "git@github.com:NOAA-EMC/NCEPLIBS-w3emc.git"

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('v2.2.0',  branch='release/public-v1')

    # FIXME: Add dependencies if required.
    depends_on('sigio')
    depends_on('bufr')
    depends_on('bacio')
    depends_on('sfcio')
    depends_on('nemsio')
    depends_on('sp')
    depends_on('w3nco')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DCMAKE_BUILD_TYPE=RELEASE']
        return args
