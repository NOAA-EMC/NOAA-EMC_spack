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
#     spack install sdptoolkit
#
# You can edit this file again by typing:
#
#     spack edit sdptoolkit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os


class Sdptoolkit(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://observer.gsfc.nasa.gov/ftp/edhs/sdptk/latest_release/SDPTK5.2.20v1.01.tar.Z"

    version('5.2.20v1.01',             sha256='a7ccbb33de2fddf1bafb718cd2d57b9f7ea0416cd80ccb4cf03bd1ec9080d96b')

    # FIXME: Add dependencies if required.
    depends_on('hdf')
    depends_on('hdf5')
    depends_on('hdf-eos')
    depends_on('hdf5eos')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
	hdf = os.getenv("HDF")
	hdfeos2 = os.getenv("HDF_EOS")
	hdfeos5 = os.getenv("HDF5EOS")
	hdf_flag = '--with-hdf4='+hdf
	hdfeos2_flag = '--with-hdfeos2='+hdfeos2
	hdfeos5_flag = '--with-hdfeos5='+hdfeos5
        args = [hdf_flag,hdfeos2_flag,hdfeos5_flag]
        return args
