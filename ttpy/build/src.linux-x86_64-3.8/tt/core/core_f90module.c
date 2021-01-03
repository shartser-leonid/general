/* File: core_f90module.c
 * This file is auto-generated with f2py (version:2).
 * f2py is a Fortran to Python Interface Generator (FPIG), Second Edition,
 * written by Pearu Peterson <pearu@cens.ioc.ee>.
 * Generation date: Tue Dec 29 16:07:50 2020
 * Do not edit this file directly unless you know what you are doing!!!
 */

#ifdef __cplusplus
extern "C" {
#endif

/*********************** See f2py2e/cfuncs.py: includes ***********************/
#include <stdarg.h>
#include "Python.h"
#include "fortranobject.h"
#include <math.h>

/**************** See f2py2e/rules.py: mod_rules['modulebody'] ****************/
static PyObject *core_f90_error;
static PyObject *core_f90_module;

/*********************** See f2py2e/cfuncs.py: typedefs ***********************/
typedef struct {double r,i;} complex_double;

/****************** See f2py2e/cfuncs.py: typedefs_generated ******************/
/*need_typedefs_generated*/

/********************** See f2py2e/cfuncs.py: cppmacros **********************/
#ifdef DEBUGCFUNCS
#define CFUNCSMESS(mess) fprintf(stderr,"debug-capi:"mess);
#define CFUNCSMESSPY(mess,obj) CFUNCSMESS(mess) \
    PyObject_Print((PyObject *)obj,stderr,Py_PRINT_RAW);\
    fprintf(stderr,"\n");
#else
#define CFUNCSMESS(mess)
#define CFUNCSMESSPY(mess,obj)
#endif

#ifndef max
#define max(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef min
#define min(a,b) ((a < b) ? (a) : (b))
#endif
#ifndef MAX
#define MAX(a,b) ((a > b) ? (a) : (b))
#endif
#ifndef MIN
#define MIN(a,b) ((a < b) ? (a) : (b))
#endif

#define rank(var) var ## _Rank
#define shape(var,dim) var ## _Dims[dim]
#define old_rank(var) (PyArray_NDIM((PyArrayObject *)(capi_ ## var ## _tmp)))
#define old_shape(var,dim) PyArray_DIM(((PyArrayObject *)(capi_ ## var ## _tmp)),dim)
#define fshape(var,dim) shape(var,rank(var)-dim-1)
#define len(var) shape(var,0)
#define flen(var) fshape(var,0)
#define old_size(var) PyArray_SIZE((PyArrayObject *)(capi_ ## var ## _tmp))
/* #define index(i) capi_i ## i */
#define slen(var) capi_ ## var ## _len
#define size(var, ...) f2py_size((PyArrayObject *)(capi_ ## var ## _tmp), ## __VA_ARGS__, -1)

#define CHECKSCALAR(check,tcheck,name,show,var)\
    if (!(check)) {\
        char errstring[256];\
        sprintf(errstring, "%s: "show, "("tcheck") failed for "name, var);\
        PyErr_SetString(core_f90_error,errstring);\
        /*goto capi_fail;*/\
    } else 
#if defined(PREPEND_FORTRAN)
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F
#else
#define F_FUNC(f,F) _##f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) _##F##_
#else
#define F_FUNC(f,F) _##f##_
#endif
#endif
#else
#if defined(NO_APPEND_FORTRAN)
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F
#else
#define F_FUNC(f,F) f
#endif
#else
#if defined(UPPERCASE_FORTRAN)
#define F_FUNC(f,F) F##_
#else
#define F_FUNC(f,F) f##_
#endif
#endif
#endif
#if defined(UNDERSCORE_G77)
#define F_FUNC_US(f,F) F_FUNC(f##_,F##_)
#else
#define F_FUNC_US(f,F) F_FUNC(f,F)
#endif


/************************ See f2py2e/cfuncs.py: cfuncs ************************/
static int f2py_size(PyArrayObject* var, ...)
{
  npy_int sz = 0;
  npy_int dim;
  npy_int rank;
  va_list argp;
  va_start(argp, var);
  dim = va_arg(argp, npy_int);
  if (dim==-1)
    {
      sz = PyArray_SIZE(var);
    }
  else
    {
      rank = PyArray_NDIM(var);
      if (dim>=1 && dim<=rank)
        sz = PyArray_DIM(var, dim-1);
      else
        fprintf(stderr, "f2py_size: 2nd argument value=%d fails to satisfy 1<=value<=%d. Result will be 0.\n", dim, rank);
    }
  va_end(argp);
  return sz;
}

static int int_from_pyobj(int* v,PyObject *obj,const char *errmess) {
    PyObject* tmp = NULL;
    if (PyInt_Check(obj)) {
        *v = (int)PyInt_AS_LONG(obj);
        return 1;
    }
    tmp = PyNumber_Int(obj);
    if (tmp) {
        *v = PyInt_AS_LONG(tmp);
        Py_DECREF(tmp);
        return 1;
    }
    if (PyComplex_Check(obj))
        tmp = PyObject_GetAttrString(obj,"real");
    else if (PyString_Check(obj) || PyUnicode_Check(obj))
        /*pass*/;
    else if (PySequence_Check(obj))
        tmp = PySequence_GetItem(obj,0);
    if (tmp) {
        PyErr_Clear();
        if (int_from_pyobj(v,tmp,errmess)) {Py_DECREF(tmp); return 1;}
        Py_DECREF(tmp);
    }
    {
        PyObject* err = PyErr_Occurred();
        if (err==NULL) err = core_f90_error;
        PyErr_SetString(err,errmess);
    }
    return 0;
}


/********************* See f2py2e/cfuncs.py: userincludes *********************/
/*need_userincludes*/

/********************* See f2py2e/capi_rules.py: usercode *********************/


/* See f2py2e/rules.py */
/*eof externroutines*/

/******************** See f2py2e/capi_rules.py: usercode1 ********************/


/******************* See f2py2e/cb_rules.py: buildcallback *******************/
/*need_callbacks*/

/*********************** See f2py2e/rules.py: buildapi ***********************/

/********************************** dealloc **********************************/
static char doc_f2py_rout_core_f90_core_dealloc[] = "\
dealloc()\n\nWrapper for ``dealloc``.\
\n";
/*  */
static PyObject *f2py_rout_core_f90_core_dealloc(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(void)) {
  PyObject * volatile capi_buildvalue = NULL;
  volatile int f2py_success = 1;
/*decl*/

  static char *capi_kwlist[] = {NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
  if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
    "|:core_f90.core.dealloc",\
    capi_kwlist))
    return NULL;
/*frompyobj*/
/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
        (*f2py_func)();
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
    if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
    CFUNCSMESS("Building return value.\n");
    capi_buildvalue = Py_BuildValue("");
/*closepyobjfrom*/
/*end of closepyobjfrom*/
    } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
/*end of cleanupfrompyobj*/
  if (capi_buildvalue == NULL) {
/*routdebugfailure*/
  } else {
/*routdebugleave*/
  }
  CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
  return capi_buildvalue;
}
/******************************* end of dealloc *******************************/

/********************************** dmat_mat **********************************/
static char doc_f2py_rout_core_f90_core_dmat_mat[] = "\
rres = dmat_mat(n,m,k,cr1,cr2,r1,r2,[d,cr1size,cr2size])\n\nWrapper for ``dmat_mat``.\
\n\nParameters\n----------\n"
"n : input rank-1 array('i') with bounds (d)\n"
"m : input rank-1 array('i') with bounds (d)\n"
"k : input rank-1 array('i') with bounds (d)\n"
"cr1 : input rank-1 array('d') with bounds (cr1size)\n"
"cr2 : input rank-1 array('d') with bounds (cr2size)\n"
"r1 : input rank-1 array('i') with bounds (d + 1)\n"
"r2 : input rank-1 array('i') with bounds (d + 1)\n"
"\nOther Parameters\n----------------\n"
"d : input int, optional\n    Default: len(n)\n"
"cr1size : input int, optional\n    Default: len(cr1)\n"
"cr2size : input int, optional\n    Default: len(cr2)\n"
"\nReturns\n-------\n"
"rres : rank-1 array('i') with bounds (d + 1)";
/*  */
static PyObject *f2py_rout_core_f90_core_dmat_mat(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(int*,int*,int*,int*,double*,int*,double*,int*,int*,int*,int*)) {
  PyObject * volatile capi_buildvalue = NULL;
  volatile int f2py_success = 1;
/*decl*/

  int d = 0;
  PyObject *d_capi = Py_None;
  int *n = NULL;
  npy_intp n_Dims[1] = {-1};
  const int n_Rank = 1;
  PyArrayObject *capi_n_tmp = NULL;
  int capi_n_intent = 0;
  PyObject *n_capi = Py_None;
  int *m = NULL;
  npy_intp m_Dims[1] = {-1};
  const int m_Rank = 1;
  PyArrayObject *capi_m_tmp = NULL;
  int capi_m_intent = 0;
  PyObject *m_capi = Py_None;
  int *k = NULL;
  npy_intp k_Dims[1] = {-1};
  const int k_Rank = 1;
  PyArrayObject *capi_k_tmp = NULL;
  int capi_k_intent = 0;
  PyObject *k_capi = Py_None;
  double *cr1 = NULL;
  npy_intp cr1_Dims[1] = {-1};
  const int cr1_Rank = 1;
  PyArrayObject *capi_cr1_tmp = NULL;
  int capi_cr1_intent = 0;
  PyObject *cr1_capi = Py_None;
  int cr1size = 0;
  PyObject *cr1size_capi = Py_None;
  double *cr2 = NULL;
  npy_intp cr2_Dims[1] = {-1};
  const int cr2_Rank = 1;
  PyArrayObject *capi_cr2_tmp = NULL;
  int capi_cr2_intent = 0;
  PyObject *cr2_capi = Py_None;
  int cr2size = 0;
  PyObject *cr2size_capi = Py_None;
  int *r1 = NULL;
  npy_intp r1_Dims[1] = {-1};
  const int r1_Rank = 1;
  PyArrayObject *capi_r1_tmp = NULL;
  int capi_r1_intent = 0;
  PyObject *r1_capi = Py_None;
  int *r2 = NULL;
  npy_intp r2_Dims[1] = {-1};
  const int r2_Rank = 1;
  PyArrayObject *capi_r2_tmp = NULL;
  int capi_r2_intent = 0;
  PyObject *r2_capi = Py_None;
  int *rres = NULL;
  npy_intp rres_Dims[1] = {-1};
  const int rres_Rank = 1;
  PyArrayObject *capi_rres_tmp = NULL;
  int capi_rres_intent = 0;
  static char *capi_kwlist[] = {"n","m","k","cr1","cr2","r1","r2","d","cr1size","cr2size",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
  if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
    "OOOOOOO|OOO:core_f90.core.dmat_mat",\
    capi_kwlist,&n_capi,&m_capi,&k_capi,&cr1_capi,&cr2_capi,&r1_capi,&r2_capi,&d_capi,&cr1size_capi,&cr2size_capi))
    return NULL;
/*frompyobj*/
  /* Processing variable n */
  ;
  capi_n_intent |= F2PY_INTENT_IN;
  capi_n_tmp = array_from_pyobj(NPY_INT,n_Dims,n_Rank,capi_n_intent,n_capi);
  if (capi_n_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 1st argument `n' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    n = (int *)(PyArray_DATA(capi_n_tmp));

  /* Processing variable cr1 */
  ;
  capi_cr1_intent |= F2PY_INTENT_IN;
  capi_cr1_tmp = array_from_pyobj(NPY_DOUBLE,cr1_Dims,cr1_Rank,capi_cr1_intent,cr1_capi);
  if (capi_cr1_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 4th argument `cr1' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    cr1 = (double *)(PyArray_DATA(capi_cr1_tmp));

  /* Processing variable cr2 */
  ;
  capi_cr2_intent |= F2PY_INTENT_IN;
  capi_cr2_tmp = array_from_pyobj(NPY_DOUBLE,cr2_Dims,cr2_Rank,capi_cr2_intent,cr2_capi);
  if (capi_cr2_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 5th argument `cr2' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    cr2 = (double *)(PyArray_DATA(capi_cr2_tmp));

  /* Processing variable d */
  if (d_capi == Py_None) d = len(n); else
    f2py_success = int_from_pyobj(&d,d_capi,"core_f90.core.dmat_mat() 1st keyword (d) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(n)>=d,"len(n)>=d","1st keyword d","dmat_mat:d=%d",d) {
  /* Processing variable m */
  m_Dims[0]=d;
  capi_m_intent |= F2PY_INTENT_IN;
  capi_m_tmp = array_from_pyobj(NPY_INT,m_Dims,m_Rank,capi_m_intent,m_capi);
  if (capi_m_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 2nd argument `m' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    m = (int *)(PyArray_DATA(capi_m_tmp));

  /* Processing variable k */
  k_Dims[0]=d;
  capi_k_intent |= F2PY_INTENT_IN;
  capi_k_tmp = array_from_pyobj(NPY_INT,k_Dims,k_Rank,capi_k_intent,k_capi);
  if (capi_k_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 3rd argument `k' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    k = (int *)(PyArray_DATA(capi_k_tmp));

  /* Processing variable cr1size */
  if (cr1size_capi == Py_None) cr1size = len(cr1); else
    f2py_success = int_from_pyobj(&cr1size,cr1size_capi,"core_f90.core.dmat_mat() 2nd keyword (cr1size) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(cr1)>=cr1size,"len(cr1)>=cr1size","2nd keyword cr1size","dmat_mat:cr1size=%d",cr1size) {
  /* Processing variable cr2size */
  if (cr2size_capi == Py_None) cr2size = len(cr2); else
    f2py_success = int_from_pyobj(&cr2size,cr2size_capi,"core_f90.core.dmat_mat() 3rd keyword (cr2size) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(cr2)>=cr2size,"len(cr2)>=cr2size","3rd keyword cr2size","dmat_mat:cr2size=%d",cr2size) {
  /* Processing variable r1 */
  r1_Dims[0]=d + 1;
  capi_r1_intent |= F2PY_INTENT_IN;
  capi_r1_tmp = array_from_pyobj(NPY_INT,r1_Dims,r1_Rank,capi_r1_intent,r1_capi);
  if (capi_r1_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 6th argument `r1' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    r1 = (int *)(PyArray_DATA(capi_r1_tmp));

  /* Processing variable r2 */
  r2_Dims[0]=d + 1;
  capi_r2_intent |= F2PY_INTENT_IN;
  capi_r2_tmp = array_from_pyobj(NPY_INT,r2_Dims,r2_Rank,capi_r2_intent,r2_capi);
  if (capi_r2_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 7th argument `r2' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    r2 = (int *)(PyArray_DATA(capi_r2_tmp));

  /* Processing variable rres */
  rres_Dims[0]=d + 1;
  capi_rres_intent |= F2PY_INTENT_OUT|F2PY_INTENT_HIDE;
  capi_rres_tmp = array_from_pyobj(NPY_INT,rres_Dims,rres_Rank,capi_rres_intent,Py_None);
  if (capi_rres_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting hidden `rres' of core_f90.core.dmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    rres = (int *)(PyArray_DATA(capi_rres_tmp));

/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
        (*f2py_func)(&d,n,m,k,cr1,&cr1size,cr2,&cr2size,r1,r2,rres);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
    if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
    CFUNCSMESS("Building return value.\n");
    capi_buildvalue = Py_BuildValue("N",capi_rres_tmp);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
    } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  }  /*if (capi_rres_tmp == NULL) ... else of rres*/
  /* End of cleaning variable rres */
  if((PyObject *)capi_r2_tmp!=r2_capi) {
    Py_XDECREF(capi_r2_tmp); }
  }  /*if (capi_r2_tmp == NULL) ... else of r2*/
  /* End of cleaning variable r2 */
  if((PyObject *)capi_r1_tmp!=r1_capi) {
    Py_XDECREF(capi_r1_tmp); }
  }  /*if (capi_r1_tmp == NULL) ... else of r1*/
  /* End of cleaning variable r1 */
  } /*CHECKSCALAR(len(cr2)>=cr2size)*/
  } /*if (f2py_success) of cr2size*/
  /* End of cleaning variable cr2size */
  } /*CHECKSCALAR(len(cr1)>=cr1size)*/
  } /*if (f2py_success) of cr1size*/
  /* End of cleaning variable cr1size */
  if((PyObject *)capi_k_tmp!=k_capi) {
    Py_XDECREF(capi_k_tmp); }
  }  /*if (capi_k_tmp == NULL) ... else of k*/
  /* End of cleaning variable k */
  if((PyObject *)capi_m_tmp!=m_capi) {
    Py_XDECREF(capi_m_tmp); }
  }  /*if (capi_m_tmp == NULL) ... else of m*/
  /* End of cleaning variable m */
  } /*CHECKSCALAR(len(n)>=d)*/
  } /*if (f2py_success) of d*/
  /* End of cleaning variable d */
  if((PyObject *)capi_cr2_tmp!=cr2_capi) {
    Py_XDECREF(capi_cr2_tmp); }
  }  /*if (capi_cr2_tmp == NULL) ... else of cr2*/
  /* End of cleaning variable cr2 */
  if((PyObject *)capi_cr1_tmp!=cr1_capi) {
    Py_XDECREF(capi_cr1_tmp); }
  }  /*if (capi_cr1_tmp == NULL) ... else of cr1*/
  /* End of cleaning variable cr1 */
  if((PyObject *)capi_n_tmp!=n_capi) {
    Py_XDECREF(capi_n_tmp); }
  }  /*if (capi_n_tmp == NULL) ... else of n*/
  /* End of cleaning variable n */
/*end of cleanupfrompyobj*/
  if (capi_buildvalue == NULL) {
/*routdebugfailure*/
  } else {
/*routdebugleave*/
  }
  CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
  return capi_buildvalue;
}
/****************************** end of dmat_mat ******************************/

/********************************** zmat_mat **********************************/
static char doc_f2py_rout_core_f90_core_zmat_mat[] = "\
rres = zmat_mat(n,m,k,cr1,cr2,r1,r2,[d,cr1size,cr2size])\n\nWrapper for ``zmat_mat``.\
\n\nParameters\n----------\n"
"n : input rank-1 array('i') with bounds (d)\n"
"m : input rank-1 array('i') with bounds (d)\n"
"k : input rank-1 array('i') with bounds (d)\n"
"cr1 : input rank-1 array('D') with bounds (cr1size)\n"
"cr2 : input rank-1 array('D') with bounds (cr2size)\n"
"r1 : input rank-1 array('i') with bounds (d + 1)\n"
"r2 : input rank-1 array('i') with bounds (d + 1)\n"
"\nOther Parameters\n----------------\n"
"d : input int, optional\n    Default: len(n)\n"
"cr1size : input int, optional\n    Default: len(cr1)\n"
"cr2size : input int, optional\n    Default: len(cr2)\n"
"\nReturns\n-------\n"
"rres : rank-1 array('i') with bounds (d + 1)";
/*  */
static PyObject *f2py_rout_core_f90_core_zmat_mat(const PyObject *capi_self,
                           PyObject *capi_args,
                           PyObject *capi_keywds,
                           void (*f2py_func)(int*,int*,int*,int*,complex_double*,int*,complex_double*,int*,int*,int*,int*)) {
  PyObject * volatile capi_buildvalue = NULL;
  volatile int f2py_success = 1;
/*decl*/

  int d = 0;
  PyObject *d_capi = Py_None;
  int *n = NULL;
  npy_intp n_Dims[1] = {-1};
  const int n_Rank = 1;
  PyArrayObject *capi_n_tmp = NULL;
  int capi_n_intent = 0;
  PyObject *n_capi = Py_None;
  int *m = NULL;
  npy_intp m_Dims[1] = {-1};
  const int m_Rank = 1;
  PyArrayObject *capi_m_tmp = NULL;
  int capi_m_intent = 0;
  PyObject *m_capi = Py_None;
  int *k = NULL;
  npy_intp k_Dims[1] = {-1};
  const int k_Rank = 1;
  PyArrayObject *capi_k_tmp = NULL;
  int capi_k_intent = 0;
  PyObject *k_capi = Py_None;
  complex_double *cr1 = NULL;
  npy_intp cr1_Dims[1] = {-1};
  const int cr1_Rank = 1;
  PyArrayObject *capi_cr1_tmp = NULL;
  int capi_cr1_intent = 0;
  PyObject *cr1_capi = Py_None;
  int cr1size = 0;
  PyObject *cr1size_capi = Py_None;
  complex_double *cr2 = NULL;
  npy_intp cr2_Dims[1] = {-1};
  const int cr2_Rank = 1;
  PyArrayObject *capi_cr2_tmp = NULL;
  int capi_cr2_intent = 0;
  PyObject *cr2_capi = Py_None;
  int cr2size = 0;
  PyObject *cr2size_capi = Py_None;
  int *r1 = NULL;
  npy_intp r1_Dims[1] = {-1};
  const int r1_Rank = 1;
  PyArrayObject *capi_r1_tmp = NULL;
  int capi_r1_intent = 0;
  PyObject *r1_capi = Py_None;
  int *r2 = NULL;
  npy_intp r2_Dims[1] = {-1};
  const int r2_Rank = 1;
  PyArrayObject *capi_r2_tmp = NULL;
  int capi_r2_intent = 0;
  PyObject *r2_capi = Py_None;
  int *rres = NULL;
  npy_intp rres_Dims[1] = {-1};
  const int rres_Rank = 1;
  PyArrayObject *capi_rres_tmp = NULL;
  int capi_rres_intent = 0;
  static char *capi_kwlist[] = {"n","m","k","cr1","cr2","r1","r2","d","cr1size","cr2size",NULL};

/*routdebugenter*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_clock();
#endif
  if (!PyArg_ParseTupleAndKeywords(capi_args,capi_keywds,\
    "OOOOOOO|OOO:core_f90.core.zmat_mat",\
    capi_kwlist,&n_capi,&m_capi,&k_capi,&cr1_capi,&cr2_capi,&r1_capi,&r2_capi,&d_capi,&cr1size_capi,&cr2size_capi))
    return NULL;
/*frompyobj*/
  /* Processing variable n */
  ;
  capi_n_intent |= F2PY_INTENT_IN;
  capi_n_tmp = array_from_pyobj(NPY_INT,n_Dims,n_Rank,capi_n_intent,n_capi);
  if (capi_n_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 1st argument `n' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    n = (int *)(PyArray_DATA(capi_n_tmp));

  /* Processing variable cr1 */
  ;
  capi_cr1_intent |= F2PY_INTENT_IN;
  capi_cr1_tmp = array_from_pyobj(NPY_CDOUBLE,cr1_Dims,cr1_Rank,capi_cr1_intent,cr1_capi);
  if (capi_cr1_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 4th argument `cr1' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    cr1 = (complex_double *)(PyArray_DATA(capi_cr1_tmp));

  /* Processing variable cr2 */
  ;
  capi_cr2_intent |= F2PY_INTENT_IN;
  capi_cr2_tmp = array_from_pyobj(NPY_CDOUBLE,cr2_Dims,cr2_Rank,capi_cr2_intent,cr2_capi);
  if (capi_cr2_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 5th argument `cr2' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    cr2 = (complex_double *)(PyArray_DATA(capi_cr2_tmp));

  /* Processing variable d */
  if (d_capi == Py_None) d = len(n); else
    f2py_success = int_from_pyobj(&d,d_capi,"core_f90.core.zmat_mat() 1st keyword (d) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(n)>=d,"len(n)>=d","1st keyword d","zmat_mat:d=%d",d) {
  /* Processing variable m */
  m_Dims[0]=d;
  capi_m_intent |= F2PY_INTENT_IN;
  capi_m_tmp = array_from_pyobj(NPY_INT,m_Dims,m_Rank,capi_m_intent,m_capi);
  if (capi_m_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 2nd argument `m' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    m = (int *)(PyArray_DATA(capi_m_tmp));

  /* Processing variable k */
  k_Dims[0]=d;
  capi_k_intent |= F2PY_INTENT_IN;
  capi_k_tmp = array_from_pyobj(NPY_INT,k_Dims,k_Rank,capi_k_intent,k_capi);
  if (capi_k_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 3rd argument `k' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    k = (int *)(PyArray_DATA(capi_k_tmp));

  /* Processing variable cr1size */
  if (cr1size_capi == Py_None) cr1size = len(cr1); else
    f2py_success = int_from_pyobj(&cr1size,cr1size_capi,"core_f90.core.zmat_mat() 2nd keyword (cr1size) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(cr1)>=cr1size,"len(cr1)>=cr1size","2nd keyword cr1size","zmat_mat:cr1size=%d",cr1size) {
  /* Processing variable cr2size */
  if (cr2size_capi == Py_None) cr2size = len(cr2); else
    f2py_success = int_from_pyobj(&cr2size,cr2size_capi,"core_f90.core.zmat_mat() 3rd keyword (cr2size) can't be converted to int");
  if (f2py_success) {
  CHECKSCALAR(len(cr2)>=cr2size,"len(cr2)>=cr2size","3rd keyword cr2size","zmat_mat:cr2size=%d",cr2size) {
  /* Processing variable r1 */
  r1_Dims[0]=d + 1;
  capi_r1_intent |= F2PY_INTENT_IN;
  capi_r1_tmp = array_from_pyobj(NPY_INT,r1_Dims,r1_Rank,capi_r1_intent,r1_capi);
  if (capi_r1_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 6th argument `r1' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    r1 = (int *)(PyArray_DATA(capi_r1_tmp));

  /* Processing variable r2 */
  r2_Dims[0]=d + 1;
  capi_r2_intent |= F2PY_INTENT_IN;
  capi_r2_tmp = array_from_pyobj(NPY_INT,r2_Dims,r2_Rank,capi_r2_intent,r2_capi);
  if (capi_r2_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting 7th argument `r2' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    r2 = (int *)(PyArray_DATA(capi_r2_tmp));

  /* Processing variable rres */
  rres_Dims[0]=d + 1;
  capi_rres_intent |= F2PY_INTENT_OUT|F2PY_INTENT_HIDE;
  capi_rres_tmp = array_from_pyobj(NPY_INT,rres_Dims,rres_Rank,capi_rres_intent,Py_None);
  if (capi_rres_tmp == NULL) {
    PyObject *exc, *val, *tb;
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_SetString(exc ? exc : core_f90_error,"failed in converting hidden `rres' of core_f90.core.zmat_mat to C/Fortran array" );
    npy_PyErr_ChainExceptionsCause(exc, val, tb);
  } else {
    rres = (int *)(PyArray_DATA(capi_rres_tmp));

/*end of frompyobj*/
#ifdef F2PY_REPORT_ATEXIT
f2py_start_call_clock();
#endif
/*callfortranroutine*/
        (*f2py_func)(&d,n,m,k,cr1,&cr1size,cr2,&cr2size,r1,r2,rres);
if (PyErr_Occurred())
  f2py_success = 0;
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_call_clock();
#endif
/*end of callfortranroutine*/
    if (f2py_success) {
/*pyobjfrom*/
/*end of pyobjfrom*/
    CFUNCSMESS("Building return value.\n");
    capi_buildvalue = Py_BuildValue("N",capi_rres_tmp);
/*closepyobjfrom*/
/*end of closepyobjfrom*/
    } /*if (f2py_success) after callfortranroutine*/
/*cleanupfrompyobj*/
  }  /*if (capi_rres_tmp == NULL) ... else of rres*/
  /* End of cleaning variable rres */
  if((PyObject *)capi_r2_tmp!=r2_capi) {
    Py_XDECREF(capi_r2_tmp); }
  }  /*if (capi_r2_tmp == NULL) ... else of r2*/
  /* End of cleaning variable r2 */
  if((PyObject *)capi_r1_tmp!=r1_capi) {
    Py_XDECREF(capi_r1_tmp); }
  }  /*if (capi_r1_tmp == NULL) ... else of r1*/
  /* End of cleaning variable r1 */
  } /*CHECKSCALAR(len(cr2)>=cr2size)*/
  } /*if (f2py_success) of cr2size*/
  /* End of cleaning variable cr2size */
  } /*CHECKSCALAR(len(cr1)>=cr1size)*/
  } /*if (f2py_success) of cr1size*/
  /* End of cleaning variable cr1size */
  if((PyObject *)capi_k_tmp!=k_capi) {
    Py_XDECREF(capi_k_tmp); }
  }  /*if (capi_k_tmp == NULL) ... else of k*/
  /* End of cleaning variable k */
  if((PyObject *)capi_m_tmp!=m_capi) {
    Py_XDECREF(capi_m_tmp); }
  }  /*if (capi_m_tmp == NULL) ... else of m*/
  /* End of cleaning variable m */
  } /*CHECKSCALAR(len(n)>=d)*/
  } /*if (f2py_success) of d*/
  /* End of cleaning variable d */
  if((PyObject *)capi_cr2_tmp!=cr2_capi) {
    Py_XDECREF(capi_cr2_tmp); }
  }  /*if (capi_cr2_tmp == NULL) ... else of cr2*/
  /* End of cleaning variable cr2 */
  if((PyObject *)capi_cr1_tmp!=cr1_capi) {
    Py_XDECREF(capi_cr1_tmp); }
  }  /*if (capi_cr1_tmp == NULL) ... else of cr1*/
  /* End of cleaning variable cr1 */
  if((PyObject *)capi_n_tmp!=n_capi) {
    Py_XDECREF(capi_n_tmp); }
  }  /*if (capi_n_tmp == NULL) ... else of n*/
  /* End of cleaning variable n */
/*end of cleanupfrompyobj*/
  if (capi_buildvalue == NULL) {
/*routdebugfailure*/
  } else {
/*routdebugleave*/
  }
  CFUNCSMESS("Freeing memory.\n");
/*freemem*/
#ifdef F2PY_REPORT_ATEXIT
f2py_stop_clock();
#endif
  return capi_buildvalue;
}
/****************************** end of zmat_mat ******************************/
/*eof body*/

/******************* See f2py2e/f90mod_rules.py: buildhooks *******************/

static FortranDataDef f2py_core_def[] = {
  {"zresult_core",1,{{-1}},NPY_CDOUBLE},
  {"result_core",1,{{-1}},NPY_DOUBLE},
  {"dealloc",-1,{{-1}},0,NULL,(void *)f2py_rout_core_f90_core_dealloc,doc_f2py_rout_core_f90_core_dealloc},
  {"dmat_mat",-1,{{-1}},0,NULL,(void *)f2py_rout_core_f90_core_dmat_mat,doc_f2py_rout_core_f90_core_dmat_mat},
  {"zmat_mat",-1,{{-1}},0,NULL,(void *)f2py_rout_core_f90_core_zmat_mat,doc_f2py_rout_core_f90_core_zmat_mat},
  {NULL}
};

static void f2py_setup_core(void (*zresult_core)(int*,int*,void(*)(char*,int*),int*),void (*result_core)(int*,int*,void(*)(char*,int*),int*),char *dealloc,char *dmat_mat,char *zmat_mat) {
  int i_f2py=0;
  f2py_core_def[i_f2py++].func = zresult_core;
  f2py_core_def[i_f2py++].func = result_core;
  f2py_core_def[i_f2py++].data = dealloc;
  f2py_core_def[i_f2py++].data = dmat_mat;
  f2py_core_def[i_f2py++].data = zmat_mat;
}
extern void F_FUNC(f2pyinitcore,F2PYINITCORE)(void (*)(void (*)(int*,int*,void(*)(char*,int*),int*),void (*)(int*,int*,void(*)(char*,int*),int*),char *,char *,char *));
static void f2py_init_core(void) {
  F_FUNC(f2pyinitcore,F2PYINITCORE)(f2py_setup_core);
}

/*need_f90modhooks*/

/************** See f2py2e/rules.py: module_rules['modulebody'] **************/

/******************* See f2py2e/common_rules.py: buildhooks *******************/

/*need_commonhooks*/

/**************************** See f2py2e/rules.py ****************************/

static FortranDataDef f2py_routine_defs[] = {

/*eof routine_defs*/
  {NULL}
};

static PyMethodDef f2py_module_methods[] = {

  {NULL,NULL}
};

static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "core_f90",
  NULL,
  -1,
  f2py_module_methods,
  NULL,
  NULL,
  NULL,
  NULL
};

PyMODINIT_FUNC PyInit_core_f90(void) {
  int i;
  PyObject *m,*d, *s, *tmp;
  m = core_f90_module = PyModule_Create(&moduledef);
  Py_SET_TYPE(&PyFortran_Type, &PyType_Type);
  import_array();
  if (PyErr_Occurred())
    {PyErr_SetString(PyExc_ImportError, "can't initialize module core_f90 (failed to import numpy)"); return m;}
  d = PyModule_GetDict(m);
  s = PyString_FromString("$Revision: $");
  PyDict_SetItemString(d, "__version__", s);
  Py_DECREF(s);
  s = PyUnicode_FromString(
    "This module 'core_f90' is auto-generated with f2py (version:2).\nFunctions:\n"
"Fortran 90/95 modules:\n""  core --- zresult_core,result_core,dealloc(),dmat_mat(),zmat_mat()"".");
  PyDict_SetItemString(d, "__doc__", s);
  Py_DECREF(s);
  core_f90_error = PyErr_NewException ("core_f90.error", NULL, NULL);
  /*
   * Store the error object inside the dict, so that it could get deallocated.
   * (in practice, this is a module, so it likely will not and cannot.)
   */
  PyDict_SetItemString(d, "_core_f90_error", core_f90_error);
  Py_DECREF(core_f90_error);
  for(i=0;f2py_routine_defs[i].name!=NULL;i++) {
    tmp = PyFortranObject_NewAsAttr(&f2py_routine_defs[i]);
    PyDict_SetItemString(d, f2py_routine_defs[i].name, tmp);
    Py_DECREF(tmp);
  }



/*eof initf2pywraphooks*/
  PyDict_SetItemString(d, "core", PyFortranObject_New(f2py_core_def,f2py_init_core));
/*eof initf90modhooks*/

/*eof initcommonhooks*/


#ifdef F2PY_REPORT_ATEXIT
  if (! PyErr_Occurred())
    on_exit(f2py_report_on_exit,(void*)"core_f90");
#endif
  return m;
}
#ifdef __cplusplus
}
#endif
