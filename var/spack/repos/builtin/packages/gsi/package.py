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
#     spack install gsi
#
# You can edit this file again by typing:
#
#     spack edit gsi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gsi(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://vlab.ncep.noaa.gov/redmine/projects/comgsi"
    git      = "gerrit:ProdGSI"

#   version('master', branch='hera-build', submodules=True)
    version('master', branch='spack-build', submodules=True)

#   parallel = False
#   depends_on('gcc')
    depends_on('hdf5+hl+cxx+fortran+mpi')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('bacio')
    depends_on('bufr')
    depends_on('crtm')
    depends_on('nemsio')
    depends_on('sp')
    depends_on('sfcio')
    depends_on('sigio')
    depends_on('w3emc')
    depends_on('w3nco')
    depends_on('lapack')
    depends_on('curl')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DBUILD_CORELIBS=OFF']
        return args
