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
#     spack install hdf5eos
#
# You can edit this file again by typing:
#
#     spack edit hdf5eos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Hdf5eos(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://observer.gsfc.nasa.gov/ftp/edhs/hdfeos5/latest_release/HDF-EOS5.1.16.tar.Z"

    version('5.1.16',             sha256='7054de24b90b6d9533329ef8dc89912c5227c83fb447792103279364e13dd452')

    # FIXME: Add dependencies if required.
    depends_on('hdf5')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = ['--enable-install-include']
        return args
