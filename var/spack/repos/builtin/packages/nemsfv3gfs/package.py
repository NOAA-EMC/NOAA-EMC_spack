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
#     spack install nemsfv3gfs
#
# You can edit this file again by typing:
#
#     spack edit nemsfv3gfs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Nemsfv3gfs(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    git = "gerrit:NEMSfv3gfs"

    # FIXME: Add proper versions and checksums here.
    version('1.0.0c', branch='cmake', submodules=True)

    # FIXME: Add dependencies if required.
    depends_on('hdf5+cxx+fortran+hl+mpi')
    depends_on('cmake@3.12.3')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('bacio')
    depends_on('zlib')
    depends_on('curl')
    depends_on('lapack')
    depends_on('sp')
    depends_on('w3nco')
    depends_on('esmf@8.0.0b')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ["-DCMAKE_BUILD_TYPE=RELEASE"]
        return args
