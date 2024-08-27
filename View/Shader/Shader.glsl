---VERTEX SHADER---
#ifdef GL_ES
    precision lowp float;
#endif

varying vec4 frag_color;
varying vec2 tex_coord0;

attribute vec2     vPosition;
attribute vec2     vTexCoords0;

uniform mat4       modelview_mat;
uniform mat4       projection_mat;
uniform vec3       current_color;

void main (void) {
  frag_color = vec4(current_color, 1.0);
  tex_coord0 = vTexCoords0;
  gl_Position = projection_mat * modelview_mat * vec4(vPosition.xy, 0.0, 1.0);
}

---FRAGMENT SHADER---
#ifdef GL_ES
    precision lowp float;
#endif

varying vec4 frag_color;
varying vec2 tex_coord0;

uniform sampler2D texture0;
uniform vec2 resolution;

void main (void){
    gl_FragColor = frag_color * texture2D(texture0, tex_coord0);
}