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
#     spack install post
#
# You can edit this file again by typing:
#
#     spack edit post
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Post(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    git = "gerrit:EMC_post"

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
    version('8.1.0', branch='spack-build', submodules=False)

    # FIXME: Add dependencies if required.
    depends_on('hdf5+cxx+fortran+hl+mpi')
    depends_on('cmake@3.13.1')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('jasper')
    depends_on('lapack')
    depends_on('libpng')
    depends_on('ip')
    depends_on('sp')
    depends_on('g2')
    depends_on('g2tmpl')
    depends_on('sfcio')
    depends_on('gfsio')
    depends_on('nemsio')
    depends_on('crtm')
    depends_on('zlib')
    depends_on('curl')
    depends_on('w3nco')
    depends_on('w3emc')
    depends_on('grib-util')
    depends_on('esmf@8.0.0b')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
