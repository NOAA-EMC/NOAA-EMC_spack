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
#     spack install gmaobaselibs
#
# You can edit this file again by typing:
#
#     spack edit gmaobaselibs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gmaobaselibs(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "gmaobaselibs.1.0.tar.gz"

    # FIXME: Add proper versions and checksums here.
    version('1.0', 'a9360cfe1882d82305197ac8c94d1cd3')

    # FIXME: Add dependencies if required.
    depends_on('mpi')
    depends_on('cmor')
#   depends_on('curl')
    depends_on('hdf')
    depends_on('hdf5+threadsafe')
    depends_on('netcdf')
    depends_on('netcdf-fortran')
    depends_on('szlib')
    depends_on('zlib')
    depends_on('esmf')
#   depends_on('uuid')
    depends_on('h5edit')
    depends_on('nco')
    depends_on('hdf-eos')
    depends_on('hdf5eos')
    depends_on('cdo')
#   depends_on('udunits2')
    depends_on('sdptoolkit')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
#       make()
        make('install')
