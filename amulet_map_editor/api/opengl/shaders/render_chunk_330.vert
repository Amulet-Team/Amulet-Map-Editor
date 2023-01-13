#version 330
layout(location = 0) in vec3 positions;
layout(location = 1) in vec2 vTexCoord;
layout(location = 2) in vec4 vTexOffset;
layout(location = 3) in vec3 vTint;

out vec2 fTexCoord;
out vec4 fTexOffset;
out vec3 fTint;

uniform mat4 transformation_matrix;

void main(){
    gl_Position = transformation_matrix * vec4(positions, 1.0);
    fTexCoord = vTexCoord;
    fTexOffset = vTexOffset;
    fTint = vTint;
}