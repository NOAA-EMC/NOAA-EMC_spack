# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RIso(RPackage):
    """Linear order and unimodal order (univariate) isotonic regression;
    bivariate isotonic regression with linear order on both variables."""

    homepage = "https://cloud.r-project.org/package=Iso"
    url      = "https://cloud.r-project.org/src/contrib/Iso_0.0-17.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/Iso"

    version('0.0-18', sha256='2d7e8c4452653364ee086d95cea620c50378e30acfcff129b7261e1756a99504')
    version('0.0-17', 'bf99821efb6a44fa75fdbf5e5c4c91e4')

    depends_on('r@1.7.0:', type=('build', 'run'))
