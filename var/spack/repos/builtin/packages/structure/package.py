# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Structure(MakefilePackage):
    """Structure is a free software package for using multi-locus genotype
       data to investigate population structure."""

    homepage = "http://web.stanford.edu/group/pritchardlab/structure.html"
    url      = "http://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v2.3.4/structure_kernel_source.tar.gz"

    version('2.3.4', '4e0591678cdbfe79347d272b5dceeda1')

    depends_on('jdk', type=('build', 'run'))

    def url_for_version(self, version):
        url = "http://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v{0}/structure_kernel_source.tar.gz"
        return url.format(version)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('structure', prefix.bin)
        install('mainparams', prefix.bin)
        install('extraparams', prefix.bin)
