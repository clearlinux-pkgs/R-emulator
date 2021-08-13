#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-emulator
Version  : 1.2.21
Release  : 31
URL      : https://cran.r-project.org/src/contrib/emulator_1.2-21.tar.gz
Source0  : https://cran.r-project.org/src/contrib/emulator_1.2-21.tar.gz
Summary  : Bayesian Emulation of Computer Programs
Group    : Development/Tools
License  : GPL-2.0
Requires: R-mvtnorm
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

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
%setup -q -c -n emulator
cd %{_builddir}/emulator

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619386652

%install
export SOURCE_DATE_EPOCH=1619386652
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emulator
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emulator
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library emulator
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc emulator || :


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
/usr/lib64/R/library/emulator/doc/quad_form_test.R
/usr/lib64/R/library/emulator/doc/quad_form_test.Rmd
/usr/lib64/R/library/emulator/doc/quad_form_test.html
/usr/lib64/R/library/emulator/doc/uncertainty.bib
/usr/lib64/R/library/emulator/help/AnIndex
/usr/lib64/R/library/emulator/help/aliases.rds
/usr/lib64/R/library/emulator/help/emulator.rdb
/usr/lib64/R/library/emulator/help/emulator.rdx
/usr/lib64/R/library/emulator/help/paths.rds
/usr/lib64/R/library/emulator/html/00Index.html
/usr/lib64/R/library/emulator/html/R.css
