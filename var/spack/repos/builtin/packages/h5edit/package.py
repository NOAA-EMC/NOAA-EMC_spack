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
#     spack install h5edit
#
# You can edit this file again by typing:
#
#     spack edit h5edit
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class H5edit(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://support.hdfgroup.org/ftp/HDF5/projects/jpss/h5edit/h5edit-1.3.1.tar.gz"

    version('1.3.1', sha256='57e2cc7cd67af82614e51064ee969ffa0a5328b8c58c4ed7085db32a8d99acef')

    # FIXME: Add dependencies if required.
    depends_on('hdf5')
#   depends_on('openmpi')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = ['CC=h5pcc','FC=mpifort','CXX=mpic++','F77=mpifort','HDF5_LDFLAGS="-L$HDF5/lib -lhdf5 -lhdf5_hl"']
        # args = ['CC=/discover/nobackup/mapotts1/GMAO-Baselibs/x86_64-unknown-linux-gnu/ifort_18.3.222-openmpi-gen/Linux/bin/h5pcc','FC=mpifort','CXX=mpic++','F77=mpifort']
#       args = ['CC=/gpfsm/dnb31/mapotts1/spack/opt/spack/linux-sles12-x86_64/intel-18.0.3/hdf5-1.10.4-nhzaq25wd7m6jbdwq64bt3ufxcbjlxth/bin/h5pcc','FC=mpifort','CXX=mpic++','F77=mpifort','LDFLAGS=-lhdf_hl']
        return args
