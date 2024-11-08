#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : R-emulator
Version  : 1.2.24
Release  : 47
URL      : https://cran.r-project.org/src/contrib/emulator_1.2-24.tar.gz
Source0  : https://cran.r-project.org/src/contrib/emulator_1.2-24.tar.gz
Summary  : Bayesian Emulation of Computer Programs
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mvtnorm
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Allows one to estimate the output of a computer program,
 as a function of the input parameters, without actually running it.
 The computer program is assumed to be a Gaussian process, whose
 parameters are estimated using Bayesian techniques that give a PDF of
 expected program output.  This PDF is conditional on a training set
 of runs, each consisting of a point in parameter space and the model
 output at that point.  The emphasis is on complex codes that take
 weeks or months to run, and that have a large number of undetermined
 input parameters; many climate prediction models fall into this
 class.  The emulator essentially determines Bayesian posterior
 estimates of the PDF of the output of a model, conditioned on results
 from previous runs and a user-specified prior linear model.  The
 package includes functionality to evaluate quadratic forms 
 efficiently.

%prep
%setup -q -n emulator
pushd ..
cp -a emulator buildavx2
popd
pushd ..
cp -a emulator buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711241846

%install
export SOURCE_DATE_EPOCH=1711241846
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/emulator/CITATION
/usr/lib64/R/library/emulator/DESCRIPTION
/usr/lib64/R/library/emulator/INDEX
/usr/lib64/R/library/emulator/Meta/Rd.rds
/usr/lib64/R/library/emulator/Meta/data.rds
/usr/lib64/R/library/emulator/Meta/features.rds
/usr/lib64/R/library/emulator/Meta/hsearch.rds
/usr/lib64/R/library/emulator/Meta/links.rds
/usr/lib64/R/library/emulator/Meta/nsInfo.rds
/usr/lib64/R/library/emulator/Meta/package.rds
/usr/lib64/R/library/emulator/Meta/vignette.rds
/usr/lib64/R/library/emulator/NAMESPACE
/usr/lib64/R/library/emulator/R/emulator
/usr/lib64/R/library/emulator/R/emulator.rdb
/usr/lib64/R/library/emulator/R/emulator.rdx
/usr/lib64/R/library/emulator/data/expert.estimates.rda
/usr/lib64/R/library/emulator/data/results.table.rda
/usr/lib64/R/library/emulator/data/toy.rda
/usr/lib64/R/library/emulator/doc/emulex.R
/usr/lib64/R/library/emulator/doc/emulex.Rnw
/usr/lib64/R/library/emulator/doc/emulex.pdf
/usr/lib64/R/library/emulator/doc/index.html
/usr/lib64/R/library/emulator/doc/uncertainty.bib
/usr/lib64/R/library/emulator/emulator_stickermaker.R
/usr/lib64/R/library/emulator/help/AnIndex
/usr/lib64/R/library/emulator/help/aliases.rds
/usr/lib64/R/library/emulator/help/emulator.rdb
/usr/lib64/R/library/emulator/help/emulator.rdx
/usr/lib64/R/library/emulator/help/figures/emulator.png
/usr/lib64/R/library/emulator/help/paths.rds
/usr/lib64/R/library/emulator/html/00Index.html
/usr/lib64/R/library/emulator/html/R.css
/usr/lib64/R/library/emulator/quad_form_test.Rmd
