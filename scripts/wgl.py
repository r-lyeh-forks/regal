import Api
from Api import Api
from Api import Function, Typedef, Enum
from Api import Return, Parameter, Input, Output, InputOutput
from Api import Enumerant

wgl = Api()
VOID = Typedef('VOID','void')

PVOID = Typedef('PVOID','void *')
PVOID.default = '0'

HANDLE = Typedef('HANDLE','PVOID')
HANDLE.default = '0'

LPCSTR = Typedef('LPCSTR','const char *')
LPCSTR.default = '0'

INT32 = Typedef('INT32','signed int')
INT32.default = '0'

INT64 = Typedef('INT64','signed __int64')
INT64.default = '0'

LPVOID = Typedef('LPVOID','void *')
LPVOID.default = '0'

BOOL = Typedef('BOOL','int')
BOOL.default = '0'

DWORD = Typedef('DWORD','unsigned long')
DWORD.default = '0'

FLOAT = Typedef('FLOAT','float')
FLOAT.default = '0'

INT = Typedef('INT','int')
INT.default = '0'

UINT = Typedef('UINT','unsigned int')
UINT.default = '0'

USHORT = Typedef('USHORT','unsigned short')
USHORT.default = '0'

PROC = Typedef('PROC','void *')
PROC.default = 'NULL'

COLORREF = Typedef('COLORREF','DWORD')
COLORREF.default = '0'

HDC = Typedef('HDC','HANDLE')
HDC.default = '0'
HDC.regal = False

HGLRC = Typedef('HGLRC','HANDLE')
HGLRC.default = '0'
HGLRC.regal = False

GLYPHMETRICSFLOAT = Typedef('GLYPHMETRICSFLOAT','struct _GLYPHMETRICSFLOAT')

LPGLYPHMETRICSFLOAT = Typedef('LPGLYPHMETRICSFLOAT','GLYPHMETRICSFLOAT *')

LAYERPLANEDESCRIPTOR = Typedef('LAYERPLANEDESCRIPTOR','struct tagLAYERPLANEDESCRIPTOR')

LPLAYERPLANEDESCRIPTOR = Typedef('LPLAYERPLANEDESCRIPTOR','LAYERPLANEDESCRIPTOR *')

PIXELFORMATDESCRIPTOR = Typedef('PIXELFORMATDESCRIPTOR','struct tagPIXELFORMATDESCRIPTOR')

LPPIXELFORMATDESCRIPTOR = Typedef('LPPIXELFORMATDESCRIPTOR','PIXELFORMATDESCRIPTOR *')

POINTFLOAT = Typedef('POINTFLOAT','struct _POINTFLOAT')

WGLSWAP = Typedef('WGLSWAP','struct _WGLSWAP')

HPBUFFERARB = Typedef('HPBUFFERARB','struct HPBUFFERARB__ *')

HPBUFFEREXT = Typedef('HPBUFFEREXT','struct HPBUFFEREXT__ *')

HGPUNV = Typedef('HGPUNV','struct HGPUNV__ *')

HPVIDEODEV = Typedef('HPVIDEODEV','struct HPVIDEODEV__ *')

HVIDEOINPUTDEVICENV = Typedef('HVIDEOINPUTDEVICENV','struct HVIDEOINPUTDEVICENV__ *')

HVIDEOOUTPUTDEVICENV = Typedef('HVIDEOOUTPUTDEVICENV','struct HVIDEOOUTPUTDEVICENV__ *')

PGPU_DEVICE = Typedef('PGPU_DEVICE','struct GPU_DEVICE *')

wgl.add(VOID)
wgl.add(PVOID)
wgl.add(HANDLE)
wgl.add(LPCSTR)
wgl.add(INT32)
wgl.add(INT64)
wgl.add(LPVOID)
wgl.add(BOOL)
wgl.add(DWORD)
wgl.add(FLOAT)
wgl.add(INT)
wgl.add(UINT)
wgl.add(USHORT)
wgl.add(PROC)
wgl.add(COLORREF)
wgl.add(HDC)
wgl.add(HGLRC)
wgl.add(GLYPHMETRICSFLOAT)
wgl.add(LPGLYPHMETRICSFLOAT)
wgl.add(LAYERPLANEDESCRIPTOR)
wgl.add(LPLAYERPLANEDESCRIPTOR)
wgl.add(PIXELFORMATDESCRIPTOR)
wgl.add(LPPIXELFORMATDESCRIPTOR)
wgl.add(POINTFLOAT)
wgl.add(WGLSWAP)
wgl.add(HPBUFFERARB)
wgl.add(HPBUFFEREXT)
wgl.add(HGPUNV)
wgl.add(HPVIDEODEV)
wgl.add(HVIDEOINPUTDEVICENV)
wgl.add(HVIDEOOUTPUTDEVICENV)
wgl.add(PGPU_DEVICE)


defines = Enum('defines')
wgl.add(defines)

# WGL_3DL_stereo_control

WGL_STEREO_EMITTER_DISABLE_3DL = Enumerant('WGL_STEREO_EMITTER_DISABLE_3DL', 8278, 'WGL_3DL_stereo_control')
WGL_STEREO_EMITTER_ENABLE_3DL = Enumerant('WGL_STEREO_EMITTER_ENABLE_3DL', 8277, 'WGL_3DL_stereo_control')
WGL_STEREO_POLARITY_INVERT_3DL = Enumerant('WGL_STEREO_POLARITY_INVERT_3DL', 8280, 'WGL_3DL_stereo_control')
WGL_STEREO_POLARITY_NORMAL_3DL = Enumerant('WGL_STEREO_POLARITY_NORMAL_3DL', 8279, 'WGL_3DL_stereo_control')

defines.add(WGL_STEREO_EMITTER_DISABLE_3DL)
defines.add(WGL_STEREO_EMITTER_ENABLE_3DL)
defines.add(WGL_STEREO_POLARITY_INVERT_3DL)
defines.add(WGL_STEREO_POLARITY_NORMAL_3DL)

# WGL_AMD_gpu_association

WGL_GPU_CLOCK_AMD = Enumerant('WGL_GPU_CLOCK_AMD', 8612, 'WGL_AMD_gpu_association')
WGL_GPU_FASTEST_TARGET_GPUS_AMD = Enumerant('WGL_GPU_FASTEST_TARGET_GPUS_AMD', 8610, 'WGL_AMD_gpu_association')
WGL_GPU_NUM_PIPES_AMD = Enumerant('WGL_GPU_NUM_PIPES_AMD', 8613, 'WGL_AMD_gpu_association')
WGL_GPU_NUM_RB_AMD = Enumerant('WGL_GPU_NUM_RB_AMD', 8615, 'WGL_AMD_gpu_association')
WGL_GPU_NUM_SIMD_AMD = Enumerant('WGL_GPU_NUM_SIMD_AMD', 8614, 'WGL_AMD_gpu_association')
WGL_GPU_NUM_SPI_AMD = Enumerant('WGL_GPU_NUM_SPI_AMD', 8616, 'WGL_AMD_gpu_association')
WGL_GPU_OPENGL_VERSION_STRING_AMD = Enumerant('WGL_GPU_OPENGL_VERSION_STRING_AMD', 7938, 'WGL_AMD_gpu_association')
WGL_GPU_RAM_AMD = Enumerant('WGL_GPU_RAM_AMD', 8611, 'WGL_AMD_gpu_association')
WGL_GPU_RENDERER_STRING_AMD = Enumerant('WGL_GPU_RENDERER_STRING_AMD', 7937, 'WGL_AMD_gpu_association')
WGL_GPU_VENDOR_AMD = Enumerant('WGL_GPU_VENDOR_AMD', 7936, 'WGL_AMD_gpu_association')

defines.add(WGL_GPU_CLOCK_AMD)
defines.add(WGL_GPU_FASTEST_TARGET_GPUS_AMD)
defines.add(WGL_GPU_NUM_PIPES_AMD)
defines.add(WGL_GPU_NUM_RB_AMD)
defines.add(WGL_GPU_NUM_SIMD_AMD)
defines.add(WGL_GPU_NUM_SPI_AMD)
defines.add(WGL_GPU_OPENGL_VERSION_STRING_AMD)
defines.add(WGL_GPU_RAM_AMD)
defines.add(WGL_GPU_RENDERER_STRING_AMD)
defines.add(WGL_GPU_VENDOR_AMD)

# WGL_ARB_buffer_region

WGL_BACK_COLOR_BUFFER_BIT_ARB = Enumerant('WGL_BACK_COLOR_BUFFER_BIT_ARB', 2, 'WGL_ARB_buffer_region')
WGL_DEPTH_BUFFER_BIT_ARB = Enumerant('WGL_DEPTH_BUFFER_BIT_ARB', 4, 'WGL_ARB_buffer_region')
WGL_FRONT_COLOR_BUFFER_BIT_ARB = Enumerant('WGL_FRONT_COLOR_BUFFER_BIT_ARB', 1, 'WGL_ARB_buffer_region')
WGL_STENCIL_BUFFER_BIT_ARB = Enumerant('WGL_STENCIL_BUFFER_BIT_ARB', 8, 'WGL_ARB_buffer_region')

defines.add(WGL_BACK_COLOR_BUFFER_BIT_ARB)
defines.add(WGL_DEPTH_BUFFER_BIT_ARB)
defines.add(WGL_FRONT_COLOR_BUFFER_BIT_ARB)
defines.add(WGL_STENCIL_BUFFER_BIT_ARB)

# WGL_ARB_create_context

WGL_CONTEXT_DEBUG_BIT_ARB = Enumerant('WGL_CONTEXT_DEBUG_BIT_ARB', 1, 'WGL_ARB_create_context')
WGL_CONTEXT_FLAGS_ARB = Enumerant('WGL_CONTEXT_FLAGS_ARB', 8340, 'WGL_ARB_create_context')
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB = Enumerant('WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB', 2, 'WGL_ARB_create_context')
WGL_CONTEXT_LAYER_PLANE_ARB = Enumerant('WGL_CONTEXT_LAYER_PLANE_ARB', 8339, 'WGL_ARB_create_context')
WGL_CONTEXT_MAJOR_VERSION_ARB = Enumerant('WGL_CONTEXT_MAJOR_VERSION_ARB', 8337, 'WGL_ARB_create_context')
WGL_CONTEXT_MINOR_VERSION_ARB = Enumerant('WGL_CONTEXT_MINOR_VERSION_ARB', 8338, 'WGL_ARB_create_context')

defines.add(WGL_CONTEXT_DEBUG_BIT_ARB)
defines.add(WGL_CONTEXT_FLAGS_ARB)
defines.add(WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB)
defines.add(WGL_CONTEXT_LAYER_PLANE_ARB)
defines.add(WGL_CONTEXT_MAJOR_VERSION_ARB)
defines.add(WGL_CONTEXT_MINOR_VERSION_ARB)

# WGL_ARB_create_context_profile

WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB = Enumerant('WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB', 2, 'WGL_ARB_create_context_profile')
WGL_CONTEXT_CORE_PROFILE_BIT_ARB = Enumerant('WGL_CONTEXT_CORE_PROFILE_BIT_ARB', 1, 'WGL_ARB_create_context_profile')
WGL_CONTEXT_PROFILE_MASK_ARB = Enumerant('WGL_CONTEXT_PROFILE_MASK_ARB', 37158, 'WGL_ARB_create_context_profile')

defines.add(WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB)
defines.add(WGL_CONTEXT_CORE_PROFILE_BIT_ARB)
defines.add(WGL_CONTEXT_PROFILE_MASK_ARB)

# WGL_ARB_framebuffer_sRGB

WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB = Enumerant('WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB', 8361, 'WGL_ARB_framebuffer_sRGB')

defines.add(WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB)

# WGL_ARB_make_current_read

ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB = Enumerant('ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB', 8276, 'WGL_ARB_make_current_read')
ERROR_INVALID_PIXEL_TYPE_ARB = Enumerant('ERROR_INVALID_PIXEL_TYPE_ARB', 8259, 'WGL_ARB_make_current_read')

defines.add(ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB)
defines.add(ERROR_INVALID_PIXEL_TYPE_ARB)

# WGL_ARB_multisample

WGL_SAMPLES_ARB = Enumerant('WGL_SAMPLES_ARB', 8258, 'WGL_ARB_multisample')
WGL_SAMPLE_BUFFERS_ARB = Enumerant('WGL_SAMPLE_BUFFERS_ARB', 8257, 'WGL_ARB_multisample')

defines.add(WGL_SAMPLES_ARB)
defines.add(WGL_SAMPLE_BUFFERS_ARB)

# WGL_ARB_pbuffer

WGL_DRAW_TO_PBUFFER_ARB = Enumerant('WGL_DRAW_TO_PBUFFER_ARB', 8237, 'WGL_ARB_pbuffer')
WGL_MAX_PBUFFER_HEIGHT_ARB = Enumerant('WGL_MAX_PBUFFER_HEIGHT_ARB', 8240, 'WGL_ARB_pbuffer')
WGL_MAX_PBUFFER_PIXELS_ARB = Enumerant('WGL_MAX_PBUFFER_PIXELS_ARB', 8238, 'WGL_ARB_pbuffer')
WGL_MAX_PBUFFER_WIDTH_ARB = Enumerant('WGL_MAX_PBUFFER_WIDTH_ARB', 8239, 'WGL_ARB_pbuffer')
WGL_PBUFFER_HEIGHT_ARB = Enumerant('WGL_PBUFFER_HEIGHT_ARB', 8245, 'WGL_ARB_pbuffer')
WGL_PBUFFER_LARGEST_ARB = Enumerant('WGL_PBUFFER_LARGEST_ARB', 8243, 'WGL_ARB_pbuffer')
WGL_PBUFFER_LOST_ARB = Enumerant('WGL_PBUFFER_LOST_ARB', 8246, 'WGL_ARB_pbuffer')
WGL_PBUFFER_WIDTH_ARB = Enumerant('WGL_PBUFFER_WIDTH_ARB', 8244, 'WGL_ARB_pbuffer')

defines.add(WGL_DRAW_TO_PBUFFER_ARB)
defines.add(WGL_MAX_PBUFFER_HEIGHT_ARB)
defines.add(WGL_MAX_PBUFFER_PIXELS_ARB)
defines.add(WGL_MAX_PBUFFER_WIDTH_ARB)
defines.add(WGL_PBUFFER_HEIGHT_ARB)
defines.add(WGL_PBUFFER_LARGEST_ARB)
defines.add(WGL_PBUFFER_LOST_ARB)
defines.add(WGL_PBUFFER_WIDTH_ARB)

# WGL_ARB_pixel_format

WGL_ACCELERATION_ARB = Enumerant('WGL_ACCELERATION_ARB', 8195, 'WGL_ARB_pixel_format')
WGL_ACCUM_ALPHA_BITS_ARB = Enumerant('WGL_ACCUM_ALPHA_BITS_ARB', 8225, 'WGL_ARB_pixel_format')
WGL_ACCUM_BITS_ARB = Enumerant('WGL_ACCUM_BITS_ARB', 8221, 'WGL_ARB_pixel_format')
WGL_ACCUM_BLUE_BITS_ARB = Enumerant('WGL_ACCUM_BLUE_BITS_ARB', 8224, 'WGL_ARB_pixel_format')
WGL_ACCUM_GREEN_BITS_ARB = Enumerant('WGL_ACCUM_GREEN_BITS_ARB', 8223, 'WGL_ARB_pixel_format')
WGL_ACCUM_RED_BITS_ARB = Enumerant('WGL_ACCUM_RED_BITS_ARB', 8222, 'WGL_ARB_pixel_format')
WGL_ALPHA_BITS_ARB = Enumerant('WGL_ALPHA_BITS_ARB', 8219, 'WGL_ARB_pixel_format')
WGL_ALPHA_SHIFT_ARB = Enumerant('WGL_ALPHA_SHIFT_ARB', 8220, 'WGL_ARB_pixel_format')
WGL_AUX_BUFFERS_ARB = Enumerant('WGL_AUX_BUFFERS_ARB', 8228, 'WGL_ARB_pixel_format')
WGL_BLUE_BITS_ARB = Enumerant('WGL_BLUE_BITS_ARB', 8217, 'WGL_ARB_pixel_format')
WGL_BLUE_SHIFT_ARB = Enumerant('WGL_BLUE_SHIFT_ARB', 8218, 'WGL_ARB_pixel_format')
WGL_COLOR_BITS_ARB = Enumerant('WGL_COLOR_BITS_ARB', 8212, 'WGL_ARB_pixel_format')
WGL_DEPTH_BITS_ARB = Enumerant('WGL_DEPTH_BITS_ARB', 8226, 'WGL_ARB_pixel_format')
WGL_DOUBLE_BUFFER_ARB = Enumerant('WGL_DOUBLE_BUFFER_ARB', 8209, 'WGL_ARB_pixel_format')
WGL_DRAW_TO_BITMAP_ARB = Enumerant('WGL_DRAW_TO_BITMAP_ARB', 8194, 'WGL_ARB_pixel_format')
WGL_DRAW_TO_WINDOW_ARB = Enumerant('WGL_DRAW_TO_WINDOW_ARB', 8193, 'WGL_ARB_pixel_format')
WGL_FULL_ACCELERATION_ARB = Enumerant('WGL_FULL_ACCELERATION_ARB', 8231, 'WGL_ARB_pixel_format')
WGL_GENERIC_ACCELERATION_ARB = Enumerant('WGL_GENERIC_ACCELERATION_ARB', 8230, 'WGL_ARB_pixel_format')
WGL_GREEN_BITS_ARB = Enumerant('WGL_GREEN_BITS_ARB', 8215, 'WGL_ARB_pixel_format')
WGL_GREEN_SHIFT_ARB = Enumerant('WGL_GREEN_SHIFT_ARB', 8216, 'WGL_ARB_pixel_format')
WGL_NEED_PALETTE_ARB = Enumerant('WGL_NEED_PALETTE_ARB', 8196, 'WGL_ARB_pixel_format')
WGL_NEED_SYSTEM_PALETTE_ARB = Enumerant('WGL_NEED_SYSTEM_PALETTE_ARB', 8197, 'WGL_ARB_pixel_format')
WGL_NO_ACCELERATION_ARB = Enumerant('WGL_NO_ACCELERATION_ARB', 8229, 'WGL_ARB_pixel_format')
WGL_NUMBER_OVERLAYS_ARB = Enumerant('WGL_NUMBER_OVERLAYS_ARB', 8200, 'WGL_ARB_pixel_format')
WGL_NUMBER_PIXEL_FORMATS_ARB = Enumerant('WGL_NUMBER_PIXEL_FORMATS_ARB', 8192, 'WGL_ARB_pixel_format')
WGL_NUMBER_UNDERLAYS_ARB = Enumerant('WGL_NUMBER_UNDERLAYS_ARB', 8201, 'WGL_ARB_pixel_format')
WGL_PIXEL_TYPE_ARB = Enumerant('WGL_PIXEL_TYPE_ARB', 8211, 'WGL_ARB_pixel_format')
WGL_RED_BITS_ARB = Enumerant('WGL_RED_BITS_ARB', 8213, 'WGL_ARB_pixel_format')
WGL_RED_SHIFT_ARB = Enumerant('WGL_RED_SHIFT_ARB', 8214, 'WGL_ARB_pixel_format')
WGL_SHARE_ACCUM_ARB = Enumerant('WGL_SHARE_ACCUM_ARB', 8206, 'WGL_ARB_pixel_format')
WGL_SHARE_DEPTH_ARB = Enumerant('WGL_SHARE_DEPTH_ARB', 8204, 'WGL_ARB_pixel_format')
WGL_SHARE_STENCIL_ARB = Enumerant('WGL_SHARE_STENCIL_ARB', 8205, 'WGL_ARB_pixel_format')
WGL_STENCIL_BITS_ARB = Enumerant('WGL_STENCIL_BITS_ARB', 8227, 'WGL_ARB_pixel_format')
WGL_STEREO_ARB = Enumerant('WGL_STEREO_ARB', 8210, 'WGL_ARB_pixel_format')
WGL_SUPPORT_GDI_ARB = Enumerant('WGL_SUPPORT_GDI_ARB', 8207, 'WGL_ARB_pixel_format')
WGL_SUPPORT_OPENGL_ARB = Enumerant('WGL_SUPPORT_OPENGL_ARB', 8208, 'WGL_ARB_pixel_format')
WGL_SWAP_COPY_ARB = Enumerant('WGL_SWAP_COPY_ARB', 8233, 'WGL_ARB_pixel_format')
WGL_SWAP_EXCHANGE_ARB = Enumerant('WGL_SWAP_EXCHANGE_ARB', 8232, 'WGL_ARB_pixel_format')
WGL_SWAP_LAYER_BUFFERS_ARB = Enumerant('WGL_SWAP_LAYER_BUFFERS_ARB', 8198, 'WGL_ARB_pixel_format')
WGL_SWAP_METHOD_ARB = Enumerant('WGL_SWAP_METHOD_ARB', 8199, 'WGL_ARB_pixel_format')
WGL_SWAP_UNDEFINED_ARB = Enumerant('WGL_SWAP_UNDEFINED_ARB', 8234, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_ALPHA_VALUE_ARB = Enumerant('WGL_TRANSPARENT_ALPHA_VALUE_ARB', 8250, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_ARB = Enumerant('WGL_TRANSPARENT_ARB', 8202, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_BLUE_VALUE_ARB = Enumerant('WGL_TRANSPARENT_BLUE_VALUE_ARB', 8249, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_GREEN_VALUE_ARB = Enumerant('WGL_TRANSPARENT_GREEN_VALUE_ARB', 8248, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_INDEX_VALUE_ARB = Enumerant('WGL_TRANSPARENT_INDEX_VALUE_ARB', 8251, 'WGL_ARB_pixel_format')
WGL_TRANSPARENT_RED_VALUE_ARB = Enumerant('WGL_TRANSPARENT_RED_VALUE_ARB', 8247, 'WGL_ARB_pixel_format')
WGL_TYPE_COLORINDEX_ARB = Enumerant('WGL_TYPE_COLORINDEX_ARB', 8236, 'WGL_ARB_pixel_format')
WGL_TYPE_RGBA_ARB = Enumerant('WGL_TYPE_RGBA_ARB', 8235, 'WGL_ARB_pixel_format')

defines.add(WGL_ACCELERATION_ARB)
defines.add(WGL_ACCUM_ALPHA_BITS_ARB)
defines.add(WGL_ACCUM_BITS_ARB)
defines.add(WGL_ACCUM_BLUE_BITS_ARB)
defines.add(WGL_ACCUM_GREEN_BITS_ARB)
defines.add(WGL_ACCUM_RED_BITS_ARB)
defines.add(WGL_ALPHA_BITS_ARB)
defines.add(WGL_ALPHA_SHIFT_ARB)
defines.add(WGL_AUX_BUFFERS_ARB)
defines.add(WGL_BLUE_BITS_ARB)
defines.add(WGL_BLUE_SHIFT_ARB)
defines.add(WGL_COLOR_BITS_ARB)
defines.add(WGL_DEPTH_BITS_ARB)
defines.add(WGL_DOUBLE_BUFFER_ARB)
defines.add(WGL_DRAW_TO_BITMAP_ARB)
defines.add(WGL_DRAW_TO_WINDOW_ARB)
defines.add(WGL_FULL_ACCELERATION_ARB)
defines.add(WGL_GENERIC_ACCELERATION_ARB)
defines.add(WGL_GREEN_BITS_ARB)
defines.add(WGL_GREEN_SHIFT_ARB)
defines.add(WGL_NEED_PALETTE_ARB)
defines.add(WGL_NEED_SYSTEM_PALETTE_ARB)
defines.add(WGL_NO_ACCELERATION_ARB)
defines.add(WGL_NUMBER_OVERLAYS_ARB)
defines.add(WGL_NUMBER_PIXEL_FORMATS_ARB)
defines.add(WGL_NUMBER_UNDERLAYS_ARB)
defines.add(WGL_PIXEL_TYPE_ARB)
defines.add(WGL_RED_BITS_ARB)
defines.add(WGL_RED_SHIFT_ARB)
defines.add(WGL_SHARE_ACCUM_ARB)
defines.add(WGL_SHARE_DEPTH_ARB)
defines.add(WGL_SHARE_STENCIL_ARB)
defines.add(WGL_STENCIL_BITS_ARB)
defines.add(WGL_STEREO_ARB)
defines.add(WGL_SUPPORT_GDI_ARB)
defines.add(WGL_SUPPORT_OPENGL_ARB)
defines.add(WGL_SWAP_COPY_ARB)
defines.add(WGL_SWAP_EXCHANGE_ARB)
defines.add(WGL_SWAP_LAYER_BUFFERS_ARB)
defines.add(WGL_SWAP_METHOD_ARB)
defines.add(WGL_SWAP_UNDEFINED_ARB)
defines.add(WGL_TRANSPARENT_ALPHA_VALUE_ARB)
defines.add(WGL_TRANSPARENT_ARB)
defines.add(WGL_TRANSPARENT_BLUE_VALUE_ARB)
defines.add(WGL_TRANSPARENT_GREEN_VALUE_ARB)
defines.add(WGL_TRANSPARENT_INDEX_VALUE_ARB)
defines.add(WGL_TRANSPARENT_RED_VALUE_ARB)
defines.add(WGL_TYPE_COLORINDEX_ARB)
defines.add(WGL_TYPE_RGBA_ARB)

# WGL_ARB_pixel_format_float

WGL_TYPE_RGBA_FLOAT_ARB = Enumerant('WGL_TYPE_RGBA_FLOAT_ARB', 8608, 'WGL_ARB_pixel_format_float')

defines.add(WGL_TYPE_RGBA_FLOAT_ARB)

# WGL_ARB_render_texture

WGL_AUX0_ARB = Enumerant('WGL_AUX0_ARB', 8327, 'WGL_ARB_render_texture')
WGL_AUX1_ARB = Enumerant('WGL_AUX1_ARB', 8328, 'WGL_ARB_render_texture')
WGL_AUX2_ARB = Enumerant('WGL_AUX2_ARB', 8329, 'WGL_ARB_render_texture')
WGL_AUX3_ARB = Enumerant('WGL_AUX3_ARB', 8330, 'WGL_ARB_render_texture')
WGL_AUX4_ARB = Enumerant('WGL_AUX4_ARB', 8331, 'WGL_ARB_render_texture')
WGL_AUX5_ARB = Enumerant('WGL_AUX5_ARB', 8332, 'WGL_ARB_render_texture')
WGL_AUX6_ARB = Enumerant('WGL_AUX6_ARB', 8333, 'WGL_ARB_render_texture')
WGL_AUX7_ARB = Enumerant('WGL_AUX7_ARB', 8334, 'WGL_ARB_render_texture')
WGL_AUX8_ARB = Enumerant('WGL_AUX8_ARB', 8335, 'WGL_ARB_render_texture')
WGL_AUX9_ARB = Enumerant('WGL_AUX9_ARB', 8336, 'WGL_ARB_render_texture')
WGL_BACK_LEFT_ARB = Enumerant('WGL_BACK_LEFT_ARB', 8325, 'WGL_ARB_render_texture')
WGL_BACK_RIGHT_ARB = Enumerant('WGL_BACK_RIGHT_ARB', 8326, 'WGL_ARB_render_texture')
WGL_BIND_TO_TEXTURE_RGBA_ARB = Enumerant('WGL_BIND_TO_TEXTURE_RGBA_ARB', 8305, 'WGL_ARB_render_texture')
WGL_BIND_TO_TEXTURE_RGB_ARB = Enumerant('WGL_BIND_TO_TEXTURE_RGB_ARB', 8304, 'WGL_ARB_render_texture')
WGL_CUBE_MAP_FACE_ARB = Enumerant('WGL_CUBE_MAP_FACE_ARB', 8316, 'WGL_ARB_render_texture')
WGL_FRONT_LEFT_ARB = Enumerant('WGL_FRONT_LEFT_ARB', 8323, 'WGL_ARB_render_texture')
WGL_FRONT_RIGHT_ARB = Enumerant('WGL_FRONT_RIGHT_ARB', 8324, 'WGL_ARB_render_texture')
WGL_MIPMAP_LEVEL_ARB = Enumerant('WGL_MIPMAP_LEVEL_ARB', 8315, 'WGL_ARB_render_texture')
WGL_MIPMAP_TEXTURE_ARB = Enumerant('WGL_MIPMAP_TEXTURE_ARB', 8308, 'WGL_ARB_render_texture')
WGL_TEXTURE_1D_ARB = Enumerant('WGL_TEXTURE_1D_ARB', 8313, 'WGL_ARB_render_texture')
WGL_TEXTURE_2D_ARB = Enumerant('WGL_TEXTURE_2D_ARB', 8314, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_ARB', 8312, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB', 8318, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB', 8320, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB', 8322, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB', 8317, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB', 8319, 'WGL_ARB_render_texture')
WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = Enumerant('WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB', 8321, 'WGL_ARB_render_texture')
WGL_TEXTURE_FORMAT_ARB = Enumerant('WGL_TEXTURE_FORMAT_ARB', 8306, 'WGL_ARB_render_texture')
WGL_TEXTURE_RGBA_ARB = Enumerant('WGL_TEXTURE_RGBA_ARB', 8310, 'WGL_ARB_render_texture')
WGL_TEXTURE_RGB_ARB = Enumerant('WGL_TEXTURE_RGB_ARB', 8309, 'WGL_ARB_render_texture')
WGL_TEXTURE_TARGET_ARB = Enumerant('WGL_TEXTURE_TARGET_ARB', 8307, 'WGL_ARB_render_texture')

defines.add(WGL_AUX0_ARB)
defines.add(WGL_AUX1_ARB)
defines.add(WGL_AUX2_ARB)
defines.add(WGL_AUX3_ARB)
defines.add(WGL_AUX4_ARB)
defines.add(WGL_AUX5_ARB)
defines.add(WGL_AUX6_ARB)
defines.add(WGL_AUX7_ARB)
defines.add(WGL_AUX8_ARB)
defines.add(WGL_AUX9_ARB)
defines.add(WGL_BACK_LEFT_ARB)
defines.add(WGL_BACK_RIGHT_ARB)
defines.add(WGL_BIND_TO_TEXTURE_RGBA_ARB)
defines.add(WGL_BIND_TO_TEXTURE_RGB_ARB)
defines.add(WGL_CUBE_MAP_FACE_ARB)
defines.add(WGL_FRONT_LEFT_ARB)
defines.add(WGL_FRONT_RIGHT_ARB)
defines.add(WGL_MIPMAP_LEVEL_ARB)
defines.add(WGL_MIPMAP_TEXTURE_ARB)
defines.add(WGL_TEXTURE_1D_ARB)
defines.add(WGL_TEXTURE_2D_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB)
defines.add(WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB)
defines.add(WGL_TEXTURE_FORMAT_ARB)
defines.add(WGL_TEXTURE_RGBA_ARB)
defines.add(WGL_TEXTURE_RGB_ARB)
defines.add(WGL_TEXTURE_TARGET_ARB)

# WGL_ATI_pixel_format_float

GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = Enumerant('GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI', 34869, 'WGL_ATI_pixel_format_float')
GL_RGBA_FLOAT_MODE_ATI = Enumerant('GL_RGBA_FLOAT_MODE_ATI', 34848, 'WGL_ATI_pixel_format_float')
WGL_TYPE_RGBA_FLOAT_ATI = Enumerant('WGL_TYPE_RGBA_FLOAT_ATI', 8608, 'WGL_ATI_pixel_format_float')

defines.add(GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI)
defines.add(GL_RGBA_FLOAT_MODE_ATI)
defines.add(WGL_TYPE_RGBA_FLOAT_ATI)

# WGL_EXT_depth_float

WGL_DEPTH_FLOAT_EXT = Enumerant('WGL_DEPTH_FLOAT_EXT', 8256, 'WGL_EXT_depth_float')

defines.add(WGL_DEPTH_FLOAT_EXT)

# WGL_EXT_framebuffer_sRGB

WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT = Enumerant('WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT', 8361, 'WGL_EXT_framebuffer_sRGB')

defines.add(WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT)

# WGL_EXT_make_current_read

ERROR_INVALID_PIXEL_TYPE_EXT = Enumerant('ERROR_INVALID_PIXEL_TYPE_EXT', 8259, 'WGL_EXT_make_current_read')

defines.add(ERROR_INVALID_PIXEL_TYPE_EXT)

# WGL_EXT_multisample

WGL_SAMPLES_EXT = Enumerant('WGL_SAMPLES_EXT', 8258, 'WGL_EXT_multisample')
WGL_SAMPLE_BUFFERS_EXT = Enumerant('WGL_SAMPLE_BUFFERS_EXT', 8257, 'WGL_EXT_multisample')

defines.add(WGL_SAMPLES_EXT)
defines.add(WGL_SAMPLE_BUFFERS_EXT)

# WGL_EXT_pbuffer

WGL_DRAW_TO_PBUFFER_EXT = Enumerant('WGL_DRAW_TO_PBUFFER_EXT', 8237, 'WGL_EXT_pbuffer')
WGL_MAX_PBUFFER_HEIGHT_EXT = Enumerant('WGL_MAX_PBUFFER_HEIGHT_EXT', 8240, 'WGL_EXT_pbuffer')
WGL_MAX_PBUFFER_PIXELS_EXT = Enumerant('WGL_MAX_PBUFFER_PIXELS_EXT', 8238, 'WGL_EXT_pbuffer')
WGL_MAX_PBUFFER_WIDTH_EXT = Enumerant('WGL_MAX_PBUFFER_WIDTH_EXT', 8239, 'WGL_EXT_pbuffer')
WGL_OPTIMAL_PBUFFER_HEIGHT_EXT = Enumerant('WGL_OPTIMAL_PBUFFER_HEIGHT_EXT', 8242, 'WGL_EXT_pbuffer')
WGL_OPTIMAL_PBUFFER_WIDTH_EXT = Enumerant('WGL_OPTIMAL_PBUFFER_WIDTH_EXT', 8241, 'WGL_EXT_pbuffer')
WGL_PBUFFER_HEIGHT_EXT = Enumerant('WGL_PBUFFER_HEIGHT_EXT', 8245, 'WGL_EXT_pbuffer')
WGL_PBUFFER_LARGEST_EXT = Enumerant('WGL_PBUFFER_LARGEST_EXT', 8243, 'WGL_EXT_pbuffer')
WGL_PBUFFER_WIDTH_EXT = Enumerant('WGL_PBUFFER_WIDTH_EXT', 8244, 'WGL_EXT_pbuffer')

defines.add(WGL_DRAW_TO_PBUFFER_EXT)
defines.add(WGL_MAX_PBUFFER_HEIGHT_EXT)
defines.add(WGL_MAX_PBUFFER_PIXELS_EXT)
defines.add(WGL_MAX_PBUFFER_WIDTH_EXT)
defines.add(WGL_OPTIMAL_PBUFFER_HEIGHT_EXT)
defines.add(WGL_OPTIMAL_PBUFFER_WIDTH_EXT)
defines.add(WGL_PBUFFER_HEIGHT_EXT)
defines.add(WGL_PBUFFER_LARGEST_EXT)
defines.add(WGL_PBUFFER_WIDTH_EXT)

# WGL_EXT_pixel_format

WGL_ACCELERATION_EXT = Enumerant('WGL_ACCELERATION_EXT', 8195, 'WGL_EXT_pixel_format')
WGL_ACCUM_ALPHA_BITS_EXT = Enumerant('WGL_ACCUM_ALPHA_BITS_EXT', 8225, 'WGL_EXT_pixel_format')
WGL_ACCUM_BITS_EXT = Enumerant('WGL_ACCUM_BITS_EXT', 8221, 'WGL_EXT_pixel_format')
WGL_ACCUM_BLUE_BITS_EXT = Enumerant('WGL_ACCUM_BLUE_BITS_EXT', 8224, 'WGL_EXT_pixel_format')
WGL_ACCUM_GREEN_BITS_EXT = Enumerant('WGL_ACCUM_GREEN_BITS_EXT', 8223, 'WGL_EXT_pixel_format')
WGL_ACCUM_RED_BITS_EXT = Enumerant('WGL_ACCUM_RED_BITS_EXT', 8222, 'WGL_EXT_pixel_format')
WGL_ALPHA_BITS_EXT = Enumerant('WGL_ALPHA_BITS_EXT', 8219, 'WGL_EXT_pixel_format')
WGL_ALPHA_SHIFT_EXT = Enumerant('WGL_ALPHA_SHIFT_EXT', 8220, 'WGL_EXT_pixel_format')
WGL_AUX_BUFFERS_EXT = Enumerant('WGL_AUX_BUFFERS_EXT', 8228, 'WGL_EXT_pixel_format')
WGL_BLUE_BITS_EXT = Enumerant('WGL_BLUE_BITS_EXT', 8217, 'WGL_EXT_pixel_format')
WGL_BLUE_SHIFT_EXT = Enumerant('WGL_BLUE_SHIFT_EXT', 8218, 'WGL_EXT_pixel_format')
WGL_COLOR_BITS_EXT = Enumerant('WGL_COLOR_BITS_EXT', 8212, 'WGL_EXT_pixel_format')
WGL_DEPTH_BITS_EXT = Enumerant('WGL_DEPTH_BITS_EXT', 8226, 'WGL_EXT_pixel_format')
WGL_DOUBLE_BUFFER_EXT = Enumerant('WGL_DOUBLE_BUFFER_EXT', 8209, 'WGL_EXT_pixel_format')
WGL_DRAW_TO_BITMAP_EXT = Enumerant('WGL_DRAW_TO_BITMAP_EXT', 8194, 'WGL_EXT_pixel_format')
WGL_DRAW_TO_WINDOW_EXT = Enumerant('WGL_DRAW_TO_WINDOW_EXT', 8193, 'WGL_EXT_pixel_format')
WGL_FULL_ACCELERATION_EXT = Enumerant('WGL_FULL_ACCELERATION_EXT', 8231, 'WGL_EXT_pixel_format')
WGL_GENERIC_ACCELERATION_EXT = Enumerant('WGL_GENERIC_ACCELERATION_EXT', 8230, 'WGL_EXT_pixel_format')
WGL_GREEN_BITS_EXT = Enumerant('WGL_GREEN_BITS_EXT', 8215, 'WGL_EXT_pixel_format')
WGL_GREEN_SHIFT_EXT = Enumerant('WGL_GREEN_SHIFT_EXT', 8216, 'WGL_EXT_pixel_format')
WGL_NEED_PALETTE_EXT = Enumerant('WGL_NEED_PALETTE_EXT', 8196, 'WGL_EXT_pixel_format')
WGL_NEED_SYSTEM_PALETTE_EXT = Enumerant('WGL_NEED_SYSTEM_PALETTE_EXT', 8197, 'WGL_EXT_pixel_format')
WGL_NO_ACCELERATION_EXT = Enumerant('WGL_NO_ACCELERATION_EXT', 8229, 'WGL_EXT_pixel_format')
WGL_NUMBER_OVERLAYS_EXT = Enumerant('WGL_NUMBER_OVERLAYS_EXT', 8200, 'WGL_EXT_pixel_format')
WGL_NUMBER_PIXEL_FORMATS_EXT = Enumerant('WGL_NUMBER_PIXEL_FORMATS_EXT', 8192, 'WGL_EXT_pixel_format')
WGL_NUMBER_UNDERLAYS_EXT = Enumerant('WGL_NUMBER_UNDERLAYS_EXT', 8201, 'WGL_EXT_pixel_format')
WGL_PIXEL_TYPE_EXT = Enumerant('WGL_PIXEL_TYPE_EXT', 8211, 'WGL_EXT_pixel_format')
WGL_RED_BITS_EXT = Enumerant('WGL_RED_BITS_EXT', 8213, 'WGL_EXT_pixel_format')
WGL_RED_SHIFT_EXT = Enumerant('WGL_RED_SHIFT_EXT', 8214, 'WGL_EXT_pixel_format')
WGL_SHARE_ACCUM_EXT = Enumerant('WGL_SHARE_ACCUM_EXT', 8206, 'WGL_EXT_pixel_format')
WGL_SHARE_DEPTH_EXT = Enumerant('WGL_SHARE_DEPTH_EXT', 8204, 'WGL_EXT_pixel_format')
WGL_SHARE_STENCIL_EXT = Enumerant('WGL_SHARE_STENCIL_EXT', 8205, 'WGL_EXT_pixel_format')
WGL_STENCIL_BITS_EXT = Enumerant('WGL_STENCIL_BITS_EXT', 8227, 'WGL_EXT_pixel_format')
WGL_STEREO_EXT = Enumerant('WGL_STEREO_EXT', 8210, 'WGL_EXT_pixel_format')
WGL_SUPPORT_GDI_EXT = Enumerant('WGL_SUPPORT_GDI_EXT', 8207, 'WGL_EXT_pixel_format')
WGL_SUPPORT_OPENGL_EXT = Enumerant('WGL_SUPPORT_OPENGL_EXT', 8208, 'WGL_EXT_pixel_format')
WGL_SWAP_COPY_EXT = Enumerant('WGL_SWAP_COPY_EXT', 8233, 'WGL_EXT_pixel_format')
WGL_SWAP_EXCHANGE_EXT = Enumerant('WGL_SWAP_EXCHANGE_EXT', 8232, 'WGL_EXT_pixel_format')
WGL_SWAP_LAYER_BUFFERS_EXT = Enumerant('WGL_SWAP_LAYER_BUFFERS_EXT', 8198, 'WGL_EXT_pixel_format')
WGL_SWAP_METHOD_EXT = Enumerant('WGL_SWAP_METHOD_EXT', 8199, 'WGL_EXT_pixel_format')
WGL_SWAP_UNDEFINED_EXT = Enumerant('WGL_SWAP_UNDEFINED_EXT', 8234, 'WGL_EXT_pixel_format')
WGL_TRANSPARENT_EXT = Enumerant('WGL_TRANSPARENT_EXT', 8202, 'WGL_EXT_pixel_format')
WGL_TRANSPARENT_VALUE_EXT = Enumerant('WGL_TRANSPARENT_VALUE_EXT', 8203, 'WGL_EXT_pixel_format')
WGL_TYPE_COLORINDEX_EXT = Enumerant('WGL_TYPE_COLORINDEX_EXT', 8236, 'WGL_EXT_pixel_format')
WGL_TYPE_RGBA_EXT = Enumerant('WGL_TYPE_RGBA_EXT', 8235, 'WGL_EXT_pixel_format')

defines.add(WGL_ACCELERATION_EXT)
defines.add(WGL_ACCUM_ALPHA_BITS_EXT)
defines.add(WGL_ACCUM_BITS_EXT)
defines.add(WGL_ACCUM_BLUE_BITS_EXT)
defines.add(WGL_ACCUM_GREEN_BITS_EXT)
defines.add(WGL_ACCUM_RED_BITS_EXT)
defines.add(WGL_ALPHA_BITS_EXT)
defines.add(WGL_ALPHA_SHIFT_EXT)
defines.add(WGL_AUX_BUFFERS_EXT)
defines.add(WGL_BLUE_BITS_EXT)
defines.add(WGL_BLUE_SHIFT_EXT)
defines.add(WGL_COLOR_BITS_EXT)
defines.add(WGL_DEPTH_BITS_EXT)
defines.add(WGL_DOUBLE_BUFFER_EXT)
defines.add(WGL_DRAW_TO_BITMAP_EXT)
defines.add(WGL_DRAW_TO_WINDOW_EXT)
defines.add(WGL_FULL_ACCELERATION_EXT)
defines.add(WGL_GENERIC_ACCELERATION_EXT)
defines.add(WGL_GREEN_BITS_EXT)
defines.add(WGL_GREEN_SHIFT_EXT)
defines.add(WGL_NEED_PALETTE_EXT)
defines.add(WGL_NEED_SYSTEM_PALETTE_EXT)
defines.add(WGL_NO_ACCELERATION_EXT)
defines.add(WGL_NUMBER_OVERLAYS_EXT)
defines.add(WGL_NUMBER_PIXEL_FORMATS_EXT)
defines.add(WGL_NUMBER_UNDERLAYS_EXT)
defines.add(WGL_PIXEL_TYPE_EXT)
defines.add(WGL_RED_BITS_EXT)
defines.add(WGL_RED_SHIFT_EXT)
defines.add(WGL_SHARE_ACCUM_EXT)
defines.add(WGL_SHARE_DEPTH_EXT)
defines.add(WGL_SHARE_STENCIL_EXT)
defines.add(WGL_STENCIL_BITS_EXT)
defines.add(WGL_STEREO_EXT)
defines.add(WGL_SUPPORT_GDI_EXT)
defines.add(WGL_SUPPORT_OPENGL_EXT)
defines.add(WGL_SWAP_COPY_EXT)
defines.add(WGL_SWAP_EXCHANGE_EXT)
defines.add(WGL_SWAP_LAYER_BUFFERS_EXT)
defines.add(WGL_SWAP_METHOD_EXT)
defines.add(WGL_SWAP_UNDEFINED_EXT)
defines.add(WGL_TRANSPARENT_EXT)
defines.add(WGL_TRANSPARENT_VALUE_EXT)
defines.add(WGL_TYPE_COLORINDEX_EXT)
defines.add(WGL_TYPE_RGBA_EXT)

# WGL_EXT_pixel_format_packed_float

WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT = Enumerant('WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT', 8360, 'WGL_EXT_pixel_format_packed_float')

defines.add(WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT)

# WGL_I3D_digital_video_control

WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D = Enumerant('WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D', 8272, 'WGL_I3D_digital_video_control')
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D = Enumerant('WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D', 8273, 'WGL_I3D_digital_video_control')
WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D = Enumerant('WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D', 8274, 'WGL_I3D_digital_video_control')
WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D = Enumerant('WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D', 8275, 'WGL_I3D_digital_video_control')

defines.add(WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D)
defines.add(WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D)
defines.add(WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D)
defines.add(WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D)

# WGL_I3D_gamma

WGL_GAMMA_EXCLUDE_DESKTOP_I3D = Enumerant('WGL_GAMMA_EXCLUDE_DESKTOP_I3D', 8271, 'WGL_I3D_gamma')
WGL_GAMMA_TABLE_SIZE_I3D = Enumerant('WGL_GAMMA_TABLE_SIZE_I3D', 8270, 'WGL_I3D_gamma')

defines.add(WGL_GAMMA_EXCLUDE_DESKTOP_I3D)
defines.add(WGL_GAMMA_TABLE_SIZE_I3D)

# WGL_I3D_genlock

WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D = Enumerant('WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D', 8265, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D = Enumerant('WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D', 8264, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D = Enumerant('WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D', 8268, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D = Enumerant('WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D', 8266, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EDGE_RISING_I3D = Enumerant('WGL_GENLOCK_SOURCE_EDGE_RISING_I3D', 8267, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EXTERNAL_FIELD_I3D = Enumerant('WGL_GENLOCK_SOURCE_EXTERNAL_FIELD_I3D', 8262, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EXTERNAL_SYNC_I3D = Enumerant('WGL_GENLOCK_SOURCE_EXTERNAL_SYNC_I3D', 8261, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_EXTERNAL_TTL_I3D = Enumerant('WGL_GENLOCK_SOURCE_EXTERNAL_TTL_I3D', 8263, 'WGL_I3D_genlock')
WGL_GENLOCK_SOURCE_MULTIVIEW_I3D = Enumerant('WGL_GENLOCK_SOURCE_MULTIVIEW_I3D', 8260, 'WGL_I3D_genlock')

defines.add(WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D)
defines.add(WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D)
defines.add(WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D)
defines.add(WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D)
defines.add(WGL_GENLOCK_SOURCE_EDGE_RISING_I3D)
defines.add(WGL_GENLOCK_SOURCE_EXTERNAL_FIELD_I3D)
defines.add(WGL_GENLOCK_SOURCE_EXTERNAL_SYNC_I3D)
defines.add(WGL_GENLOCK_SOURCE_EXTERNAL_TTL_I3D)
defines.add(WGL_GENLOCK_SOURCE_MULTIVIEW_I3D)

# WGL_I3D_image_buffer

WGL_IMAGE_BUFFER_LOCK_I3D = Enumerant('WGL_IMAGE_BUFFER_LOCK_I3D', 2, 'WGL_I3D_image_buffer')
WGL_IMAGE_BUFFER_MIN_ACCESS_I3D = Enumerant('WGL_IMAGE_BUFFER_MIN_ACCESS_I3D', 1, 'WGL_I3D_image_buffer')

defines.add(WGL_IMAGE_BUFFER_LOCK_I3D)
defines.add(WGL_IMAGE_BUFFER_MIN_ACCESS_I3D)

# WGL_NV_float_buffer

WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV', 8372, 'WGL_NV_float_buffer')
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV', 8371, 'WGL_NV_float_buffer')
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV', 8370, 'WGL_NV_float_buffer')
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV', 8369, 'WGL_NV_float_buffer')
WGL_FLOAT_COMPONENTS_NV = Enumerant('WGL_FLOAT_COMPONENTS_NV', 8368, 'WGL_NV_float_buffer')
WGL_TEXTURE_FLOAT_RGBA_NV = Enumerant('WGL_TEXTURE_FLOAT_RGBA_NV', 8376, 'WGL_NV_float_buffer')
WGL_TEXTURE_FLOAT_RGB_NV = Enumerant('WGL_TEXTURE_FLOAT_RGB_NV', 8375, 'WGL_NV_float_buffer')
WGL_TEXTURE_FLOAT_RG_NV = Enumerant('WGL_TEXTURE_FLOAT_RG_NV', 8374, 'WGL_NV_float_buffer')
WGL_TEXTURE_FLOAT_R_NV = Enumerant('WGL_TEXTURE_FLOAT_R_NV', 8373, 'WGL_NV_float_buffer')

defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV)
defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV)
defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV)
defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV)
defines.add(WGL_FLOAT_COMPONENTS_NV)
defines.add(WGL_TEXTURE_FLOAT_RGBA_NV)
defines.add(WGL_TEXTURE_FLOAT_RGB_NV)
defines.add(WGL_TEXTURE_FLOAT_RG_NV)
defines.add(WGL_TEXTURE_FLOAT_R_NV)

# WGL_NV_gpu_affinity

WGL_ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV = Enumerant('WGL_ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV', 8400, 'WGL_NV_gpu_affinity')
WGL_ERROR_MISSING_AFFINITY_MASK_NV = Enumerant('WGL_ERROR_MISSING_AFFINITY_MASK_NV', 8401, 'WGL_NV_gpu_affinity')

defines.add(WGL_ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV)
defines.add(WGL_ERROR_MISSING_AFFINITY_MASK_NV)

# WGL_NV_present_video

WGL_NUM_VIDEO_SLOTS_NV = Enumerant('WGL_NUM_VIDEO_SLOTS_NV', 8432, 'WGL_NV_present_video')

defines.add(WGL_NUM_VIDEO_SLOTS_NV)

# WGL_NV_render_depth_texture

WGL_BIND_TO_TEXTURE_DEPTH_NV = Enumerant('WGL_BIND_TO_TEXTURE_DEPTH_NV', 8355, 'WGL_NV_render_depth_texture')
WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV', 8356, 'WGL_NV_render_depth_texture')
WGL_DEPTH_COMPONENT_NV = Enumerant('WGL_DEPTH_COMPONENT_NV', 8359, 'WGL_NV_render_depth_texture')
WGL_DEPTH_TEXTURE_FORMAT_NV = Enumerant('WGL_DEPTH_TEXTURE_FORMAT_NV', 8357, 'WGL_NV_render_depth_texture')
WGL_NO_TEXTURE_ARB = Enumerant('WGL_NO_TEXTURE_ARB', 8311, 'WGL_NV_render_depth_texture')
WGL_NO_TEXTURE_ARB = Enumerant('WGL_NO_TEXTURE_ARB', 8311, 'WGL_NV_render_depth_texture')
WGL_TEXTURE_DEPTH_COMPONENT_NV = Enumerant('WGL_TEXTURE_DEPTH_COMPONENT_NV', 8358, 'WGL_NV_render_depth_texture')

defines.add(WGL_BIND_TO_TEXTURE_DEPTH_NV)
defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV)
defines.add(WGL_DEPTH_COMPONENT_NV)
defines.add(WGL_DEPTH_TEXTURE_FORMAT_NV)
defines.add(WGL_NO_TEXTURE_ARB)
defines.add(WGL_NO_TEXTURE_ARB)
defines.add(WGL_TEXTURE_DEPTH_COMPONENT_NV)

# WGL_NV_render_texture_rectangle

WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV', 8353, 'WGL_NV_render_texture_rectangle')
WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV = Enumerant('WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV', 8352, 'WGL_NV_render_texture_rectangle')
WGL_TEXTURE_RECTANGLE_NV = Enumerant('WGL_TEXTURE_RECTANGLE_NV', 8354, 'WGL_NV_render_texture_rectangle')

defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV)
defines.add(WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV)
defines.add(WGL_TEXTURE_RECTANGLE_NV)

# WGL_NV_video_output

WGL_BIND_TO_VIDEO_RGBA_NV = Enumerant('WGL_BIND_TO_VIDEO_RGBA_NV', 8385, 'WGL_NV_video_output')
WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV = Enumerant('WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV', 8386, 'WGL_NV_video_output')
WGL_BIND_TO_VIDEO_RGB_NV = Enumerant('WGL_BIND_TO_VIDEO_RGB_NV', 8384, 'WGL_NV_video_output')
WGL_VIDEO_OUT_ALPHA_NV = Enumerant('WGL_VIDEO_OUT_ALPHA_NV', 8388, 'WGL_NV_video_output')
WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV = Enumerant('WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV', 8390, 'WGL_NV_video_output')
WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV = Enumerant('WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV', 8391, 'WGL_NV_video_output')
WGL_VIDEO_OUT_COLOR_NV = Enumerant('WGL_VIDEO_OUT_COLOR_NV', 8387, 'WGL_NV_video_output')
WGL_VIDEO_OUT_DEPTH_NV = Enumerant('WGL_VIDEO_OUT_DEPTH_NV', 8389, 'WGL_NV_video_output')
WGL_VIDEO_OUT_FIELD_1 = Enumerant('WGL_VIDEO_OUT_FIELD_1', 8393, 'WGL_NV_video_output')
WGL_VIDEO_OUT_FIELD_2 = Enumerant('WGL_VIDEO_OUT_FIELD_2', 8394, 'WGL_NV_video_output')
WGL_VIDEO_OUT_FRAME = Enumerant('WGL_VIDEO_OUT_FRAME', 8392, 'WGL_NV_video_output')
WGL_VIDEO_OUT_STACKED_FIELDS_1_2 = Enumerant('WGL_VIDEO_OUT_STACKED_FIELDS_1_2', 8395, 'WGL_NV_video_output')
WGL_VIDEO_OUT_STACKED_FIELDS_2_1 = Enumerant('WGL_VIDEO_OUT_STACKED_FIELDS_2_1', 8396, 'WGL_NV_video_output')

defines.add(WGL_BIND_TO_VIDEO_RGBA_NV)
defines.add(WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV)
defines.add(WGL_BIND_TO_VIDEO_RGB_NV)
defines.add(WGL_VIDEO_OUT_ALPHA_NV)
defines.add(WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV)
defines.add(WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV)
defines.add(WGL_VIDEO_OUT_COLOR_NV)
defines.add(WGL_VIDEO_OUT_DEPTH_NV)
defines.add(WGL_VIDEO_OUT_FIELD_1)
defines.add(WGL_VIDEO_OUT_FIELD_2)
defines.add(WGL_VIDEO_OUT_FRAME)
defines.add(WGL_VIDEO_OUT_STACKED_FIELDS_1_2)
defines.add(WGL_VIDEO_OUT_STACKED_FIELDS_2_1)

# WGL_3DL_stereo_control

wglSetStereoEmitterState3DL = Function('wglSetStereoEmitterState3DL')
wglSetStereoEmitterState3DL.ret = Return('BOOL')
wglSetStereoEmitterState3DL.add( Input( 'hDC','HDC' ))
wglSetStereoEmitterState3DL.add( Input( 'uState','UINT' ))
wglSetStereoEmitterState3DL.version = ''
wglSetStereoEmitterState3DL.category = 'WGL_3DL_stereo_control'
wglSetStereoEmitterState3DL.trace = True
wglSetStereoEmitterState3DL.play = True
wgl.add(wglSetStereoEmitterState3DL)

# WGL_AMD_gpu_association

wglBlitContextFramebufferAMD = Function('wglBlitContextFramebufferAMD')
wglBlitContextFramebufferAMD.ret = Return('VOID')
wglBlitContextFramebufferAMD.add( Input( 'dstCtx','HGLRC' ))
wglBlitContextFramebufferAMD.add( Input( 'srcX0','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'srcY0','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'srcX1','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'srcY1','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'dstX0','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'dstY0','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'dstX1','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'dstY1','GLint' ))
wglBlitContextFramebufferAMD.add( Input( 'mask','GLbitfield' ))
wglBlitContextFramebufferAMD.add( Input( 'filter','GLenum' ))
wglBlitContextFramebufferAMD.version = ''
wglBlitContextFramebufferAMD.category = 'WGL_AMD_gpu_association'
wglBlitContextFramebufferAMD.trace = True
wglBlitContextFramebufferAMD.play = True
wgl.add(wglBlitContextFramebufferAMD)

wglCreateAssociatedContextAMD = Function('wglCreateAssociatedContextAMD')
wglCreateAssociatedContextAMD.ret = Return('HGLRC')
wglCreateAssociatedContextAMD.add( Input( 'id','UINT' ))
wglCreateAssociatedContextAMD.version = ''
wglCreateAssociatedContextAMD.category = 'WGL_AMD_gpu_association'
wglCreateAssociatedContextAMD.trace = True
wglCreateAssociatedContextAMD.play = True
wgl.add(wglCreateAssociatedContextAMD)

wglCreateAssociatedContextAttribsAMD = Function('wglCreateAssociatedContextAttribsAMD')
wglCreateAssociatedContextAttribsAMD.ret = Return('HGLRC')
wglCreateAssociatedContextAttribsAMD.add( Input( 'id','UINT' ))
wglCreateAssociatedContextAttribsAMD.add( Input( 'hShareContext','HGLRC' ))
wglCreateAssociatedContextAttribsAMD.add( Input( 'attribList','const int *' ))
wglCreateAssociatedContextAttribsAMD.version = ''
wglCreateAssociatedContextAttribsAMD.category = 'WGL_AMD_gpu_association'
wglCreateAssociatedContextAttribsAMD.trace = True
wglCreateAssociatedContextAttribsAMD.play = True
wgl.add(wglCreateAssociatedContextAttribsAMD)

wglDeleteAssociatedContextAMD = Function('wglDeleteAssociatedContextAMD')
wglDeleteAssociatedContextAMD.ret = Return('BOOL')
wglDeleteAssociatedContextAMD.add( Input( 'hglrc','HGLRC' ))
wglDeleteAssociatedContextAMD.version = ''
wglDeleteAssociatedContextAMD.category = 'WGL_AMD_gpu_association'
wglDeleteAssociatedContextAMD.trace = True
wglDeleteAssociatedContextAMD.play = True
wgl.add(wglDeleteAssociatedContextAMD)

wglGetContextGPUIDAMD = Function('wglGetContextGPUIDAMD')
wglGetContextGPUIDAMD.ret = Return('UINT')
wglGetContextGPUIDAMD.add( Input( 'hglrc','HGLRC' ))
wglGetContextGPUIDAMD.version = ''
wglGetContextGPUIDAMD.category = 'WGL_AMD_gpu_association'
wglGetContextGPUIDAMD.trace = True
wglGetContextGPUIDAMD.play = True
wgl.add(wglGetContextGPUIDAMD)

wglGetCurrentAssociatedContextAMD = Function('wglGetCurrentAssociatedContextAMD')
wglGetCurrentAssociatedContextAMD.ret = Return('HGLRC')
wglGetCurrentAssociatedContextAMD.version = ''
wglGetCurrentAssociatedContextAMD.category = 'WGL_AMD_gpu_association'
wglGetCurrentAssociatedContextAMD.trace = True
wglGetCurrentAssociatedContextAMD.play = True
wgl.add(wglGetCurrentAssociatedContextAMD)

wglGetGPUIDsAMD = Function('wglGetGPUIDsAMD')
wglGetGPUIDsAMD.ret = Return('UINT')
wglGetGPUIDsAMD.add( Input( 'maxCount','UINT' ))
wglGetGPUIDsAMD.add( Output( 'ids','UINT *' ,size = 'maxCount' ))
wglGetGPUIDsAMD.version = ''
wglGetGPUIDsAMD.category = 'WGL_AMD_gpu_association'
wglGetGPUIDsAMD.trace = True
wglGetGPUIDsAMD.play = True
wgl.add(wglGetGPUIDsAMD)

wglGetGPUInfoAMD = Function('wglGetGPUInfoAMD')
wglGetGPUInfoAMD.ret = Return('INT')
wglGetGPUInfoAMD.add( Input( 'id','UINT' ))
wglGetGPUInfoAMD.add( Input( 'property','int' ))
wglGetGPUInfoAMD.add( Input( 'dataType','GLenum' ))
wglGetGPUInfoAMD.add( Input( 'size','UINT' ))
wglGetGPUInfoAMD.add( Output( 'data','void *' ))
wglGetGPUInfoAMD.version = ''
wglGetGPUInfoAMD.category = 'WGL_AMD_gpu_association'
wglGetGPUInfoAMD.trace = True
wglGetGPUInfoAMD.play = True
wgl.add(wglGetGPUInfoAMD)

wglMakeAssociatedContextCurrentAMD = Function('wglMakeAssociatedContextCurrentAMD')
wglMakeAssociatedContextCurrentAMD.ret = Return('BOOL')
wglMakeAssociatedContextCurrentAMD.add( Input( 'hglrc','HGLRC' ))
wglMakeAssociatedContextCurrentAMD.version = ''
wglMakeAssociatedContextCurrentAMD.category = 'WGL_AMD_gpu_association'
wglMakeAssociatedContextCurrentAMD.trace = True
wglMakeAssociatedContextCurrentAMD.play = True
wgl.add(wglMakeAssociatedContextCurrentAMD)

# WGL_ARB_buffer_region

wglCreateBufferRegionARB = Function('wglCreateBufferRegionARB')
wglCreateBufferRegionARB.ret = Return('HANDLE')
wglCreateBufferRegionARB.add( Input( 'hDC','HDC' ))
wglCreateBufferRegionARB.add( Input( 'iLayerPlane','int' ))
wglCreateBufferRegionARB.add( Input( 'uType','UINT' ))
wglCreateBufferRegionARB.version = ''
wglCreateBufferRegionARB.category = 'WGL_ARB_buffer_region'
wglCreateBufferRegionARB.trace = True
wglCreateBufferRegionARB.play = True
wgl.add(wglCreateBufferRegionARB)

wglDeleteBufferRegionARB = Function('wglDeleteBufferRegionARB')
wglDeleteBufferRegionARB.ret = Return('VOID')
wglDeleteBufferRegionARB.add( Input( 'hRegion','HANDLE' ))
wglDeleteBufferRegionARB.version = ''
wglDeleteBufferRegionARB.category = 'WGL_ARB_buffer_region'
wglDeleteBufferRegionARB.trace = True
wglDeleteBufferRegionARB.play = True
wgl.add(wglDeleteBufferRegionARB)

wglRestoreBufferRegionARB = Function('wglRestoreBufferRegionARB')
wglRestoreBufferRegionARB.ret = Return('BOOL')
wglRestoreBufferRegionARB.add( Input( 'hRegion','HANDLE' ))
wglRestoreBufferRegionARB.add( Input( 'x','int' ))
wglRestoreBufferRegionARB.add( Input( 'y','int' ))
wglRestoreBufferRegionARB.add( Input( 'width','int' ))
wglRestoreBufferRegionARB.add( Input( 'height','int' ))
wglRestoreBufferRegionARB.add( Input( 'xSrc','int' ))
wglRestoreBufferRegionARB.add( Input( 'ySrc','int' ))
wglRestoreBufferRegionARB.version = ''
wglRestoreBufferRegionARB.category = 'WGL_ARB_buffer_region'
wglRestoreBufferRegionARB.trace = True
wglRestoreBufferRegionARB.play = True
wgl.add(wglRestoreBufferRegionARB)

wglSaveBufferRegionARB = Function('wglSaveBufferRegionARB')
wglSaveBufferRegionARB.ret = Return('BOOL')
wglSaveBufferRegionARB.add( Input( 'hRegion','HANDLE' ))
wglSaveBufferRegionARB.add( Input( 'x','int' ))
wglSaveBufferRegionARB.add( Input( 'y','int' ))
wglSaveBufferRegionARB.add( Input( 'width','int' ))
wglSaveBufferRegionARB.add( Input( 'height','int' ))
wglSaveBufferRegionARB.version = ''
wglSaveBufferRegionARB.category = 'WGL_ARB_buffer_region'
wglSaveBufferRegionARB.trace = True
wglSaveBufferRegionARB.play = True
wgl.add(wglSaveBufferRegionARB)

# WGL_ARB_create_context

wglCreateContextAttribsARB = Function('wglCreateContextAttribsARB')
wglCreateContextAttribsARB.ret = Return('HGLRC')
wglCreateContextAttribsARB.add( Input( 'hDC','HDC' ))
wglCreateContextAttribsARB.add( Input( 'hShareContext','HGLRC' ))
wglCreateContextAttribsARB.add( Input( 'piAttribList','const int *' ))
wglCreateContextAttribsARB.version = ''
wglCreateContextAttribsARB.category = 'WGL_ARB_create_context'
wglCreateContextAttribsARB.trace = True
wglCreateContextAttribsARB.play = True
wgl.add(wglCreateContextAttribsARB)

# WGL_ARB_extensions_string

wglGetExtensionsStringARB = Function('wglGetExtensionsStringARB')
wglGetExtensionsStringARB.ret = Return('const char *')
wglGetExtensionsStringARB.add( Input( 'hDC','HDC' ))
wglGetExtensionsStringARB.version = ''
wglGetExtensionsStringARB.category = 'WGL_ARB_extensions_string'
wglGetExtensionsStringARB.trace = True
wglGetExtensionsStringARB.play = True
wgl.add(wglGetExtensionsStringARB)

# WGL_ARB_make_current_read

wglGetCurrentReadDCARB = Function('wglGetCurrentReadDCARB')
wglGetCurrentReadDCARB.ret = Return('HDC')
wglGetCurrentReadDCARB.version = ''
wglGetCurrentReadDCARB.category = 'WGL_ARB_make_current_read'
wglGetCurrentReadDCARB.trace = True
wglGetCurrentReadDCARB.play = True
wgl.add(wglGetCurrentReadDCARB)

wglMakeContextCurrentARB = Function('wglMakeContextCurrentARB')
wglMakeContextCurrentARB.ret = Return('BOOL')
wglMakeContextCurrentARB.add( Input( 'hDrawDC','HDC' ))
wglMakeContextCurrentARB.add( Input( 'hReadDC','HDC' ))
wglMakeContextCurrentARB.add( Input( 'hglrc','HGLRC' ))
wglMakeContextCurrentARB.version = ''
wglMakeContextCurrentARB.category = 'WGL_ARB_make_current_read'
wglMakeContextCurrentARB.trace = True
wglMakeContextCurrentARB.play = True
wgl.add(wglMakeContextCurrentARB)

# WGL_ARB_pbuffer

wglCreatePbufferARB = Function('wglCreatePbufferARB')
wglCreatePbufferARB.ret = Return('HPBUFFERARB')
wglCreatePbufferARB.add( Input( 'hDC','HDC' ))
wglCreatePbufferARB.add( Input( 'iPixelFormat','int' ))
wglCreatePbufferARB.add( Input( 'iWidth','int' ))
wglCreatePbufferARB.add( Input( 'iHeight','int' ))
wglCreatePbufferARB.add( Input( 'piAttribList','const int *' ))
wglCreatePbufferARB.version = ''
wglCreatePbufferARB.category = 'WGL_ARB_pbuffer'
wglCreatePbufferARB.trace = True
wglCreatePbufferARB.play = True
wgl.add(wglCreatePbufferARB)

wglDestroyPbufferARB = Function('wglDestroyPbufferARB')
wglDestroyPbufferARB.ret = Return('BOOL')
wglDestroyPbufferARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglDestroyPbufferARB.version = ''
wglDestroyPbufferARB.category = 'WGL_ARB_pbuffer'
wglDestroyPbufferARB.trace = True
wglDestroyPbufferARB.play = True
wgl.add(wglDestroyPbufferARB)

wglGetPbufferDCARB = Function('wglGetPbufferDCARB')
wglGetPbufferDCARB.ret = Return('HDC')
wglGetPbufferDCARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglGetPbufferDCARB.version = ''
wglGetPbufferDCARB.category = 'WGL_ARB_pbuffer'
wglGetPbufferDCARB.trace = True
wglGetPbufferDCARB.play = True
wgl.add(wglGetPbufferDCARB)

wglQueryPbufferARB = Function('wglQueryPbufferARB')
wglQueryPbufferARB.ret = Return('BOOL')
wglQueryPbufferARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglQueryPbufferARB.add( Input( 'iAttribute','int' ))
wglQueryPbufferARB.add( Output( 'piValue','int *' ,size = 1 ))
wglQueryPbufferARB.version = ''
wglQueryPbufferARB.category = 'WGL_ARB_pbuffer'
wglQueryPbufferARB.trace = True
wglQueryPbufferARB.play = True
wgl.add(wglQueryPbufferARB)

wglReleasePbufferDCARB = Function('wglReleasePbufferDCARB')
wglReleasePbufferDCARB.ret = Return('int')
wglReleasePbufferDCARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglReleasePbufferDCARB.add( Input( 'hDC','HDC' ))
wglReleasePbufferDCARB.version = ''
wglReleasePbufferDCARB.category = 'WGL_ARB_pbuffer'
wglReleasePbufferDCARB.trace = True
wglReleasePbufferDCARB.play = True
wgl.add(wglReleasePbufferDCARB)

# WGL_ARB_pixel_format

wglChoosePixelFormatARB = Function('wglChoosePixelFormatARB')
wglChoosePixelFormatARB.ret = Return('BOOL')
wglChoosePixelFormatARB.add( Input( 'hDC','HDC' ))
wglChoosePixelFormatARB.add( Input( 'piAttribIList','const int *' ))
wglChoosePixelFormatARB.add( Input( 'pfAttribFList','const FLOAT *' ))
wglChoosePixelFormatARB.add( Input( 'nMaxFormats','UINT' ))
wglChoosePixelFormatARB.add( Output( 'piFormats','int *' ))
wglChoosePixelFormatARB.add( Output( 'nNumFormats','UINT *' ,size = 1 ))
wglChoosePixelFormatARB.version = ''
wglChoosePixelFormatARB.category = 'WGL_ARB_pixel_format'
wglChoosePixelFormatARB.trace = True
wglChoosePixelFormatARB.play = True
wgl.add(wglChoosePixelFormatARB)

wglGetPixelFormatAttribfvARB = Function('wglGetPixelFormatAttribfvARB')
wglGetPixelFormatAttribfvARB.ret = Return('BOOL')
wglGetPixelFormatAttribfvARB.add( Input( 'hDC','HDC' ))
wglGetPixelFormatAttribfvARB.add( Input( 'iPixelFormat','int' ))
wglGetPixelFormatAttribfvARB.add( Input( 'iLayerPlane','int' ))
wglGetPixelFormatAttribfvARB.add( Input( 'nAttributes','UINT' ))
wglGetPixelFormatAttribfvARB.add( Input( 'piAttributes','const int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribfvARB.add( Output( 'pfValues','FLOAT *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribfvARB.version = ''
wglGetPixelFormatAttribfvARB.category = 'WGL_ARB_pixel_format'
wglGetPixelFormatAttribfvARB.trace = True
wglGetPixelFormatAttribfvARB.play = True
wgl.add(wglGetPixelFormatAttribfvARB)

wglGetPixelFormatAttribivARB = Function('wglGetPixelFormatAttribivARB')
wglGetPixelFormatAttribivARB.ret = Return('BOOL')
wglGetPixelFormatAttribivARB.add( Input( 'hDC','HDC' ))
wglGetPixelFormatAttribivARB.add( Input( 'iPixelFormat','int' ))
wglGetPixelFormatAttribivARB.add( Input( 'iLayerPlane','int' ))
wglGetPixelFormatAttribivARB.add( Input( 'nAttributes','UINT' ))
wglGetPixelFormatAttribivARB.add( Input( 'piAttributes','const int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribivARB.add( Output( 'piValues','int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribivARB.version = ''
wglGetPixelFormatAttribivARB.category = 'WGL_ARB_pixel_format'
wglGetPixelFormatAttribivARB.trace = True
wglGetPixelFormatAttribivARB.play = True
wgl.add(wglGetPixelFormatAttribivARB)

# WGL_ARB_render_texture

wglBindTexImageARB = Function('wglBindTexImageARB')
wglBindTexImageARB.ret = Return('BOOL')
wglBindTexImageARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglBindTexImageARB.add( Input( 'iBuffer','int' ))
wglBindTexImageARB.version = ''
wglBindTexImageARB.category = 'WGL_ARB_render_texture'
wglBindTexImageARB.trace = True
wglBindTexImageARB.play = True
wgl.add(wglBindTexImageARB)

wglReleaseTexImageARB = Function('wglReleaseTexImageARB')
wglReleaseTexImageARB.ret = Return('BOOL')
wglReleaseTexImageARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglReleaseTexImageARB.add( Input( 'iBuffer','int' ))
wglReleaseTexImageARB.version = ''
wglReleaseTexImageARB.category = 'WGL_ARB_render_texture'
wglReleaseTexImageARB.trace = True
wglReleaseTexImageARB.play = True
wgl.add(wglReleaseTexImageARB)

wglSetPbufferAttribARB = Function('wglSetPbufferAttribARB')
wglSetPbufferAttribARB.ret = Return('BOOL')
wglSetPbufferAttribARB.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglSetPbufferAttribARB.add( Input( 'piAttribList','const int *' ))
wglSetPbufferAttribARB.version = ''
wglSetPbufferAttribARB.category = 'WGL_ARB_render_texture'
wglSetPbufferAttribARB.trace = True
wglSetPbufferAttribARB.play = True
wgl.add(wglSetPbufferAttribARB)

# WGL_EXT_display_color_table

wglBindDisplayColorTableEXT = Function('wglBindDisplayColorTableEXT')
wglBindDisplayColorTableEXT.ret = Return('GLboolean')
wglBindDisplayColorTableEXT.add( Input( 'id','GLushort' ))
wglBindDisplayColorTableEXT.version = ''
wglBindDisplayColorTableEXT.category = 'WGL_EXT_display_color_table'
wglBindDisplayColorTableEXT.trace = True
wglBindDisplayColorTableEXT.play = True
wgl.add(wglBindDisplayColorTableEXT)

wglCreateDisplayColorTableEXT = Function('wglCreateDisplayColorTableEXT')
wglCreateDisplayColorTableEXT.ret = Return('GLboolean')
wglCreateDisplayColorTableEXT.add( Input( 'id','GLushort' ))
wglCreateDisplayColorTableEXT.version = ''
wglCreateDisplayColorTableEXT.category = 'WGL_EXT_display_color_table'
wglCreateDisplayColorTableEXT.trace = True
wglCreateDisplayColorTableEXT.play = True
wgl.add(wglCreateDisplayColorTableEXT)

wglDestroyDisplayColorTableEXT = Function('wglDestroyDisplayColorTableEXT')
wglDestroyDisplayColorTableEXT.ret = Return('VOID')
wglDestroyDisplayColorTableEXT.add( Input( 'id','GLushort' ))
wglDestroyDisplayColorTableEXT.version = ''
wglDestroyDisplayColorTableEXT.category = 'WGL_EXT_display_color_table'
wglDestroyDisplayColorTableEXT.trace = True
wglDestroyDisplayColorTableEXT.play = True
wgl.add(wglDestroyDisplayColorTableEXT)

wglLoadDisplayColorTableEXT = Function('wglLoadDisplayColorTableEXT')
wglLoadDisplayColorTableEXT.ret = Return('GLboolean')
wglLoadDisplayColorTableEXT.add( Input( 'table','const GLushort *' ,size = 'length' ))
wglLoadDisplayColorTableEXT.add( Input( 'length','GLuint' ))
wglLoadDisplayColorTableEXT.version = ''
wglLoadDisplayColorTableEXT.category = 'WGL_EXT_display_color_table'
wglLoadDisplayColorTableEXT.trace = True
wglLoadDisplayColorTableEXT.play = True
wgl.add(wglLoadDisplayColorTableEXT)

# WGL_EXT_extensions_string

wglGetExtensionsStringEXT = Function('wglGetExtensionsStringEXT')
wglGetExtensionsStringEXT.ret = Return('const char *')
wglGetExtensionsStringEXT.version = ''
wglGetExtensionsStringEXT.category = 'WGL_EXT_extensions_string'
wglGetExtensionsStringEXT.trace = True
wglGetExtensionsStringEXT.play = True
wgl.add(wglGetExtensionsStringEXT)

# WGL_EXT_make_current_read

wglGetCurrentReadDCEXT = Function('wglGetCurrentReadDCEXT')
wglGetCurrentReadDCEXT.ret = Return('HDC')
wglGetCurrentReadDCEXT.version = ''
wglGetCurrentReadDCEXT.category = 'WGL_EXT_make_current_read'
wglGetCurrentReadDCEXT.trace = True
wglGetCurrentReadDCEXT.play = True
wgl.add(wglGetCurrentReadDCEXT)

wglMakeContextCurrentEXT = Function('wglMakeContextCurrentEXT')
wglMakeContextCurrentEXT.ret = Return('BOOL')
wglMakeContextCurrentEXT.add( Input( 'hDrawDC','HDC' ))
wglMakeContextCurrentEXT.add( Input( 'hReadDC','HDC' ))
wglMakeContextCurrentEXT.add( Input( 'hglrc','HGLRC' ))
wglMakeContextCurrentEXT.version = ''
wglMakeContextCurrentEXT.category = 'WGL_EXT_make_current_read'
wglMakeContextCurrentEXT.trace = True
wglMakeContextCurrentEXT.play = True
wgl.add(wglMakeContextCurrentEXT)

# WGL_EXT_pbuffer

wglCreatePbufferEXT = Function('wglCreatePbufferEXT')
wglCreatePbufferEXT.ret = Return('HPBUFFEREXT')
wglCreatePbufferEXT.add( Input( 'hDC','HDC' ))
wglCreatePbufferEXT.add( Input( 'iPixelFormat','int' ))
wglCreatePbufferEXT.add( Input( 'iWidth','int' ))
wglCreatePbufferEXT.add( Input( 'iHeight','int' ))
wglCreatePbufferEXT.add( Input( 'piAttribList','const int *' ))
wglCreatePbufferEXT.version = ''
wglCreatePbufferEXT.category = 'WGL_EXT_pbuffer'
wglCreatePbufferEXT.trace = True
wglCreatePbufferEXT.play = True
wgl.add(wglCreatePbufferEXT)

wglDestroyPbufferEXT = Function('wglDestroyPbufferEXT')
wglDestroyPbufferEXT.ret = Return('BOOL')
wglDestroyPbufferEXT.add( Input( 'hPbuffer','HPBUFFEREXT' ))
wglDestroyPbufferEXT.version = ''
wglDestroyPbufferEXT.category = 'WGL_EXT_pbuffer'
wglDestroyPbufferEXT.trace = True
wglDestroyPbufferEXT.play = True
wgl.add(wglDestroyPbufferEXT)

wglGetPbufferDCEXT = Function('wglGetPbufferDCEXT')
wglGetPbufferDCEXT.ret = Return('HDC')
wglGetPbufferDCEXT.add( Input( 'hPbuffer','HPBUFFEREXT' ))
wglGetPbufferDCEXT.version = ''
wglGetPbufferDCEXT.category = 'WGL_EXT_pbuffer'
wglGetPbufferDCEXT.trace = True
wglGetPbufferDCEXT.play = True
wgl.add(wglGetPbufferDCEXT)

wglQueryPbufferEXT = Function('wglQueryPbufferEXT')
wglQueryPbufferEXT.ret = Return('BOOL')
wglQueryPbufferEXT.add( Input( 'hPbuffer','HPBUFFEREXT' ))
wglQueryPbufferEXT.add( Input( 'iAttribute','int' ))
wglQueryPbufferEXT.add( Output( 'piValue','int *' ,size = 1 ))
wglQueryPbufferEXT.version = ''
wglQueryPbufferEXT.category = 'WGL_EXT_pbuffer'
wglQueryPbufferEXT.trace = True
wglQueryPbufferEXT.play = True
wgl.add(wglQueryPbufferEXT)

wglReleasePbufferDCEXT = Function('wglReleasePbufferDCEXT')
wglReleasePbufferDCEXT.ret = Return('int')
wglReleasePbufferDCEXT.add( Input( 'hPbuffer','HPBUFFEREXT' ))
wglReleasePbufferDCEXT.add( Input( 'hDC','HDC' ))
wglReleasePbufferDCEXT.version = ''
wglReleasePbufferDCEXT.category = 'WGL_EXT_pbuffer'
wglReleasePbufferDCEXT.trace = True
wglReleasePbufferDCEXT.play = True
wgl.add(wglReleasePbufferDCEXT)

# WGL_EXT_pixel_format

wglChoosePixelFormatEXT = Function('wglChoosePixelFormatEXT')
wglChoosePixelFormatEXT.ret = Return('BOOL')
wglChoosePixelFormatEXT.add( Input( 'hDC','HDC' ))
wglChoosePixelFormatEXT.add( Input( 'piAttribIList','const int *' ))
wglChoosePixelFormatEXT.add( Input( 'pfAttribFList','const FLOAT *' ))
wglChoosePixelFormatEXT.add( Input( 'nMaxFormats','UINT' ))
wglChoosePixelFormatEXT.add( Output( 'piFormats','int *' ))
wglChoosePixelFormatEXT.add( Output( 'nNumFormats','UINT *' ,size = 1 ))
wglChoosePixelFormatEXT.version = ''
wglChoosePixelFormatEXT.category = 'WGL_EXT_pixel_format'
wglChoosePixelFormatEXT.trace = True
wglChoosePixelFormatEXT.play = True
wgl.add(wglChoosePixelFormatEXT)

wglGetPixelFormatAttribfvEXT = Function('wglGetPixelFormatAttribfvEXT')
wglGetPixelFormatAttribfvEXT.ret = Return('BOOL')
wglGetPixelFormatAttribfvEXT.add( Input( 'hDC','HDC' ))
wglGetPixelFormatAttribfvEXT.add( Input( 'iPixelFormat','int' ))
wglGetPixelFormatAttribfvEXT.add( Input( 'iLayerPlane','int' ))
wglGetPixelFormatAttribfvEXT.add( Input( 'nAttributes','UINT' ))
wglGetPixelFormatAttribfvEXT.add( Input( 'piAttributes','const int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribfvEXT.add( Output( 'pfValues','FLOAT *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribfvEXT.version = ''
wglGetPixelFormatAttribfvEXT.category = 'WGL_EXT_pixel_format'
wglGetPixelFormatAttribfvEXT.trace = True
wglGetPixelFormatAttribfvEXT.play = True
wgl.add(wglGetPixelFormatAttribfvEXT)

wglGetPixelFormatAttribivEXT = Function('wglGetPixelFormatAttribivEXT')
wglGetPixelFormatAttribivEXT.ret = Return('BOOL')
wglGetPixelFormatAttribivEXT.add( Input( 'hDC','HDC' ))
wglGetPixelFormatAttribivEXT.add( Input( 'iPixelFormat','int' ))
wglGetPixelFormatAttribivEXT.add( Input( 'iLayerPlane','int' ))
wglGetPixelFormatAttribivEXT.add( Input( 'nAttributes','UINT' ))
wglGetPixelFormatAttribivEXT.add( Input( 'piAttributes','const int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribivEXT.add( Output( 'piValues','int *' ,size = 'nAttributes' ))
wglGetPixelFormatAttribivEXT.version = ''
wglGetPixelFormatAttribivEXT.category = 'WGL_EXT_pixel_format'
wglGetPixelFormatAttribivEXT.trace = True
wglGetPixelFormatAttribivEXT.play = True
wgl.add(wglGetPixelFormatAttribivEXT)

# WGL_EXT_swap_control

wglGetSwapIntervalEXT = Function('wglGetSwapIntervalEXT')
wglGetSwapIntervalEXT.ret = Return('int')
wglGetSwapIntervalEXT.version = ''
wglGetSwapIntervalEXT.category = 'WGL_EXT_swap_control'
wglGetSwapIntervalEXT.trace = True
wglGetSwapIntervalEXT.play = True
wgl.add(wglGetSwapIntervalEXT)

wglSwapIntervalEXT = Function('wglSwapIntervalEXT')
wglSwapIntervalEXT.ret = Return('BOOL')
wglSwapIntervalEXT.add( Input( 'interval','int' ))
wglSwapIntervalEXT.version = ''
wglSwapIntervalEXT.category = 'WGL_EXT_swap_control'
wglSwapIntervalEXT.trace = True
wglSwapIntervalEXT.play = True
wgl.add(wglSwapIntervalEXT)

# WGL_GDI

wglChoosePixelFormat = Function('wglChoosePixelFormat')
wglChoosePixelFormat.ret = Return('int')
wglChoosePixelFormat.add( Input( 'hDC','HDC' ))
wglChoosePixelFormat.add( Input( 'ppfd','const PIXELFORMATDESCRIPTOR *' ,size = 1 ))
wglChoosePixelFormat.version = ''
wglChoosePixelFormat.category = 'WGL_GDI'
wglChoosePixelFormat.trace = True
wglChoosePixelFormat.play = True
wgl.add(wglChoosePixelFormat)

wglDescribePixelFormat = Function('wglDescribePixelFormat')
wglDescribePixelFormat.ret = Return('int')
wglDescribePixelFormat.add( Input( 'hDC','HDC' ))
wglDescribePixelFormat.add( Input( 'iPixelFormat','int' ))
wglDescribePixelFormat.add( Input( 'nBytes','UINT' ))
wglDescribePixelFormat.add( Output( 'ppfd','LPPIXELFORMATDESCRIPTOR' ,size = 1 ))
wglDescribePixelFormat.version = ''
wglDescribePixelFormat.category = 'WGL_GDI'
wglDescribePixelFormat.trace = True
wglDescribePixelFormat.play = True
wgl.add(wglDescribePixelFormat)

wglGetPixelFormat = Function('wglGetPixelFormat')
wglGetPixelFormat.ret = Return('int')
wglGetPixelFormat.add( Input( 'hDC','HDC' ))
wglGetPixelFormat.version = ''
wglGetPixelFormat.category = 'WGL_GDI'
wglGetPixelFormat.trace = True
wglGetPixelFormat.play = True
wgl.add(wglGetPixelFormat)

wglSetPixelFormat = Function('wglSetPixelFormat')
wglSetPixelFormat.ret = Return('BOOL')
wglSetPixelFormat.add( Input( 'hDC','HDC' ))
wglSetPixelFormat.add( Input( 'iPixelFormat','int' ))
wglSetPixelFormat.add( Input( 'ppfd','const PIXELFORMATDESCRIPTOR *' ,size = 1 ))
wglSetPixelFormat.version = ''
wglSetPixelFormat.category = 'WGL_GDI'
wglSetPixelFormat.trace = True
wglSetPixelFormat.play = True
wgl.add(wglSetPixelFormat)

wglSwapBuffers = Function('wglSwapBuffers')
wglSwapBuffers.ret = Return('BOOL')
wglSwapBuffers.add( Input( 'hDC','HDC' ))
wglSwapBuffers.version = ''
wglSwapBuffers.category = 'WGL_GDI'
wglSwapBuffers.trace = True
wglSwapBuffers.play = True
wgl.add(wglSwapBuffers)

# WGL_I3D_digital_video_control

wglGetDigitalVideoParametersI3D = Function('wglGetDigitalVideoParametersI3D')
wglGetDigitalVideoParametersI3D.ret = Return('BOOL')
wglGetDigitalVideoParametersI3D.add( Input( 'hDC','HDC' ))
wglGetDigitalVideoParametersI3D.add( Input( 'iAttribute','int' ))
wglGetDigitalVideoParametersI3D.add( Output( 'piValue','int *' ))
wglGetDigitalVideoParametersI3D.version = ''
wglGetDigitalVideoParametersI3D.category = 'WGL_I3D_digital_video_control'
wglGetDigitalVideoParametersI3D.trace = True
wglGetDigitalVideoParametersI3D.play = True
wgl.add(wglGetDigitalVideoParametersI3D)

wglSetDigitalVideoParametersI3D = Function('wglSetDigitalVideoParametersI3D')
wglSetDigitalVideoParametersI3D.ret = Return('BOOL')
wglSetDigitalVideoParametersI3D.add( Input( 'hDC','HDC' ))
wglSetDigitalVideoParametersI3D.add( Input( 'iAttribute','int' ))
wglSetDigitalVideoParametersI3D.add( Input( 'piValue','const int *' ))
wglSetDigitalVideoParametersI3D.version = ''
wglSetDigitalVideoParametersI3D.category = 'WGL_I3D_digital_video_control'
wglSetDigitalVideoParametersI3D.trace = True
wglSetDigitalVideoParametersI3D.play = True
wgl.add(wglSetDigitalVideoParametersI3D)

# WGL_I3D_gamma

wglGetGammaTableI3D = Function('wglGetGammaTableI3D')
wglGetGammaTableI3D.ret = Return('BOOL')
wglGetGammaTableI3D.add( Input( 'hDC','HDC' ))
wglGetGammaTableI3D.add( Output( 'iEntries','int' ))
wglGetGammaTableI3D.add( Output( 'puRed','USHORT *' ,size = 'iEntries' ))
wglGetGammaTableI3D.add( Output( 'puGreen','USHORT *' ,size = 'iEntries' ))
wglGetGammaTableI3D.add( Output( 'puBlue','USHORT *' ,size = 'iEntries' ))
wglGetGammaTableI3D.version = ''
wglGetGammaTableI3D.category = 'WGL_I3D_gamma'
wglGetGammaTableI3D.trace = True
wglGetGammaTableI3D.play = True
wgl.add(wglGetGammaTableI3D)

wglGetGammaTableParametersI3D = Function('wglGetGammaTableParametersI3D')
wglGetGammaTableParametersI3D.ret = Return('BOOL')
wglGetGammaTableParametersI3D.add( Input( 'hDC','HDC' ))
wglGetGammaTableParametersI3D.add( Input( 'iAttribute','int' ))
wglGetGammaTableParametersI3D.add( Output( 'piValue','int *' ))
wglGetGammaTableParametersI3D.version = ''
wglGetGammaTableParametersI3D.category = 'WGL_I3D_gamma'
wglGetGammaTableParametersI3D.trace = True
wglGetGammaTableParametersI3D.play = True
wgl.add(wglGetGammaTableParametersI3D)

wglSetGammaTableI3D = Function('wglSetGammaTableI3D')
wglSetGammaTableI3D.ret = Return('BOOL')
wglSetGammaTableI3D.add( Input( 'hDC','HDC' ))
wglSetGammaTableI3D.add( Input( 'iEntries','int' ))
wglSetGammaTableI3D.add( Input( 'puRed','const USHORT *' ,size = 'iEntries' ))
wglSetGammaTableI3D.add( Input( 'puGreen','const USHORT *' ,size = 'iEntries' ))
wglSetGammaTableI3D.add( Input( 'puBlue','const USHORT *' ,size = 'iEntries' ))
wglSetGammaTableI3D.version = ''
wglSetGammaTableI3D.category = 'WGL_I3D_gamma'
wglSetGammaTableI3D.trace = True
wglSetGammaTableI3D.play = True
wgl.add(wglSetGammaTableI3D)

wglSetGammaTableParametersI3D = Function('wglSetGammaTableParametersI3D')
wglSetGammaTableParametersI3D.ret = Return('BOOL')
wglSetGammaTableParametersI3D.add( Input( 'hDC','HDC' ))
wglSetGammaTableParametersI3D.add( Input( 'iAttribute','int' ))
wglSetGammaTableParametersI3D.add( Input( 'piValue','const int *' ))
wglSetGammaTableParametersI3D.version = ''
wglSetGammaTableParametersI3D.category = 'WGL_I3D_gamma'
wglSetGammaTableParametersI3D.trace = True
wglSetGammaTableParametersI3D.play = True
wgl.add(wglSetGammaTableParametersI3D)

# WGL_I3D_genlock

wglDisableGenlockI3D = Function('wglDisableGenlockI3D')
wglDisableGenlockI3D.ret = Return('BOOL')
wglDisableGenlockI3D.add( Input( 'hDC','HDC' ))
wglDisableGenlockI3D.version = ''
wglDisableGenlockI3D.category = 'WGL_I3D_genlock'
wglDisableGenlockI3D.trace = True
wglDisableGenlockI3D.play = True
wgl.add(wglDisableGenlockI3D)

wglEnableGenlockI3D = Function('wglEnableGenlockI3D')
wglEnableGenlockI3D.ret = Return('BOOL')
wglEnableGenlockI3D.add( Input( 'hDC','HDC' ))
wglEnableGenlockI3D.version = ''
wglEnableGenlockI3D.category = 'WGL_I3D_genlock'
wglEnableGenlockI3D.trace = True
wglEnableGenlockI3D.play = True
wgl.add(wglEnableGenlockI3D)

wglGenlockSampleRateI3D = Function('wglGenlockSampleRateI3D')
wglGenlockSampleRateI3D.ret = Return('BOOL')
wglGenlockSampleRateI3D.add( Input( 'hDC','HDC' ))
wglGenlockSampleRateI3D.add( Input( 'uRate','UINT' ))
wglGenlockSampleRateI3D.version = ''
wglGenlockSampleRateI3D.category = 'WGL_I3D_genlock'
wglGenlockSampleRateI3D.trace = True
wglGenlockSampleRateI3D.play = True
wgl.add(wglGenlockSampleRateI3D)

wglGenlockSourceDelayI3D = Function('wglGenlockSourceDelayI3D')
wglGenlockSourceDelayI3D.ret = Return('BOOL')
wglGenlockSourceDelayI3D.add( Input( 'hDC','HDC' ))
wglGenlockSourceDelayI3D.add( Input( 'uDelay','UINT' ))
wglGenlockSourceDelayI3D.version = ''
wglGenlockSourceDelayI3D.category = 'WGL_I3D_genlock'
wglGenlockSourceDelayI3D.trace = True
wglGenlockSourceDelayI3D.play = True
wgl.add(wglGenlockSourceDelayI3D)

wglGenlockSourceEdgeI3D = Function('wglGenlockSourceEdgeI3D')
wglGenlockSourceEdgeI3D.ret = Return('BOOL')
wglGenlockSourceEdgeI3D.add( Input( 'hDC','HDC' ))
wglGenlockSourceEdgeI3D.add( Input( 'uEdge','UINT' ))
wglGenlockSourceEdgeI3D.version = ''
wglGenlockSourceEdgeI3D.category = 'WGL_I3D_genlock'
wglGenlockSourceEdgeI3D.trace = True
wglGenlockSourceEdgeI3D.play = True
wgl.add(wglGenlockSourceEdgeI3D)

wglGenlockSourceI3D = Function('wglGenlockSourceI3D')
wglGenlockSourceI3D.ret = Return('BOOL')
wglGenlockSourceI3D.add( Input( 'hDC','HDC' ))
wglGenlockSourceI3D.add( Input( 'uSource','UINT' ))
wglGenlockSourceI3D.version = ''
wglGenlockSourceI3D.category = 'WGL_I3D_genlock'
wglGenlockSourceI3D.trace = True
wglGenlockSourceI3D.play = True
wgl.add(wglGenlockSourceI3D)

wglGetGenlockSampleRateI3D = Function('wglGetGenlockSampleRateI3D')
wglGetGenlockSampleRateI3D.ret = Return('BOOL')
wglGetGenlockSampleRateI3D.add( Input( 'hDC','HDC' ))
wglGetGenlockSampleRateI3D.add( Output( 'uRate','UINT *' ,size = 1 ))
wglGetGenlockSampleRateI3D.version = ''
wglGetGenlockSampleRateI3D.category = 'WGL_I3D_genlock'
wglGetGenlockSampleRateI3D.trace = True
wglGetGenlockSampleRateI3D.play = True
wgl.add(wglGetGenlockSampleRateI3D)

wglGetGenlockSourceDelayI3D = Function('wglGetGenlockSourceDelayI3D')
wglGetGenlockSourceDelayI3D.ret = Return('BOOL')
wglGetGenlockSourceDelayI3D.add( Input( 'hDC','HDC' ))
wglGetGenlockSourceDelayI3D.add( Output( 'uDelay','UINT *' ,size = 1 ))
wglGetGenlockSourceDelayI3D.version = ''
wglGetGenlockSourceDelayI3D.category = 'WGL_I3D_genlock'
wglGetGenlockSourceDelayI3D.trace = True
wglGetGenlockSourceDelayI3D.play = True
wgl.add(wglGetGenlockSourceDelayI3D)

wglGetGenlockSourceEdgeI3D = Function('wglGetGenlockSourceEdgeI3D')
wglGetGenlockSourceEdgeI3D.ret = Return('BOOL')
wglGetGenlockSourceEdgeI3D.add( Input( 'hDC','HDC' ))
wglGetGenlockSourceEdgeI3D.add( Output( 'uEdge','UINT *' ,size = 1 ))
wglGetGenlockSourceEdgeI3D.version = ''
wglGetGenlockSourceEdgeI3D.category = 'WGL_I3D_genlock'
wglGetGenlockSourceEdgeI3D.trace = True
wglGetGenlockSourceEdgeI3D.play = True
wgl.add(wglGetGenlockSourceEdgeI3D)

wglGetGenlockSourceI3D = Function('wglGetGenlockSourceI3D')
wglGetGenlockSourceI3D.ret = Return('BOOL')
wglGetGenlockSourceI3D.add( Input( 'hDC','HDC' ))
wglGetGenlockSourceI3D.add( Output( 'uSource','UINT *' ,size = 1 ))
wglGetGenlockSourceI3D.version = ''
wglGetGenlockSourceI3D.category = 'WGL_I3D_genlock'
wglGetGenlockSourceI3D.trace = True
wglGetGenlockSourceI3D.play = True
wgl.add(wglGetGenlockSourceI3D)

wglIsEnabledGenlockI3D = Function('wglIsEnabledGenlockI3D')
wglIsEnabledGenlockI3D.ret = Return('BOOL')
wglIsEnabledGenlockI3D.add( Input( 'hDC','HDC' ))
wglIsEnabledGenlockI3D.add( Output( 'pFlag','BOOL *' ,size = 1 ))
wglIsEnabledGenlockI3D.version = ''
wglIsEnabledGenlockI3D.category = 'WGL_I3D_genlock'
wglIsEnabledGenlockI3D.trace = True
wglIsEnabledGenlockI3D.play = True
wgl.add(wglIsEnabledGenlockI3D)

wglQueryGenlockMaxSourceDelayI3D = Function('wglQueryGenlockMaxSourceDelayI3D')
wglQueryGenlockMaxSourceDelayI3D.ret = Return('BOOL')
wglQueryGenlockMaxSourceDelayI3D.add( Input( 'hDC','HDC' ))
wglQueryGenlockMaxSourceDelayI3D.add( Output( 'uMaxLineDelay','UINT *' ,size = 1 ))
wglQueryGenlockMaxSourceDelayI3D.add( Output( 'uMaxPixelDelay','UINT *' ,size = 1 ))
wglQueryGenlockMaxSourceDelayI3D.version = ''
wglQueryGenlockMaxSourceDelayI3D.category = 'WGL_I3D_genlock'
wglQueryGenlockMaxSourceDelayI3D.trace = True
wglQueryGenlockMaxSourceDelayI3D.play = True
wgl.add(wglQueryGenlockMaxSourceDelayI3D)

# WGL_I3D_image_buffer

wglAssociateImageBufferEventsI3D = Function('wglAssociateImageBufferEventsI3D')
wglAssociateImageBufferEventsI3D.ret = Return('BOOL')
wglAssociateImageBufferEventsI3D.add( Input( 'hDC','HDC' ))
wglAssociateImageBufferEventsI3D.add( Input( 'pEvent','const HANDLE *' ,size = 'count' ))
wglAssociateImageBufferEventsI3D.add( Input( 'pAddress','const LPVOID *' ,size = 'count' ))
wglAssociateImageBufferEventsI3D.add( Input( 'pSize','const DWORD *' ,size = 'count' ))
wglAssociateImageBufferEventsI3D.add( Input( 'count','UINT' ))
wglAssociateImageBufferEventsI3D.version = ''
wglAssociateImageBufferEventsI3D.category = 'WGL_I3D_image_buffer'
wglAssociateImageBufferEventsI3D.trace = True
wglAssociateImageBufferEventsI3D.play = True
wgl.add(wglAssociateImageBufferEventsI3D)

wglCreateImageBufferI3D = Function('wglCreateImageBufferI3D')
wglCreateImageBufferI3D.ret = Return('LPVOID')
wglCreateImageBufferI3D.add( Input( 'hDC','HDC' ))
wglCreateImageBufferI3D.add( Input( 'dwSize','DWORD' ))
wglCreateImageBufferI3D.add( Input( 'uFlags','UINT' ))
wglCreateImageBufferI3D.version = ''
wglCreateImageBufferI3D.category = 'WGL_I3D_image_buffer'
wglCreateImageBufferI3D.trace = True
wglCreateImageBufferI3D.play = True
wgl.add(wglCreateImageBufferI3D)

wglDestroyImageBufferI3D = Function('wglDestroyImageBufferI3D')
wglDestroyImageBufferI3D.ret = Return('BOOL')
wglDestroyImageBufferI3D.add( Input( 'hDC','HDC' ))
wglDestroyImageBufferI3D.add( Input( 'pAddress','LPVOID' ))
wglDestroyImageBufferI3D.version = ''
wglDestroyImageBufferI3D.category = 'WGL_I3D_image_buffer'
wglDestroyImageBufferI3D.trace = True
wglDestroyImageBufferI3D.play = True
wgl.add(wglDestroyImageBufferI3D)

wglReleaseImageBufferEventsI3D = Function('wglReleaseImageBufferEventsI3D')
wglReleaseImageBufferEventsI3D.ret = Return('BOOL')
wglReleaseImageBufferEventsI3D.add( Input( 'hDC','HDC' ))
wglReleaseImageBufferEventsI3D.add( Input( 'pAddress','const LPVOID *' ,size = 'count' ))
wglReleaseImageBufferEventsI3D.add( Input( 'count','UINT' ))
wglReleaseImageBufferEventsI3D.version = ''
wglReleaseImageBufferEventsI3D.category = 'WGL_I3D_image_buffer'
wglReleaseImageBufferEventsI3D.trace = True
wglReleaseImageBufferEventsI3D.play = True
wgl.add(wglReleaseImageBufferEventsI3D)

# WGL_I3D_swap_frame_lock

wglDisableFrameLockI3D = Function('wglDisableFrameLockI3D')
wglDisableFrameLockI3D.ret = Return('BOOL')
wglDisableFrameLockI3D.version = ''
wglDisableFrameLockI3D.category = 'WGL_I3D_swap_frame_lock'
wglDisableFrameLockI3D.trace = True
wglDisableFrameLockI3D.play = True
wgl.add(wglDisableFrameLockI3D)

wglEnableFrameLockI3D = Function('wglEnableFrameLockI3D')
wglEnableFrameLockI3D.ret = Return('BOOL')
wglEnableFrameLockI3D.version = ''
wglEnableFrameLockI3D.category = 'WGL_I3D_swap_frame_lock'
wglEnableFrameLockI3D.trace = True
wglEnableFrameLockI3D.play = True
wgl.add(wglEnableFrameLockI3D)

wglIsEnabledFrameLockI3D = Function('wglIsEnabledFrameLockI3D')
wglIsEnabledFrameLockI3D.ret = Return('BOOL')
wglIsEnabledFrameLockI3D.add( Output( 'pFlag','BOOL *' ,size = 1 ))
wglIsEnabledFrameLockI3D.version = ''
wglIsEnabledFrameLockI3D.category = 'WGL_I3D_swap_frame_lock'
wglIsEnabledFrameLockI3D.trace = True
wglIsEnabledFrameLockI3D.play = True
wgl.add(wglIsEnabledFrameLockI3D)

wglQueryFrameLockMasterI3D = Function('wglQueryFrameLockMasterI3D')
wglQueryFrameLockMasterI3D.ret = Return('BOOL')
wglQueryFrameLockMasterI3D.add( Output( 'pFlag','BOOL *' ,size = 1 ))
wglQueryFrameLockMasterI3D.version = ''
wglQueryFrameLockMasterI3D.category = 'WGL_I3D_swap_frame_lock'
wglQueryFrameLockMasterI3D.trace = True
wglQueryFrameLockMasterI3D.play = True
wgl.add(wglQueryFrameLockMasterI3D)

# WGL_I3D_swap_frame_usage

wglBeginFrameTrackingI3D = Function('wglBeginFrameTrackingI3D')
wglBeginFrameTrackingI3D.ret = Return('BOOL')
wglBeginFrameTrackingI3D.version = ''
wglBeginFrameTrackingI3D.category = 'WGL_I3D_swap_frame_usage'
wglBeginFrameTrackingI3D.trace = True
wglBeginFrameTrackingI3D.play = True
wgl.add(wglBeginFrameTrackingI3D)

wglEndFrameTrackingI3D = Function('wglEndFrameTrackingI3D')
wglEndFrameTrackingI3D.ret = Return('BOOL')
wglEndFrameTrackingI3D.version = ''
wglEndFrameTrackingI3D.category = 'WGL_I3D_swap_frame_usage'
wglEndFrameTrackingI3D.trace = True
wglEndFrameTrackingI3D.play = True
wgl.add(wglEndFrameTrackingI3D)

wglGetFrameUsageI3D = Function('wglGetFrameUsageI3D')
wglGetFrameUsageI3D.ret = Return('BOOL')
wglGetFrameUsageI3D.add( Output( 'pUsage','float *' ,size = 1 ))
wglGetFrameUsageI3D.version = ''
wglGetFrameUsageI3D.category = 'WGL_I3D_swap_frame_usage'
wglGetFrameUsageI3D.trace = True
wglGetFrameUsageI3D.play = True
wgl.add(wglGetFrameUsageI3D)

wglQueryFrameTrackingI3D = Function('wglQueryFrameTrackingI3D')
wglQueryFrameTrackingI3D.ret = Return('BOOL')
wglQueryFrameTrackingI3D.add( Output( 'pFrameCount','DWORD *' ,size = 1 ))
wglQueryFrameTrackingI3D.add( Output( 'pMissedFrames','DWORD *' ,size = 1 ))
wglQueryFrameTrackingI3D.add( Output( 'pLastMissedUsage','float *' ,size = 1 ))
wglQueryFrameTrackingI3D.version = ''
wglQueryFrameTrackingI3D.category = 'WGL_I3D_swap_frame_usage'
wglQueryFrameTrackingI3D.trace = True
wglQueryFrameTrackingI3D.play = True
wgl.add(wglQueryFrameTrackingI3D)

# WGL_NV_copy_image

wglCopyImageSubDataNV = Function('wglCopyImageSubDataNV')
wglCopyImageSubDataNV.ret = Return('BOOL')
wglCopyImageSubDataNV.add( Input( 'hSrcRC','HGLRC' ))
wglCopyImageSubDataNV.add( Input( 'srcName','GLuint' ))
wglCopyImageSubDataNV.add( Input( 'srcTarget','GLenum' ))
wglCopyImageSubDataNV.add( Input( 'srcLevel','GLint' ))
wglCopyImageSubDataNV.add( Input( 'srcX','GLint' ))
wglCopyImageSubDataNV.add( Input( 'srcY','GLint' ))
wglCopyImageSubDataNV.add( Input( 'srcZ','GLint' ))
wglCopyImageSubDataNV.add( Input( 'hDstRC','HGLRC' ))
wglCopyImageSubDataNV.add( Input( 'dstName','GLuint' ))
wglCopyImageSubDataNV.add( Input( 'dstTarget','GLenum' ))
wglCopyImageSubDataNV.add( Input( 'dstLevel','GLint' ))
wglCopyImageSubDataNV.add( Input( 'dstX','GLint' ))
wglCopyImageSubDataNV.add( Input( 'dstY','GLint' ))
wglCopyImageSubDataNV.add( Input( 'dstZ','GLint' ))
wglCopyImageSubDataNV.add( Input( 'width','GLsizei' ))
wglCopyImageSubDataNV.add( Input( 'height','GLsizei' ))
wglCopyImageSubDataNV.add( Input( 'depth','GLsizei' ))
wglCopyImageSubDataNV.version = ''
wglCopyImageSubDataNV.category = 'WGL_NV_copy_image'
wglCopyImageSubDataNV.trace = True
wglCopyImageSubDataNV.play = True
wgl.add(wglCopyImageSubDataNV)

# WGL_NV_gpu_affinity

wglCreateAffinityDCNV = Function('wglCreateAffinityDCNV')
wglCreateAffinityDCNV.ret = Return('HDC')
wglCreateAffinityDCNV.add( Input( 'phGpuList','const HGPUNV *' ))
wglCreateAffinityDCNV.version = ''
wglCreateAffinityDCNV.category = 'WGL_NV_gpu_affinity'
wglCreateAffinityDCNV.trace = True
wglCreateAffinityDCNV.play = True
wgl.add(wglCreateAffinityDCNV)

wglDeleteDCNV = Function('wglDeleteDCNV')
wglDeleteDCNV.ret = Return('BOOL')
wglDeleteDCNV.add( Input( 'hAffinityDC','HDC' ))
wglDeleteDCNV.version = ''
wglDeleteDCNV.category = 'WGL_NV_gpu_affinity'
wglDeleteDCNV.trace = True
wglDeleteDCNV.play = True
wgl.add(wglDeleteDCNV)

wglEnumGpuDevicesNV = Function('wglEnumGpuDevicesNV')
wglEnumGpuDevicesNV.ret = Return('BOOL')
wglEnumGpuDevicesNV.add( Input( 'hGpu','HGPUNV' ))
wglEnumGpuDevicesNV.add( Input( 'iDeviceIndex','UINT' ))
wglEnumGpuDevicesNV.add( Output( 'lpGpuDevice','PGPU_DEVICE' ))
wglEnumGpuDevicesNV.version = ''
wglEnumGpuDevicesNV.category = 'WGL_NV_gpu_affinity'
wglEnumGpuDevicesNV.trace = True
wglEnumGpuDevicesNV.play = True
wgl.add(wglEnumGpuDevicesNV)

wglEnumGpusFromAffinityDCNV = Function('wglEnumGpusFromAffinityDCNV')
wglEnumGpusFromAffinityDCNV.ret = Return('BOOL')
wglEnumGpusFromAffinityDCNV.add( Input( 'hAffinityDC','HDC' ))
wglEnumGpusFromAffinityDCNV.add( Input( 'iGpuIndex','UINT' ))
wglEnumGpusFromAffinityDCNV.add( Output( 'hGpu','HGPUNV *' ,size = 1 ))
wglEnumGpusFromAffinityDCNV.version = ''
wglEnumGpusFromAffinityDCNV.category = 'WGL_NV_gpu_affinity'
wglEnumGpusFromAffinityDCNV.trace = True
wglEnumGpusFromAffinityDCNV.play = True
wgl.add(wglEnumGpusFromAffinityDCNV)

wglEnumGpusNV = Function('wglEnumGpusNV')
wglEnumGpusNV.ret = Return('BOOL')
wglEnumGpusNV.add( Input( 'iGpuIndex','UINT' ))
wglEnumGpusNV.add( Output( 'phGpu','HGPUNV *' ,size = 1 ))
wglEnumGpusNV.version = ''
wglEnumGpusNV.category = 'WGL_NV_gpu_affinity'
wglEnumGpusNV.trace = True
wglEnumGpusNV.play = True
wgl.add(wglEnumGpusNV)

# WGL_NV_present_video

wglBindVideoDeviceNV = Function('wglBindVideoDeviceNV')
wglBindVideoDeviceNV.ret = Return('BOOL')
wglBindVideoDeviceNV.add( Input( 'hDC','HDC' ))
wglBindVideoDeviceNV.add( Input( 'uVideoSlot','unsigned int' ))
wglBindVideoDeviceNV.add( Input( 'hVideoDevice','HVIDEOOUTPUTDEVICENV' ))
wglBindVideoDeviceNV.add( Input( 'piAttribList','const int *' ))
wglBindVideoDeviceNV.version = ''
wglBindVideoDeviceNV.category = 'WGL_NV_present_video'
wglBindVideoDeviceNV.trace = True
wglBindVideoDeviceNV.play = True
wgl.add(wglBindVideoDeviceNV)

wglEnumerateVideoDevicesNV = Function('wglEnumerateVideoDevicesNV')
wglEnumerateVideoDevicesNV.ret = Return('int')
wglEnumerateVideoDevicesNV.add( Input( 'hDC','HDC' ))
wglEnumerateVideoDevicesNV.add( Output( 'phDeviceList','HVIDEOOUTPUTDEVICENV *' ))
wglEnumerateVideoDevicesNV.version = ''
wglEnumerateVideoDevicesNV.category = 'WGL_NV_present_video'
wglEnumerateVideoDevicesNV.trace = True
wglEnumerateVideoDevicesNV.play = True
wgl.add(wglEnumerateVideoDevicesNV)

wglQueryCurrentContextNV = Function('wglQueryCurrentContextNV')
wglQueryCurrentContextNV.ret = Return('BOOL')
wglQueryCurrentContextNV.add( Input( 'iAttribute','int' ))
wglQueryCurrentContextNV.add( Output( 'piValue','int *' ))
wglQueryCurrentContextNV.version = ''
wglQueryCurrentContextNV.category = 'WGL_NV_present_video'
wglQueryCurrentContextNV.trace = True
wglQueryCurrentContextNV.play = True
wgl.add(wglQueryCurrentContextNV)

# WGL_NV_swap_group

wglBindSwapBarrierNV = Function('wglBindSwapBarrierNV')
wglBindSwapBarrierNV.ret = Return('BOOL')
wglBindSwapBarrierNV.add( Input( 'group','GLuint' ))
wglBindSwapBarrierNV.add( Input( 'barrier','GLuint' ))
wglBindSwapBarrierNV.version = ''
wglBindSwapBarrierNV.category = 'WGL_NV_swap_group'
wglBindSwapBarrierNV.trace = True
wglBindSwapBarrierNV.play = True
wgl.add(wglBindSwapBarrierNV)

wglJoinSwapGroupNV = Function('wglJoinSwapGroupNV')
wglJoinSwapGroupNV.ret = Return('BOOL')
wglJoinSwapGroupNV.add( Input( 'hDC','HDC' ))
wglJoinSwapGroupNV.add( Input( 'group','GLuint' ))
wglJoinSwapGroupNV.version = ''
wglJoinSwapGroupNV.category = 'WGL_NV_swap_group'
wglJoinSwapGroupNV.trace = True
wglJoinSwapGroupNV.play = True
wgl.add(wglJoinSwapGroupNV)

wglQueryFrameCountNV = Function('wglQueryFrameCountNV')
wglQueryFrameCountNV.ret = Return('BOOL')
wglQueryFrameCountNV.add( Input( 'hDC','HDC' ))
wglQueryFrameCountNV.add( Output( 'count','GLuint *' ,size = 1 ))
wglQueryFrameCountNV.version = ''
wglQueryFrameCountNV.category = 'WGL_NV_swap_group'
wglQueryFrameCountNV.trace = True
wglQueryFrameCountNV.play = True
wgl.add(wglQueryFrameCountNV)

wglQueryMaxSwapGroupsNV = Function('wglQueryMaxSwapGroupsNV')
wglQueryMaxSwapGroupsNV.ret = Return('BOOL')
wglQueryMaxSwapGroupsNV.add( Input( 'hDC','HDC' ))
wglQueryMaxSwapGroupsNV.add( Output( 'maxGroups','GLuint *' ,size = 1 ))
wglQueryMaxSwapGroupsNV.add( Output( 'maxBarriers','GLuint *' ,size = 1 ))
wglQueryMaxSwapGroupsNV.version = ''
wglQueryMaxSwapGroupsNV.category = 'WGL_NV_swap_group'
wglQueryMaxSwapGroupsNV.trace = True
wglQueryMaxSwapGroupsNV.play = True
wgl.add(wglQueryMaxSwapGroupsNV)

wglQuerySwapGroupNV = Function('wglQuerySwapGroupNV')
wglQuerySwapGroupNV.ret = Return('BOOL')
wglQuerySwapGroupNV.add( Input( 'hDC','HDC' ))
wglQuerySwapGroupNV.add( Output( 'group','GLuint *' ,size = 1 ))
wglQuerySwapGroupNV.add( Output( 'barrier','GLuint *' ,size = 1 ))
wglQuerySwapGroupNV.version = ''
wglQuerySwapGroupNV.category = 'WGL_NV_swap_group'
wglQuerySwapGroupNV.trace = True
wglQuerySwapGroupNV.play = True
wgl.add(wglQuerySwapGroupNV)

wglResetFrameCountNV = Function('wglResetFrameCountNV')
wglResetFrameCountNV.ret = Return('BOOL')
wglResetFrameCountNV.add( Input( 'hDC','HDC' ))
wglResetFrameCountNV.version = ''
wglResetFrameCountNV.category = 'WGL_NV_swap_group'
wglResetFrameCountNV.trace = True
wglResetFrameCountNV.play = True
wgl.add(wglResetFrameCountNV)

# WGL_NV_vertex_array_range

wglAllocateMemoryNV = Function('wglAllocateMemoryNV')
wglAllocateMemoryNV.ret = Return('void *')
wglAllocateMemoryNV.add( Input( 'size','GLsizei' ))
wglAllocateMemoryNV.add( Input( 'readfreq','GLfloat' ))
wglAllocateMemoryNV.add( Input( 'writefreq','GLfloat' ))
wglAllocateMemoryNV.add( Input( 'priority','GLfloat' ))
wglAllocateMemoryNV.version = ''
wglAllocateMemoryNV.category = 'WGL_NV_vertex_array_range'
wglAllocateMemoryNV.trace = True
wglAllocateMemoryNV.play = True
wgl.add(wglAllocateMemoryNV)

wglFreeMemoryNV = Function('wglFreeMemoryNV')
wglFreeMemoryNV.ret = Return('void')
wglFreeMemoryNV.add( Input( 'pointer','void *' ,size = 1 ))
wglFreeMemoryNV.version = ''
wglFreeMemoryNV.category = 'WGL_NV_vertex_array_range'
wglFreeMemoryNV.trace = True
wglFreeMemoryNV.play = True
wgl.add(wglFreeMemoryNV)

# WGL_NV_video_capture

wglBindVideoCaptureDeviceNV = Function('wglBindVideoCaptureDeviceNV')
wglBindVideoCaptureDeviceNV.ret = Return('BOOL')
wglBindVideoCaptureDeviceNV.add( Input( 'uVideoSlot','UINT' ))
wglBindVideoCaptureDeviceNV.add( Input( 'hDevice','HVIDEOINPUTDEVICENV' ))
wglBindVideoCaptureDeviceNV.version = ''
wglBindVideoCaptureDeviceNV.category = 'WGL_NV_video_capture'
wglBindVideoCaptureDeviceNV.trace = True
wglBindVideoCaptureDeviceNV.play = True
wgl.add(wglBindVideoCaptureDeviceNV)

wglEnumerateVideoCaptureDevicesNV = Function('wglEnumerateVideoCaptureDevicesNV')
wglEnumerateVideoCaptureDevicesNV.ret = Return('UINT')
wglEnumerateVideoCaptureDevicesNV.add( Input( 'hDC','HDC' ))
wglEnumerateVideoCaptureDevicesNV.add( Output( 'phDeviceList','HVIDEOINPUTDEVICENV *' ,size = 1 ))
wglEnumerateVideoCaptureDevicesNV.version = ''
wglEnumerateVideoCaptureDevicesNV.category = 'WGL_NV_video_capture'
wglEnumerateVideoCaptureDevicesNV.trace = True
wglEnumerateVideoCaptureDevicesNV.play = True
wgl.add(wglEnumerateVideoCaptureDevicesNV)

wglLockVideoCaptureDeviceNV = Function('wglLockVideoCaptureDeviceNV')
wglLockVideoCaptureDeviceNV.ret = Return('BOOL')
wglLockVideoCaptureDeviceNV.add( Input( 'hDC','HDC' ))
wglLockVideoCaptureDeviceNV.add( Input( 'hDevice','HVIDEOINPUTDEVICENV' ))
wglLockVideoCaptureDeviceNV.version = ''
wglLockVideoCaptureDeviceNV.category = 'WGL_NV_video_capture'
wglLockVideoCaptureDeviceNV.trace = True
wglLockVideoCaptureDeviceNV.play = True
wgl.add(wglLockVideoCaptureDeviceNV)

wglQueryVideoCaptureDeviceNV = Function('wglQueryVideoCaptureDeviceNV')
wglQueryVideoCaptureDeviceNV.ret = Return('BOOL')
wglQueryVideoCaptureDeviceNV.add( Input( 'hDC','HDC' ))
wglQueryVideoCaptureDeviceNV.add( Input( 'hDevice','HVIDEOINPUTDEVICENV' ))
wglQueryVideoCaptureDeviceNV.add( Input( 'iAttribute','int' ))
wglQueryVideoCaptureDeviceNV.add( Output( 'piValue','int *' ,size = 1 ))
wglQueryVideoCaptureDeviceNV.version = ''
wglQueryVideoCaptureDeviceNV.category = 'WGL_NV_video_capture'
wglQueryVideoCaptureDeviceNV.trace = True
wglQueryVideoCaptureDeviceNV.play = True
wgl.add(wglQueryVideoCaptureDeviceNV)

wglReleaseVideoCaptureDeviceNV = Function('wglReleaseVideoCaptureDeviceNV')
wglReleaseVideoCaptureDeviceNV.ret = Return('BOOL')
wglReleaseVideoCaptureDeviceNV.add( Input( 'hDC','HDC' ))
wglReleaseVideoCaptureDeviceNV.add( Input( 'hDevice','HVIDEOINPUTDEVICENV' ))
wglReleaseVideoCaptureDeviceNV.version = ''
wglReleaseVideoCaptureDeviceNV.category = 'WGL_NV_video_capture'
wglReleaseVideoCaptureDeviceNV.trace = True
wglReleaseVideoCaptureDeviceNV.play = True
wgl.add(wglReleaseVideoCaptureDeviceNV)

# WGL_NV_video_output

wglBindVideoImageNV = Function('wglBindVideoImageNV')
wglBindVideoImageNV.ret = Return('BOOL')
wglBindVideoImageNV.add( Input( 'hVideoDevice','HPVIDEODEV' ))
wglBindVideoImageNV.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglBindVideoImageNV.add( Input( 'iVideoBuffer','int' ))
wglBindVideoImageNV.version = ''
wglBindVideoImageNV.category = 'WGL_NV_video_output'
wglBindVideoImageNV.trace = True
wglBindVideoImageNV.play = True
wgl.add(wglBindVideoImageNV)

wglGetVideoDeviceNV = Function('wglGetVideoDeviceNV')
wglGetVideoDeviceNV.ret = Return('BOOL')
wglGetVideoDeviceNV.add( Input( 'hDC','HDC' ))
wglGetVideoDeviceNV.add( Input( 'numDevices','int' ))
wglGetVideoDeviceNV.add( Output( 'hVideoDevice','HPVIDEODEV *' ,size = 1 ))
wglGetVideoDeviceNV.version = ''
wglGetVideoDeviceNV.category = 'WGL_NV_video_output'
wglGetVideoDeviceNV.trace = True
wglGetVideoDeviceNV.play = True
wgl.add(wglGetVideoDeviceNV)

wglGetVideoInfoNV = Function('wglGetVideoInfoNV')
wglGetVideoInfoNV.ret = Return('BOOL')
wglGetVideoInfoNV.add( Input( 'hpVideoDevice','HPVIDEODEV' ))
wglGetVideoInfoNV.add( Output( 'pulCounterOutputPbuffer','unsigned long *' ,size = 1 ))
wglGetVideoInfoNV.add( Output( 'pulCounterOutputVideo','unsigned long *' ,size = 1 ))
wglGetVideoInfoNV.version = ''
wglGetVideoInfoNV.category = 'WGL_NV_video_output'
wglGetVideoInfoNV.trace = True
wglGetVideoInfoNV.play = True
wgl.add(wglGetVideoInfoNV)

wglReleaseVideoDeviceNV = Function('wglReleaseVideoDeviceNV')
wglReleaseVideoDeviceNV.ret = Return('BOOL')
wglReleaseVideoDeviceNV.add( Input( 'hVideoDevice','HPVIDEODEV' ))
wglReleaseVideoDeviceNV.version = ''
wglReleaseVideoDeviceNV.category = 'WGL_NV_video_output'
wglReleaseVideoDeviceNV.trace = True
wglReleaseVideoDeviceNV.play = True
wgl.add(wglReleaseVideoDeviceNV)

wglReleaseVideoImageNV = Function('wglReleaseVideoImageNV')
wglReleaseVideoImageNV.ret = Return('BOOL')
wglReleaseVideoImageNV.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglReleaseVideoImageNV.add( Input( 'iVideoBuffer','int' ))
wglReleaseVideoImageNV.version = ''
wglReleaseVideoImageNV.category = 'WGL_NV_video_output'
wglReleaseVideoImageNV.trace = True
wglReleaseVideoImageNV.play = True
wgl.add(wglReleaseVideoImageNV)

wglSendPbufferToVideoNV = Function('wglSendPbufferToVideoNV')
wglSendPbufferToVideoNV.ret = Return('BOOL')
wglSendPbufferToVideoNV.add( Input( 'hPbuffer','HPBUFFERARB' ))
wglSendPbufferToVideoNV.add( Input( 'iBufferType','int' ))
wglSendPbufferToVideoNV.add( Output( 'pulCounterPbuffer','unsigned long *' ,size = 1 ))
wglSendPbufferToVideoNV.add( Input( 'bBlock','BOOL' ))
wglSendPbufferToVideoNV.version = ''
wglSendPbufferToVideoNV.category = 'WGL_NV_video_output'
wglSendPbufferToVideoNV.trace = True
wglSendPbufferToVideoNV.play = True
wgl.add(wglSendPbufferToVideoNV)

# WGL_OML_sync_control

wglGetMscRateOML = Function('wglGetMscRateOML')
wglGetMscRateOML.ret = Return('BOOL')
wglGetMscRateOML.add( Input( 'hDC','HDC' ))
wglGetMscRateOML.add( Output( 'numerator','INT32 *' ,size = 1 ))
wglGetMscRateOML.add( Output( 'denominator','INT32 *' ,size = 1 ))
wglGetMscRateOML.version = ''
wglGetMscRateOML.category = 'WGL_OML_sync_control'
wglGetMscRateOML.trace = True
wglGetMscRateOML.play = True
wgl.add(wglGetMscRateOML)

wglGetSyncValuesOML = Function('wglGetSyncValuesOML')
wglGetSyncValuesOML.ret = Return('BOOL')
wglGetSyncValuesOML.add( Input( 'hDC','HDC' ))
wglGetSyncValuesOML.add( Output( 'ust','INT64 *' ,size = 1 ))
wglGetSyncValuesOML.add( Output( 'msc','INT64 *' ,size = 1 ))
wglGetSyncValuesOML.add( Output( 'sbc','INT64 *' ,size = 1 ))
wglGetSyncValuesOML.version = ''
wglGetSyncValuesOML.category = 'WGL_OML_sync_control'
wglGetSyncValuesOML.trace = True
wglGetSyncValuesOML.play = True
wgl.add(wglGetSyncValuesOML)

wglSwapBuffersMscOML = Function('wglSwapBuffersMscOML')
wglSwapBuffersMscOML.ret = Return('INT64')
wglSwapBuffersMscOML.add( Input( 'hDC','HDC' ))
wglSwapBuffersMscOML.add( Input( 'target_msc','INT64' ))
wglSwapBuffersMscOML.add( Input( 'divisor','INT64' ))
wglSwapBuffersMscOML.add( Input( 'remainder','INT64' ))
wglSwapBuffersMscOML.version = ''
wglSwapBuffersMscOML.category = 'WGL_OML_sync_control'
wglSwapBuffersMscOML.trace = True
wglSwapBuffersMscOML.play = True
wgl.add(wglSwapBuffersMscOML)

wglSwapLayerBuffersMscOML = Function('wglSwapLayerBuffersMscOML')
wglSwapLayerBuffersMscOML.ret = Return('INT64')
wglSwapLayerBuffersMscOML.add( Input( 'hDC','HDC' ))
wglSwapLayerBuffersMscOML.add( Input( 'fuPlanes','int' ))
wglSwapLayerBuffersMscOML.add( Input( 'target_msc','INT64' ))
wglSwapLayerBuffersMscOML.add( Input( 'divisor','INT64' ))
wglSwapLayerBuffersMscOML.add( Input( 'remainder','INT64' ))
wglSwapLayerBuffersMscOML.version = ''
wglSwapLayerBuffersMscOML.category = 'WGL_OML_sync_control'
wglSwapLayerBuffersMscOML.trace = True
wglSwapLayerBuffersMscOML.play = True
wgl.add(wglSwapLayerBuffersMscOML)

wglWaitForMscOML = Function('wglWaitForMscOML')
wglWaitForMscOML.ret = Return('BOOL')
wglWaitForMscOML.add( Input( 'hDC','HDC' ))
wglWaitForMscOML.add( Input( 'target_msc','INT64' ))
wglWaitForMscOML.add( Input( 'divisor','INT64' ))
wglWaitForMscOML.add( Input( 'remainder','INT64' ))
wglWaitForMscOML.add( Output( 'ust','INT64 *' ,size = 1 ))
wglWaitForMscOML.add( Output( 'msc','INT64 *' ,size = 1 ))
wglWaitForMscOML.add( Output( 'sbc','INT64 *' ,size = 1 ))
wglWaitForMscOML.version = ''
wglWaitForMscOML.category = 'WGL_OML_sync_control'
wglWaitForMscOML.trace = True
wglWaitForMscOML.play = True
wgl.add(wglWaitForMscOML)

wglWaitForSbcOML = Function('wglWaitForSbcOML')
wglWaitForSbcOML.ret = Return('BOOL')
wglWaitForSbcOML.add( Input( 'hDC','HDC' ))
wglWaitForSbcOML.add( Input( 'target_sbc','INT64' ))
wglWaitForSbcOML.add( Output( 'ust','INT64 *' ,size = 1 ))
wglWaitForSbcOML.add( Output( 'msc','INT64 *' ,size = 1 ))
wglWaitForSbcOML.add( Output( 'sbc','INT64 *' ,size = 1 ))
wglWaitForSbcOML.version = ''
wglWaitForSbcOML.category = 'WGL_OML_sync_control'
wglWaitForSbcOML.trace = True
wglWaitForSbcOML.play = True
wgl.add(wglWaitForSbcOML)

# WGL_core

wglCopyContext = Function('wglCopyContext')
wglCopyContext.ret = Return('BOOL')
wglCopyContext.add( Input( 'hglrcSrc','HGLRC' ))
wglCopyContext.add( Input( 'hglrcDst','HGLRC' ))
wglCopyContext.add( Input( 'mask','UINT' ))
wglCopyContext.version = ''
wglCopyContext.category = 'WGL_core'
wglCopyContext.trace = True
wglCopyContext.play = True
wgl.add(wglCopyContext)

wglCreateContext = Function('wglCreateContext')
wglCreateContext.ret = Return('HGLRC')
wglCreateContext.add( Input( 'hDC','HDC' ))
wglCreateContext.version = ''
wglCreateContext.category = 'WGL_core'
wglCreateContext.trace = True
wglCreateContext.play = True
wgl.add(wglCreateContext)

wglCreateLayerContext = Function('wglCreateLayerContext')
wglCreateLayerContext.ret = Return('HGLRC')
wglCreateLayerContext.add( Input( 'hDC','HDC' ))
wglCreateLayerContext.add( Input( 'iLayerPlane','int' ))
wglCreateLayerContext.version = ''
wglCreateLayerContext.category = 'WGL_core'
wglCreateLayerContext.trace = True
wglCreateLayerContext.play = True
wgl.add(wglCreateLayerContext)

wglDeleteContext = Function('wglDeleteContext')
wglDeleteContext.ret = Return('BOOL')
wglDeleteContext.add( Input( 'hglrc','HGLRC' ))
wglDeleteContext.version = ''
wglDeleteContext.category = 'WGL_core'
wglDeleteContext.trace = True
wglDeleteContext.play = True
wgl.add(wglDeleteContext)

wglDescribeLayerPlane = Function('wglDescribeLayerPlane')
wglDescribeLayerPlane.ret = Return('BOOL')
wglDescribeLayerPlane.add( Input( 'hDC','HDC' ))
wglDescribeLayerPlane.add( Input( 'iPixelFormat','int' ))
wglDescribeLayerPlane.add( Input( 'iLayerPlane','int' ))
wglDescribeLayerPlane.add( Input( 'nBytes','UINT' ))
wglDescribeLayerPlane.add( Output( 'plpd','LPLAYERPLANEDESCRIPTOR' ,size = 1 ))
wglDescribeLayerPlane.version = ''
wglDescribeLayerPlane.category = 'WGL_core'
wglDescribeLayerPlane.trace = True
wglDescribeLayerPlane.play = True
wgl.add(wglDescribeLayerPlane)

wglGetCurrentContext = Function('wglGetCurrentContext')
wglGetCurrentContext.ret = Return('HGLRC')
wglGetCurrentContext.version = ''
wglGetCurrentContext.category = 'WGL_core'
wglGetCurrentContext.trace = True
wglGetCurrentContext.play = False
wgl.add(wglGetCurrentContext)

wglGetCurrentDC = Function('wglGetCurrentDC')
wglGetCurrentDC.ret = Return('HDC')
wglGetCurrentDC.version = ''
wglGetCurrentDC.category = 'WGL_core'
wglGetCurrentDC.trace = True
wglGetCurrentDC.play = False
wgl.add(wglGetCurrentDC)

wglGetDefaultProcAddress = Function('wglGetDefaultProcAddress')
wglGetDefaultProcAddress.ret = Return('PROC')
wglGetDefaultProcAddress.add( Input( 'lpszProc','LPCSTR' ))
wglGetDefaultProcAddress.version = ''
wglGetDefaultProcAddress.category = 'WGL_core'
wglGetDefaultProcAddress.trace = True
wglGetDefaultProcAddress.play = False
wgl.add(wglGetDefaultProcAddress)

wglGetLayerPaletteEntries = Function('wglGetLayerPaletteEntries')
wglGetLayerPaletteEntries.ret = Return('int')
wglGetLayerPaletteEntries.add( Input( 'hDC','HDC' ))
wglGetLayerPaletteEntries.add( Input( 'iLayerPlane','int' ))
wglGetLayerPaletteEntries.add( Input( 'iStart','int' ))
wglGetLayerPaletteEntries.add( Input( 'nEntries','int' ))
wglGetLayerPaletteEntries.add( Output( 'pcr','COLORREF *' ,size = 'ret' ))
wglGetLayerPaletteEntries.version = ''
wglGetLayerPaletteEntries.category = 'WGL_core'
wglGetLayerPaletteEntries.trace = True
wglGetLayerPaletteEntries.play = True
wgl.add(wglGetLayerPaletteEntries)

wglGetProcAddress = Function('wglGetProcAddress')
wglGetProcAddress.ret = Return('PROC')
wglGetProcAddress.add( Input( 'lpszProc','LPCSTR' ))
wglGetProcAddress.version = ''
wglGetProcAddress.category = 'WGL_core'
wglGetProcAddress.trace = True
wglGetProcAddress.play = False
wgl.add(wglGetProcAddress)

wglMakeCurrent = Function('wglMakeCurrent')
wglMakeCurrent.ret = Return('BOOL')
wglMakeCurrent.add( Input( 'hDC','HDC' ))
wglMakeCurrent.add( Input( 'hglrc','HGLRC' ))
wglMakeCurrent.version = ''
wglMakeCurrent.category = 'WGL_core'
wglMakeCurrent.trace = True
wglMakeCurrent.play = True
wgl.add(wglMakeCurrent)

wglRealizeLayerPalette = Function('wglRealizeLayerPalette')
wglRealizeLayerPalette.ret = Return('BOOL')
wglRealizeLayerPalette.add( Input( 'hDC','HDC' ))
wglRealizeLayerPalette.add( Input( 'iLayerPlane','int' ))
wglRealizeLayerPalette.add( Input( 'bRealize','BOOL' ))
wglRealizeLayerPalette.version = ''
wglRealizeLayerPalette.category = 'WGL_core'
wglRealizeLayerPalette.trace = True
wglRealizeLayerPalette.play = True
wgl.add(wglRealizeLayerPalette)

wglSetLayerPaletteEntries = Function('wglSetLayerPaletteEntries')
wglSetLayerPaletteEntries.ret = Return('int')
wglSetLayerPaletteEntries.add( Input( 'hDC','HDC' ))
wglSetLayerPaletteEntries.add( Input( 'iLayerPlane','int' ))
wglSetLayerPaletteEntries.add( Input( 'iStart','int' ))
wglSetLayerPaletteEntries.add( Input( 'nEntries','int' ))
wglSetLayerPaletteEntries.add( Input( 'pcr','const COLORREF *' ,size = 'nEntries' ))
wglSetLayerPaletteEntries.version = ''
wglSetLayerPaletteEntries.category = 'WGL_core'
wglSetLayerPaletteEntries.trace = True
wglSetLayerPaletteEntries.play = True
wgl.add(wglSetLayerPaletteEntries)

wglShareLists = Function('wglShareLists')
wglShareLists.ret = Return('BOOL')
wglShareLists.add( Input( 'hglrcShare','HGLRC' ))
wglShareLists.add( Input( 'hglrcSrc','HGLRC' ))
wglShareLists.version = ''
wglShareLists.category = 'WGL_core'
wglShareLists.trace = True
wglShareLists.play = True
wgl.add(wglShareLists)

wglSwapLayerBuffers = Function('wglSwapLayerBuffers')
wglSwapLayerBuffers.ret = Return('BOOL')
wglSwapLayerBuffers.add( Input( 'hDC','HDC' ))
wglSwapLayerBuffers.add( Input( 'fuPlanes','UINT' ))
wglSwapLayerBuffers.version = ''
wglSwapLayerBuffers.category = 'WGL_core'
wglSwapLayerBuffers.trace = True
wglSwapLayerBuffers.play = True
wgl.add(wglSwapLayerBuffers)

wglSwapMultipleBuffers = Function('wglSwapMultipleBuffers')
wglSwapMultipleBuffers.ret = Return('DWORD')
wglSwapMultipleBuffers.add( Input( 'n','UINT' ))
wglSwapMultipleBuffers.add( Input( 'ps','const WGLSWAP *' ))
wglSwapMultipleBuffers.version = ''
wglSwapMultipleBuffers.category = 'WGL_core'
wglSwapMultipleBuffers.trace = True
wglSwapMultipleBuffers.play = True
wgl.add(wglSwapMultipleBuffers)

wglUseFontBitmapsA = Function('wglUseFontBitmapsA')
wglUseFontBitmapsA.ret = Return('BOOL')
wglUseFontBitmapsA.add( Input( 'hDC','HDC' ))
wglUseFontBitmapsA.add( Input( 'first','DWORD' ))
wglUseFontBitmapsA.add( Input( 'count','DWORD' ))
wglUseFontBitmapsA.add( Input( 'listBase','DWORD' ))
wglUseFontBitmapsA.version = ''
wglUseFontBitmapsA.category = 'WGL_core'
wglUseFontBitmapsA.trace = True
wglUseFontBitmapsA.play = True
wgl.add(wglUseFontBitmapsA)

wglUseFontBitmapsW = Function('wglUseFontBitmapsW')
wglUseFontBitmapsW.ret = Return('BOOL')
wglUseFontBitmapsW.add( Input( 'hDC','HDC' ))
wglUseFontBitmapsW.add( Input( 'first','DWORD' ))
wglUseFontBitmapsW.add( Input( 'count','DWORD' ))
wglUseFontBitmapsW.add( Input( 'listBase','DWORD' ))
wglUseFontBitmapsW.version = ''
wglUseFontBitmapsW.category = 'WGL_core'
wglUseFontBitmapsW.trace = True
wglUseFontBitmapsW.play = True
wgl.add(wglUseFontBitmapsW)

wglUseFontOutlinesA = Function('wglUseFontOutlinesA')
wglUseFontOutlinesA.ret = Return('BOOL')
wglUseFontOutlinesA.add( Input( 'hDC','HDC' ))
wglUseFontOutlinesA.add( Input( 'first','DWORD' ))
wglUseFontOutlinesA.add( Input( 'count','DWORD' ))
wglUseFontOutlinesA.add( Input( 'listBase','DWORD' ))
wglUseFontOutlinesA.add( Input( 'deviation','FLOAT' ))
wglUseFontOutlinesA.add( Input( 'extrusion','FLOAT' ))
wglUseFontOutlinesA.add( Input( 'format','int' ))
wglUseFontOutlinesA.add( Output( 'lpgmf','LPGLYPHMETRICSFLOAT' ,size = 'count' ))
wglUseFontOutlinesA.version = ''
wglUseFontOutlinesA.category = 'WGL_core'
wglUseFontOutlinesA.trace = True
wglUseFontOutlinesA.play = True
wgl.add(wglUseFontOutlinesA)

wglUseFontOutlinesW = Function('wglUseFontOutlinesW')
wglUseFontOutlinesW.ret = Return('BOOL')
wglUseFontOutlinesW.add( Input( 'hDC','HDC' ))
wglUseFontOutlinesW.add( Input( 'first','DWORD' ))
wglUseFontOutlinesW.add( Input( 'count','DWORD' ))
wglUseFontOutlinesW.add( Input( 'listBase','DWORD' ))
wglUseFontOutlinesW.add( Input( 'deviation','FLOAT' ))
wglUseFontOutlinesW.add( Input( 'extrusion','FLOAT' ))
wglUseFontOutlinesW.add( Input( 'format','int' ))
wglUseFontOutlinesW.add( Output( 'lpgmf','LPGLYPHMETRICSFLOAT' ,size = 'count' ))
wglUseFontOutlinesW.version = ''
wglUseFontOutlinesW.category = 'WGL_core'
wglUseFontOutlinesW.trace = True
wglUseFontOutlinesW.play = True
wgl.add(wglUseFontOutlinesW)

