#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-insight
Version  : 0.17.1
Release  : 36
URL      : https://cran.r-project.org/src/contrib/insight_0.17.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/insight_0.17.1.tar.gz
Summary  : Easy Access to Model Information for Various Model Objects
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-JM
BuildRequires : buildreq-R

%description
access to information contained in various R models, like model
    formulas, model terms, information about random effects, data that was
    used to fit the model or data from response variables. 'insight'

%prep
%setup -q -c -n insight
cd %{_builddir}/insight

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652461388

%install
export SOURCE_DATE_EPOCH=1652461388
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library insight
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library insight
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library insight
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc insight || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/insight/CITATION
/usr/lib64/R/library/insight/DESCRIPTION
/usr/lib64/R/library/insight/INDEX
/usr/lib64/R/library/insight/Meta/Rd.rds
/usr/lib64/R/library/insight/Meta/data.rds
/usr/lib64/R/library/insight/Meta/features.rds
/usr/lib64/R/library/insight/Meta/hsearch.rds
/usr/lib64/R/library/insight/Meta/links.rds
/usr/lib64/R/library/insight/Meta/nsInfo.rds
/usr/lib64/R/library/insight/Meta/package.rds
/usr/lib64/R/library/insight/Meta/vignette.rds
/usr/lib64/R/library/insight/NAMESPACE
/usr/lib64/R/library/insight/NEWS.md
/usr/lib64/R/library/insight/R/insight
/usr/lib64/R/library/insight/R/insight.rdb
/usr/lib64/R/library/insight/R/insight.rdx
/usr/lib64/R/library/insight/WORDLIST
/usr/lib64/R/library/insight/data/fish.RData
/usr/lib64/R/library/insight/doc/display.R
/usr/lib64/R/library/insight/doc/display.Rmd
/usr/lib64/R/library/insight/doc/display.html
/usr/lib64/R/library/insight/doc/export.R
/usr/lib64/R/library/insight/doc/export.Rmd
/usr/lib64/R/library/insight/doc/export.html
/usr/lib64/R/library/insight/doc/index.html
/usr/lib64/R/library/insight/doc/insight.R
/usr/lib64/R/library/insight/doc/insight.Rmd
/usr/lib64/R/library/insight/doc/insight.html
/usr/lib64/R/library/insight/help/AnIndex
/usr/lib64/R/library/insight/help/aliases.rds
/usr/lib64/R/library/insight/help/figures/logo.png
/usr/lib64/R/library/insight/help/insight.rdb
/usr/lib64/R/library/insight/help/insight.rdx
/usr/lib64/R/library/insight/help/paths.rds
/usr/lib64/R/library/insight/html/00Index.html
/usr/lib64/R/library/insight/html/R.css
/usr/lib64/R/library/insight/tests/spelling.R
/usr/lib64/R/library/insight/tests/testthat.R
/usr/lib64/R/library/insight/tests/testthat/helper-requiet.R
/usr/lib64/R/library/insight/tests/testthat/test-BayesFactorBF.R
/usr/lib64/R/library/insight/tests/testthat/test-FE-formula.R
/usr/lib64/R/library/insight/tests/testthat/test-GLMMadaptive.R
/usr/lib64/R/library/insight/tests/testthat/test-Gam2.R
/usr/lib64/R/library/insight/tests/testthat/test-LORgee.R
/usr/lib64/R/library/insight/tests/testthat/test-MCMCglmm.R
/usr/lib64/R/library/insight/tests/testthat/test-afex_aov.R
/usr/lib64/R/library/insight/tests/testthat/test-all_models_equal.R
/usr/lib64/R/library/insight/tests/testthat/test-aovlist.R
/usr/lib64/R/library/insight/tests/testthat/test-backticks.R
/usr/lib64/R/library/insight/tests/testthat/test-betabin.R
/usr/lib64/R/library/insight/tests/testthat/test-betareg.R
/usr/lib64/R/library/insight/tests/testthat/test-bife.R
/usr/lib64/R/library/insight/tests/testthat/test-bigglm.R
/usr/lib64/R/library/insight/tests/testthat/test-blmer.R
/usr/lib64/R/library/insight/tests/testthat/test-brms.R
/usr/lib64/R/library/insight/tests/testthat/test-censReg.R
/usr/lib64/R/library/insight/tests/testthat/test-cgam.R
/usr/lib64/R/library/insight/tests/testthat/test-check_if_installed.R
/usr/lib64/R/library/insight/tests/testthat/test-clean_names.R
/usr/lib64/R/library/insight/tests/testthat/test-clm.R
/usr/lib64/R/library/insight/tests/testthat/test-clm2.R
/usr/lib64/R/library/insight/tests/testthat/test-clmm.R
/usr/lib64/R/library/insight/tests/testthat/test-compact-character.R
/usr/lib64/R/library/insight/tests/testthat/test-compact-list.R
/usr/lib64/R/library/insight/tests/testthat/test-coxme.R
/usr/lib64/R/library/insight/tests/testthat/test-coxph.R
/usr/lib64/R/library/insight/tests/testthat/test-cpglmm.R
/usr/lib64/R/library/insight/tests/testthat/test-crch.R
/usr/lib64/R/library/insight/tests/testthat/test-crq.R
/usr/lib64/R/library/insight/tests/testthat/test-data.frame.R
/usr/lib64/R/library/insight/tests/testthat/test-ellipses_info.R
/usr/lib64/R/library/insight/tests/testthat/test-emmeans.R
/usr/lib64/R/library/insight/tests/testthat/test-epiR.R
/usr/lib64/R/library/insight/tests/testthat/test-export_table.R
/usr/lib64/R/library/insight/tests/testthat/test-feis.R
/usr/lib64/R/library/insight/tests/testthat/test-felm.R
/usr/lib64/R/library/insight/tests/testthat/test-find_formula-data.R
/usr/lib64/R/library/insight/tests/testthat/test-find_predictor_nested_re.R
/usr/lib64/R/library/insight/tests/testthat/test-find_predictors-strata.R
/usr/lib64/R/library/insight/tests/testthat/test-find_random.R
/usr/lib64/R/library/insight/tests/testthat/test-find_response.R
/usr/lib64/R/library/insight/tests/testthat/test-find_smooth.R
/usr/lib64/R/library/insight/tests/testthat/test-find_terms.R
/usr/lib64/R/library/insight/tests/testthat/test-fixest.R
/usr/lib64/R/library/insight/tests/testthat/test-format.R
/usr/lib64/R/library/insight/tests/testthat/test-format_capitalize.R
/usr/lib64/R/library/insight/tests/testthat/test-format_table_ci.R
/usr/lib64/R/library/insight/tests/testthat/test-formatting.R
/usr/lib64/R/library/insight/tests/testthat/test-gam.R
/usr/lib64/R/library/insight/tests/testthat/test-gamlss.R
/usr/lib64/R/library/insight/tests/testthat/test-gamm.R
/usr/lib64/R/library/insight/tests/testthat/test-gamm4.R
/usr/lib64/R/library/insight/tests/testthat/test-gbm.R
/usr/lib64/R/library/insight/tests/testthat/test-gee.R
/usr/lib64/R/library/insight/tests/testthat/test-geeglm.R
/usr/lib64/R/library/insight/tests/testthat/test-get_auxiliary.R
/usr/lib64/R/library/insight/tests/testthat/test-get_data.R
/usr/lib64/R/library/insight/tests/testthat/test-get_datagrid.R
/usr/lib64/R/library/insight/tests/testthat/test-get_deviance.R
/usr/lib64/R/library/insight/tests/testthat/test-get_loglikelihood.R
/usr/lib64/R/library/insight/tests/testthat/test-get_modelmatrix-estimatr.R
/usr/lib64/R/library/insight/tests/testthat/test-get_predicted-iv.R
/usr/lib64/R/library/insight/tests/testthat/test-get_predicted.R
/usr/lib64/R/library/insight/tests/testthat/test-get_priors.R
/usr/lib64/R/library/insight/tests/testthat/test-get_residuals.R
/usr/lib64/R/library/insight/tests/testthat/test-get_varcov.R
/usr/lib64/R/library/insight/tests/testthat/test-get_variance.R
/usr/lib64/R/library/insight/tests/testthat/test-get_weights.R
/usr/lib64/R/library/insight/tests/testthat/test-glm.R
/usr/lib64/R/library/insight/tests/testthat/test-glmmTMB.R
/usr/lib64/R/library/insight/tests/testthat/test-glmrob_base.R
/usr/lib64/R/library/insight/tests/testthat/test-gls.R
/usr/lib64/R/library/insight/tests/testthat/test-gmnl.R
/usr/lib64/R/library/insight/tests/testthat/test-has_intercept.R
/usr/lib64/R/library/insight/tests/testthat/test-htest.R
/usr/lib64/R/library/insight/tests/testthat/test-hurdle.R
/usr/lib64/R/library/insight/tests/testthat/test-is-empty-object.R
/usr/lib64/R/library/insight/tests/testthat/test-is_nullmodel.R
/usr/lib64/R/library/insight/tests/testthat/test-iv_robust.R
/usr/lib64/R/library/insight/tests/testthat/test-ivreg.R
/usr/lib64/R/library/insight/tests/testthat/test-ivreg_AER.R
/usr/lib64/R/library/insight/tests/testthat/test-lm.R
/usr/lib64/R/library/insight/tests/testthat/test-lm_robust.R
/usr/lib64/R/library/insight/tests/testthat/test-lme.R
/usr/lib64/R/library/insight/tests/testthat/test-lmer.R
/usr/lib64/R/library/insight/tests/testthat/test-lmrob_base.R
/usr/lib64/R/library/insight/tests/testthat/test-lmtest.R
/usr/lib64/R/library/insight/tests/testthat/test-logistf.R
/usr/lib64/R/library/insight/tests/testthat/test-marginaleffects.R
/usr/lib64/R/library/insight/tests/testthat/test-metaBMA.R
/usr/lib64/R/library/insight/tests/testthat/test-mhurdle.R
/usr/lib64/R/library/insight/tests/testthat/test-mixed.R
/usr/lib64/R/library/insight/tests/testthat/test-mlogit.R
/usr/lib64/R/library/insight/tests/testthat/test-model_data.R
/usr/lib64/R/library/insight/tests/testthat/test-model_info.R
/usr/lib64/R/library/insight/tests/testthat/test-multinom.R
/usr/lib64/R/library/insight/tests/testthat/test-mvrstanarm.R
/usr/lib64/R/library/insight/tests/testthat/test-n_parameters_rank-deficiency.R
/usr/lib64/R/library/insight/tests/testthat/test-namespace.R
/usr/lib64/R/library/insight/tests/testthat/test-negbin.R
/usr/lib64/R/library/insight/tests/testthat/test-nlmer.R
/usr/lib64/R/library/insight/tests/testthat/test-object_has_helpers.R
/usr/lib64/R/library/insight/tests/testthat/test-offset.R
/usr/lib64/R/library/insight/tests/testthat/test-ols.R
/usr/lib64/R/library/insight/tests/testthat/test-panelr.R
/usr/lib64/R/library/insight/tests/testthat/test-plm.R
/usr/lib64/R/library/insight/tests/testthat/test-polr.R
/usr/lib64/R/library/insight/tests/testthat/test-proportion_response.R
/usr/lib64/R/library/insight/tests/testthat/test-psm.R
/usr/lib64/R/library/insight/tests/testthat/test-r3_4.R
/usr/lib64/R/library/insight/tests/testthat/test-response_data2.R
/usr/lib64/R/library/insight/tests/testthat/test-rlm.R
/usr/lib64/R/library/insight/tests/testthat/test-rlmer.R
/usr/lib64/R/library/insight/tests/testthat/test-rms.R
/usr/lib64/R/library/insight/tests/testthat/test-rq.R
/usr/lib64/R/library/insight/tests/testthat/test-rqss.R
/usr/lib64/R/library/insight/tests/testthat/test-rstanarm.R
/usr/lib64/R/library/insight/tests/testthat/test-spatial.R
/usr/lib64/R/library/insight/tests/testthat/test-speedglm.R
/usr/lib64/R/library/insight/tests/testthat/test-speedlm.R
/usr/lib64/R/library/insight/tests/testthat/test-standardize_column_order.R
/usr/lib64/R/library/insight/tests/testthat/test-standardize_names.R
/usr/lib64/R/library/insight/tests/testthat/test-survey.R
/usr/lib64/R/library/insight/tests/testthat/test-survfit.R
/usr/lib64/R/library/insight/tests/testthat/test-survreg.R
/usr/lib64/R/library/insight/tests/testthat/test-tidymodels.R
/usr/lib64/R/library/insight/tests/testthat/test-tobit.R
/usr/lib64/R/library/insight/tests/testthat/test-truncreg.R
/usr/lib64/R/library/insight/tests/testthat/test-vgam.R
/usr/lib64/R/library/insight/tests/testthat/test-vglm.R
/usr/lib64/R/library/insight/tests/testthat/test-zeroinfl.R
