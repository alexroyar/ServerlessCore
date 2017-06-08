# This file is generated by /tmp/pip-build-wWFuQK/scipy/-c
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

atlas_3_10_blas_info={}
atlas_3_10_blas_threads_info={}
atlas_threads_info={'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib64/atlas-sse3'], 'language': 'f77', 'define_macros': [('ATLAS_INFO', '"\\"3.8.4\\""')], 'include_dirs': ['/usr/include']}
blas_opt_info={'libraries': ['ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib64/atlas-sse3'], 'language': 'c', 'define_macros': [('HAVE_CBLAS', None), ('ATLAS_INFO', '"\\"3.8.4\\""')], 'include_dirs': ['/usr/include']}
blis_info={}
atlas_blas_threads_info={'libraries': ['ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib64/atlas-sse3'], 'language': 'c', 'define_macros': [('HAVE_CBLAS', None), ('ATLAS_INFO', '"\\"3.8.4\\""')], 'include_dirs': ['/usr/include']}
openblas_info={}
lapack_opt_info={'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/lib64/atlas-sse3'], 'language': 'f77', 'define_macros': [('ATLAS_INFO', '"\\"3.8.4\\""')], 'include_dirs': ['/usr/include']}
openblas_lapack_info={}
atlas_3_10_threads_info={}
atlas_3_10_info={}
lapack_mkl_info={}
blas_mkl_info={}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    