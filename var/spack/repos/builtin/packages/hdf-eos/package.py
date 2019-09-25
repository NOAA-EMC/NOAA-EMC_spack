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
#     spack install hdf-eos
#
# You can edit this file again by typing:
#
#     spack edit hdf-eos
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class HdfEos(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://observer.gsfc.nasa.gov/ftp/edhs/hdfeos/latest_release/HDF-EOS2.20v1.00.tar.Z"

    version('2.20v1.00',            sha256='cb0f900d2732ab01e51284d6c9e90d0e852d61bba9bce3b43af0430ab5414903')

    # FIXME: Add dependencies if required.
    depends_on('hdf')
    depends_on('libjpeg-turbo')

    def configure_args(self):
        # FIXME: Unknown build system
	args = ['--enable-install-include']
	return args
