/* NOTE: Do not edit this file, it is generated by a script:
   Export.py --api gl 4.2 --api wgl 4.0 --api glx 4.0 --api cgl 1.4 --api egl 1.0 --outdir src/regal
*/

/*
  Copyright (c) 2011 NVIDIA Corporation
  Copyright (c) 2011-2012 Cass Everitt
  Copyright (c) 2012 Scott Nations
  Copyright (c) 2012 Mathias Schott
  Copyright (c) 2012 Nigel Stewart
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification,
  are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
  OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#ifndef __REGAL_LOOKUP_H__
#define __REGAL_LOOKUP_H__

#include "RegalUtil.h"

REGAL_GLOBAL_BEGIN

#include <cstdlib>
#include <cstring>

REGAL_GLOBAL_END

REGAL_NAMESPACE_BEGIN

namespace Lookup {

inline int NameCmp(const void *a, const void *b)
{
  return std::strcmp(*(const char **) a, *(const char **) b);
}

extern const char * const gl_Name[2392];
extern const void *gl_Value[2392];
extern const size_t gl_Offset[2392];

template<typename T>
T
gl_Lookup(const char *name, T def = NULL)
{
  const char **res = (const char **) std::bsearch(&name, gl_Name, 2391, sizeof(const char *), NameCmp);
  return res ? reinterpret_cast<T>(const_cast<void *>(gl_Value[(size_t) (res - gl_Name)])) : def;
}

inline size_t gl_LookupOffset(const char *name)
{
  const char **res = (const char **) std::bsearch(&name, gl_Name, 2391, sizeof(const char *), NameCmp);
  return res ? gl_Offset[(size_t) (res - gl_Name)] : 0;
}

#ifdef REGAL_SYS_WGL

extern const char * const wgl_Name[136];
extern const void *wgl_Value[136];
extern const size_t wgl_Offset[136];

template<typename T>
T
wgl_Lookup(const char *name, T def = NULL)
{
  const char **res = (const char **) std::bsearch(&name, wgl_Name, 135, sizeof(const char *), NameCmp);
  return res ? reinterpret_cast<T>(const_cast<void *>(wgl_Value[(size_t) (res - wgl_Name)])) : def;
}

inline size_t wgl_LookupOffset(const char *name)
{
  const char **res = (const char **) std::bsearch(&name, wgl_Name, 135, sizeof(const char *), NameCmp);
  return res ? wgl_Offset[(size_t) (res - wgl_Name)] : 0;
}

#endif

#ifdef REGAL_SYS_GLX

extern const char * const glx_Name[107];
extern const void *glx_Value[107];
extern const size_t glx_Offset[107];

template<typename T>
T
glx_Lookup(const char *name, T def = NULL)
{
  const char **res = (const char **) std::bsearch(&name, glx_Name, 106, sizeof(const char *), NameCmp);
  return res ? reinterpret_cast<T>(const_cast<void *>(glx_Value[(size_t) (res - glx_Name)])) : def;
}

inline size_t glx_LookupOffset(const char *name)
{
  const char **res = (const char **) std::bsearch(&name, glx_Name, 106, sizeof(const char *), NameCmp);
  return res ? glx_Offset[(size_t) (res - glx_Name)] : 0;
}

#endif

#ifdef REGAL_SYS_OSX

extern const char * const cgl_Name[53];
extern const void *cgl_Value[53];
extern const size_t cgl_Offset[53];

template<typename T>
T
cgl_Lookup(const char *name, T def = NULL)
{
  const char **res = (const char **) std::bsearch(&name, cgl_Name, 52, sizeof(const char *), NameCmp);
  return res ? reinterpret_cast<T>(const_cast<void *>(cgl_Value[(size_t) (res - cgl_Name)])) : def;
}

inline size_t cgl_LookupOffset(const char *name)
{
  const char **res = (const char **) std::bsearch(&name, cgl_Name, 52, sizeof(const char *), NameCmp);
  return res ? cgl_Offset[(size_t) (res - cgl_Name)] : 0;
}

#endif

#ifdef REGAL_SYS_ANDROID

extern const char * const egl_Name[35];
extern const void *egl_Value[35];
extern const size_t egl_Offset[35];

template<typename T>
T
egl_Lookup(const char *name, T def = NULL)
{
  const char **res = (const char **) std::bsearch(&name, egl_Name, 34, sizeof(const char *), NameCmp);
  return res ? reinterpret_cast<T>(const_cast<void *>(egl_Value[(size_t) (res - egl_Name)])) : def;
}

inline size_t egl_LookupOffset(const char *name)
{
  const char **res = (const char **) std::bsearch(&name, egl_Name, 34, sizeof(const char *), NameCmp);
  return res ? egl_Offset[(size_t) (res - egl_Name)] : 0;
}

#endif

}

REGAL_NAMESPACE_END

#endif
