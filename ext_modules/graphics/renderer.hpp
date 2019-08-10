#ifndef _GRAPHICS_RENDERER_HPP
#define _GRAPHICS_RENDERER_HPP


#include "util.hpp"
#include "gl_wrappers.hpp"


struct Viewport {
  ivec2 pos;
  ivec2 size;
};

struct Camera {
  vec3 pos;
  float pitch;
  float yaw;
  float fov_y;
};

struct Surface {
  vec3 vertices[3];
  vec3 color;
};


class Renderer {
public:
  Renderer();

  void clear();
  void set_viewport(const Viewport &viewport);
  void set_camera(const Camera &camera);
  void add_surface(const Surface &surface);
  void add_object(vec3 pos, float height);
  void render();

private:
  Viewport viewport;
  Camera camera;

  struct {
    Program *program;
    VertexArray *vertex_array;
    struct {
      vector<vec3> pos;
      vector<vec3> color;
    } buffers;
  } p_surface;
};


#endif
